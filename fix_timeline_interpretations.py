import os
import glob
from bs4 import BeautifulSoup
import shutil
import re

def fix_timeline_interpretations():
    """Fix missing artist interpretation images on visual timeline pages"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Target the visual timeline directory
    timeline_dir = os.path.join(base_dir, "learn-design-trends/modern-relevant-art-history")
    
    if not os.path.exists(timeline_dir):
        print(f"⚠️ Visual timeline directory not found at: {timeline_dir}")
        return False
    
    # Get all HTML files in the timeline directory
    timeline_pages = glob.glob(os.path.join(timeline_dir, "*visual-timeline*.html"))
    
    if not timeline_pages:
        print(f"⚠️ No visual timeline HTML files found")
        return False
    
    print(f"✓ Found {len(timeline_pages)} visual timeline pages to process")
    
    # Define Dropbox path where the images might be
    dropbox_path = "/Users/seanivore/Dropbox"
    
    # Create images directory if it doesn't exist
    target_img_dir = os.path.join(base_dir, "assets/images/visual-timelines")
    os.makedirs(target_img_dir, exist_ok=True)
    
    total_fixed = 0
    
    # Process each timeline page
    for page_path in timeline_pages:
        page_name = os.path.basename(page_path)
        
        # Extract art style from filename
        match = re.search(r'(.+?)-visual-timeline', page_name)
        if match:
            art_style = match.group(1)
        else:
            art_style = page_name.replace('-visual-timeline.html', '')
        
        print(f"\n🔍 Processing timeline page: {page_name} (style: {art_style})")
        
        # Create backup
        backup_path = page_path + ".bak"
        shutil.copy2(page_path, backup_path)
        
        try:
            with open(page_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse the file
            soup = BeautifulSoup(content, 'html.parser')
            
            # Look for image sections that might be empty
            changes_made = False
            
            # Find all image elements
            img_tags = soup.find_all('img')
            broken_imgs = []
            
            for img in img_tags:
                src = img.get('src', '')
                if not src or src.endswith('/'):
                    broken_imgs.append(img)
                elif src.startswith('data:image'):
                    broken_imgs.append(img)
                elif 'placeholder' in src.lower():
                    broken_imgs.append(img)
            
            if broken_imgs:
                print(f"✓ Found {len(broken_imgs)} broken/empty images")
            else:
                print("✓ No broken images found, checking for timeline sections")
            
            # Look for timeline sections
            timeline_sections = []
            
            # Find by heading or section class
            timeline_headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            for header in timeline_headers:
                if "timeline" in header.get_text().lower() or "history" in header.get_text().lower():
                    parent_section = header.find_parent(['section', 'div'])
                    if parent_section:
                        timeline_sections.append(parent_section)
                        print(f"✓ Found timeline section with heading: {header.get_text()}")
            
            # Find any divs with timeline-related classes
            timeline_divs = soup.select('div[class*="timeline"], div[class*="history"], .w-dyn-empty, .w-condition-invisible')
            for div in timeline_divs:
                if div not in timeline_sections:
                    timeline_sections.append(div)
            
            if timeline_sections and not broken_imgs:
                print(f"✓ Found {len(timeline_sections)} potential timeline sections")
                
                # Look for empty containers in these sections
                for section in timeline_sections:
                    empty_containers = section.select('div[role="img"], .w-dyn-empty, .w-condition-invisible')
                    if empty_containers:
                        print(f"✓ Found {len(empty_containers)} empty/broken containers in timeline section")
                        broken_imgs.extend(empty_containers)
            
            # Search for potential timeline images
            potential_images = []
            
            # Check current assets directory for matching images
            for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
                for file in files:
                    if file.endswith((".jpg", ".png", ".webp")):
                        if art_style.lower() in file.lower() and ("timeline" in file.lower() or "history" in file.lower()):
                            potential_images.append(os.path.join(root, file))
            
            # If not found in assets, check Dropbox
            if not potential_images and os.path.exists(dropbox_path):
                print(f"🔍 Looking for timeline images in Dropbox...")
                for root, dirs, files in os.walk(dropbox_path):
                    for file in files:
                        if file.endswith((".jpg", ".png", ".webp")):
                            if art_style.lower() in file.lower() and ("timeline" in file.lower() or "history" in file.lower()):
                                potential_images.append(os.path.join(root, file))
            
            # Try broader search with just the style name
            if not potential_images:
                print(f"🔍 Trying broader search for {art_style} timeline images...")
                
                # Extract key terms from art style
                terms = re.split(r'[-\s]', art_style.lower())
                terms = [t for t in terms if len(t) > 3]
                
                # First check in assets
                for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
                    for file in files:
                        if file.endswith((".jpg", ".png", ".webp")):
                            if any(term in file.lower() for term in terms):
                                if "timeline" in file.lower() or "history" in file.lower() or "evolution" in file.lower():
                                    potential_images.append(os.path.join(root, file))
                
                # Then check Dropbox with broader terms
                if not potential_images and os.path.exists(dropbox_path):
                    print(f"🔍 Checking Dropbox with broader terms...")
                    for root, dirs, files in os.walk(dropbox_path):
                        for file in files:
                            if file.endswith((".jpg", ".png", ".webp")):
                                if any(term in file.lower() for term in terms):
                                    if "timeline" in file.lower() or "history" in file.lower() or "evolution" in file.lower():
                                        potential_images.append(os.path.join(root, file))
            
            # As a last resort, try any images related to the style
            if not potential_images:
                print(f"🔍 Looking for any images related to {art_style}...")
                
                # Extract key terms from art style
                terms = re.split(r'[-\s]', art_style.lower())
                terms = [t for t in terms if len(t) > 3]
                
                for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
                    for file in files:
                        if file.endswith((".jpg", ".png", ".webp")):
                            if any(term in file.lower() for term in terms):
                                potential_images.append(os.path.join(root, file))
                                if len(potential_images) >= 6:
                                    break
                
                # If still not found, check Dropbox
                if len(potential_images) < 3 and os.path.exists(dropbox_path):
                    for root, dirs, files in os.walk(dropbox_path):
                        for file in files:
                            if file.endswith((".jpg", ".png", ".webp")):
                                if any(term in file.lower() for term in terms):
                                    potential_images.append(os.path.join(root, file))
                                    if len(potential_images) >= 6:
                                        break
            
            if potential_images:
                print(f"✓ Found {len(potential_images)} potential images for {art_style} timeline")
                
                # Limit to a reasonable number of images
                potential_images = potential_images[:6]
                
                # Copy images to assets directory if needed
                copied_images = []
                for img_path in potential_images:
                    img_name = os.path.basename(img_path)
                    # Add art style prefix to avoid conflicts
                    if not img_name.startswith(art_style):
                        img_name = f"{art_style}-{img_name}"
                        
                    target_path = os.path.join(target_img_dir, img_name)
                    
                    # Only copy if not already in assets
                    if not os.path.exists(target_path) or not img_path.startswith(base_dir):
                        shutil.copy2(img_path, target_path)
                        print(f"  ✓ Copied {img_name} to assets/images/visual-timelines")
                    
                    # Add to list of available images
                    web_path = f"/assets/images/visual-timelines/{img_name}"
                    copied_images.append(web_path)
                
                # Fix broken images
                if broken_imgs:
                    # Replace broken image sources
                    for i, img in enumerate(broken_imgs):
                        if i < len(copied_images):
                            if img.name == 'img':
                                img['src'] = copied_images[i]
                                # Set appropriate alt text
                                img['alt'] = f"{art_style} timeline visualization"
                                print(f"  ✓ Updated image src to: {copied_images[i]}")
                                changes_made = True
                            else:
                                # This is a container, need to replace with an image
                                new_img = soup.new_tag('img')
                                new_img['src'] = copied_images[i]
                                new_img['alt'] = f"{art_style} timeline visualization"
                                new_img['style'] = 'width: 100%; height: auto; border-radius: 8px;'
                                img.replace_with(new_img)
                                print(f"  ✓ Replaced container with new image: {copied_images[i]}")
                                changes_made = True
                
                # If no broken images were found but we have timeline sections, add a visual timeline section
                elif timeline_sections:
                    # Find a good place to insert our timeline visuals
                    target_section = timeline_sections[0]
                    
                    # Create new visual timeline gallery
                    timeline_div = soup.new_tag('div')
                    timeline_div['class'] = 'visual-timeline-gallery'
                    timeline_div['style'] = 'display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; margin-top: 40px;'
                    
                    # Add a header
                    timeline_header = soup.new_tag('h3')
                    timeline_header['style'] = 'grid-column: 1 / -1; margin-bottom: 20px;'
                    timeline_header.string = f"{art_style.title()} Visual Timeline"
                    timeline_div.append(timeline_header)
                    
                    for img_path in copied_images:
                        # Create figure element
                        figure = soup.new_tag('figure')
                        figure['style'] = 'margin: 0; text-align: center;'
                        
                        # Create image element
                        img = soup.new_tag('img')
                        img['src'] = img_path
                        img['alt'] = f"{art_style} timeline visualization"
                        img['style'] = 'width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'
                        
                        # Create caption
                        figcaption = soup.new_tag('figcaption')
                        figcaption['style'] = 'margin-top: 10px; font-size: 14px; color: #666;'
                        figcaption.string = f"{art_style.title()} Historical Evolution"
                        
                        # Assemble the figure
                        figure.append(img)
                        figure.append(figcaption)
                        timeline_div.append(figure)
                    
                    # Add to the page
                    target_section.append(timeline_div)
                    print(f"  ✓ Added visual timeline gallery with {len(copied_images)} images")
                    changes_made = True
            else:
                print(f"⚠️ No matching images found for {art_style} timeline")
            
            # Save changes
            if changes_made:
                with open(page_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"✅ Fixed visual timeline on {page_name}")
                total_fixed += 1
            else:
                os.remove(backup_path)
                print(f"ℹ️ No changes needed for {page_name}")
        
        except Exception as e:
            # Restore backup on error
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, page_path)
                os.remove(backup_path)
            print(f"❌ Error processing {page_name}: {e}")
    
    return total_fixed

if __name__ == "__main__":
    print("🔍 Fixing missing visual timeline images...")
    total_fixed = fix_timeline_interpretations()
    
    if total_fixed > 0:
        print(f"\n✨ Successfully fixed visual timelines on {total_fixed} pages")
    else:
        print("\n⚠️ No timeline pages were fixed")
    
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. Check the visual timeline pages to see the updated images") 