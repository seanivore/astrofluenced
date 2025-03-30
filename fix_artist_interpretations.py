import os
import glob
from bs4 import BeautifulSoup
import shutil
import re

def fix_artist_interpretations():
    """Fix missing artist interpretation images on design trends pages"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Target the design-trends directory
    design_trends_dir = os.path.join(base_dir, "learn-design-trends")
    
    if not os.path.exists(design_trends_dir):
        print(f"⚠️ Design trends directory not found at: {design_trends_dir}")
        return False
    
    # Get all HTML files in the design-trends directory
    design_trends_pages = glob.glob(os.path.join(design_trends_dir, "*.html"))
    
    # Also check subdirectories if the files might be nested
    if not design_trends_pages:
        design_trends_pages = glob.glob(os.path.join(design_trends_dir, "**/*.html"), recursive=True)
    
    if not design_trends_pages:
        print(f"⚠️ No HTML files found in design-trends directory")
        return False
    
    print(f"✓ Found {len(design_trends_pages)} design trend pages to process")
    
    # Define Dropbox path where the images might be
    dropbox_path = "/Users/seanivore/Dropbox"
    
    # Create images directory if it doesn't exist
    target_img_dir = os.path.join(base_dir, "assets/images/artist-interpretations")
    os.makedirs(target_img_dir, exist_ok=True)
    
    total_fixed = 0
    
    # Process each design trends page
    for page_path in design_trends_pages:
        page_name = os.path.basename(page_path)
        art_style = os.path.splitext(page_name)[0]
        
        print(f"\n🔍 Processing design trend page: {page_name}")
        
        # Create backup
        backup_path = page_path + ".bak"
        shutil.copy2(page_path, backup_path)
        
        try:
            with open(page_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse the file
            soup = BeautifulSoup(content, 'html.parser')
            
            # Look for the "Artist Interpretations" section
            artist_sections = []
            
            # Find by heading text
            headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            for header in headers:
                if "Artist Interpretations" in header.get_text():
                    print(f"✓ Found 'Artist Interpretations' section")
                    # Get the parent section
                    parent_section = header.find_parent(['section', 'div'])
                    if parent_section:
                        artist_sections.append(parent_section)
            
            if not artist_sections:
                print(f"⚠️ No 'Artist Interpretations' section found on page: {page_name}")
                os.remove(backup_path)
                continue
            
            changes_made = False
            
            for section in artist_sections:
                # Find all image tags in the section
                img_tags = section.find_all('img')
                
                if not img_tags:
                    print(f"⚠️ No image tags found in 'Artist Interpretations' section")
                    
                    # Try to find broken image containers
                    empty_containers = section.select('div[role="img"], .w-dyn-empty, .w-condition-invisible')
                    if empty_containers:
                        print(f"✓ Found {len(empty_containers)} empty/broken image containers")
                else:
                    print(f"✓ Found {len(img_tags)} image tags in section")
                
                # Look for potential image files in the assets directory
                potential_images = []
                
                # Check current assets directory
                for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
                    for file in files:
                        if file.endswith((".jpg", ".png", ".webp")) and art_style.lower() in file.lower():
                            if "artist" in file.lower() or "interpretation" in file.lower() or "art" in file.lower():
                                potential_images.append(os.path.join(root, file))
                
                # If not found in assets, check Dropbox
                if not potential_images and os.path.exists(dropbox_path):
                    print(f"🔍 Looking for images in Dropbox...")
                    for root, dirs, files in os.walk(dropbox_path):
                        for file in files:
                            if file.endswith((".jpg", ".png", ".webp")) and art_style.lower() in file.lower():
                                if "artist" in file.lower() or "interpretation" in file.lower() or "art" in file.lower():
                                    potential_images.append(os.path.join(root, file))
                
                # If still not found, try broader search
                if not potential_images:
                    print(f"🔍 Trying broader search for {art_style} art...")
                    
                    # Extract key terms from art style
                    terms = re.split(r'[-\s]', art_style.lower())
                    
                    for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
                        for file in files:
                            if file.endswith((".jpg", ".png", ".webp")):
                                # Check if any term matches
                                if any(term in file.lower() for term in terms if len(term) > 3):
                                    if "artist" in file.lower() or "art" in file.lower() or "style" in file.lower():
                                        potential_images.append(os.path.join(root, file))
                    
                    # If still not found, check Dropbox with broader terms
                    if not potential_images and os.path.exists(dropbox_path):
                        print(f"🔍 Checking Dropbox with broader terms...")
                        for root, dirs, files in os.walk(dropbox_path):
                            for file in files:
                                if file.endswith((".jpg", ".png", ".webp")):
                                    if any(term in file.lower() for term in terms if len(term) > 3):
                                        if "artist" in file.lower() or "art" in file.lower() or "style" in file.lower():
                                            potential_images.append(os.path.join(root, file))
                
                if potential_images:
                    print(f"✓ Found {len(potential_images)} potential images related to {art_style}")
                    
                    # Limit to a reasonable number of images (max 6)
                    potential_images = potential_images[:6]
                    
                    # Copy images to assets directory if needed
                    copied_images = []
                    for img_path in potential_images:
                        img_name = os.path.basename(img_path)
                        target_path = os.path.join(target_img_dir, img_name)
                        
                        # Only copy if not already in assets
                        if not os.path.exists(target_path) or not img_path.startswith(base_dir):
                            shutil.copy2(img_path, target_path)
                            print(f"  ✓ Copied {img_name} to assets/images/artist-interpretations")
                        
                        # Add to list of available images
                        web_path = f"/assets/images/artist-interpretations/{img_name}"
                        copied_images.append(web_path)
                    
                    # Handle broken images in the page
                    if img_tags:
                        # Replace broken image sources
                        for i, img in enumerate(img_tags):
                            src = img.get('src', '')
                            if i < len(copied_images):
                                img['src'] = copied_images[i]
                                print(f"  ✓ Updated image src to: {copied_images[i]}")
                                changes_made = True
                    else:
                        # Create new image gallery
                        gallery_div = soup.new_tag('div')
                        gallery_div['class'] = 'artist-interpretation-gallery'
                        gallery_div['style'] = 'display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; margin-top: 30px;'
                        
                        for img_path in copied_images:
                            # Create figure element
                            figure = soup.new_tag('figure')
                            figure['style'] = 'margin: 0; text-align: center;'
                            
                            # Create image element
                            img = soup.new_tag('img')
                            img['src'] = img_path
                            img['alt'] = f"{art_style} artist interpretation"
                            img['style'] = 'width: 100%; height: auto; border-radius: 8px;'
                            
                            # Create caption
                            figcaption = soup.new_tag('figcaption')
                            figcaption['style'] = 'margin-top: 8px; font-size: 14px; color: #aaa;'
                            figcaption.string = f"Artist's {art_style} interpretation"
                            
                            # Assemble the figure
                            figure.append(img)
                            figure.append(figcaption)
                            gallery_div.append(figure)
                        
                        # Find where to insert gallery
                        if empty_containers:
                            # Replace first empty container with gallery
                            empty_containers[0].replace_with(gallery_div)
                        else:
                            # Append to section
                            section.append(gallery_div)
                        
                        print(f"  ✓ Added image gallery with {len(copied_images)} images")
                        changes_made = True
                else:
                    print(f"⚠️ No matching images found for {art_style}")
            
            # Save changes
            if changes_made:
                with open(page_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"✅ Fixed artist interpretations on {page_name}")
                total_fixed += 1
            else:
                os.remove(backup_path)
        
        except Exception as e:
            # Restore backup on error
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, page_path)
                os.remove(backup_path)
            print(f"❌ Error processing {page_name}: {e}")
    
    return total_fixed

if __name__ == "__main__":
    print("🔍 Fixing missing artist interpretation images...")
    total_fixed = fix_artist_interpretations()
    
    if total_fixed > 0:
        print(f"\n✨ Successfully fixed artist interpretations on {total_fixed} pages")
    else:
        print("\n⚠️ No pages were fixed")
    
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. Check design trends pages to see the artist interpretation images") 