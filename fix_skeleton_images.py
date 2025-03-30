import os
from bs4 import BeautifulSoup
import shutil

def fix_skeleton_images():
    """Fix missing skeleton images on the about page"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # About page path
    about_page = os.path.join(base_dir, "about/seanivore-house-llc-brands.html")
    
    if not os.path.exists(about_page):
        print(f"⚠️ About page not found at: {about_page}")
        return False
    
    # Create backup
    backup_path = about_page + ".bak"
    shutil.copy2(about_page, backup_path)
    
    # Skeleton image paths
    skeleton_images = {
        "skeleton-prayer-R": "/assets/downloaded/images/64e5ed612820e6e33ee2cf91_skeleton-prayer-R.webp",
        "skeleton-prayer-L": "/assets/downloaded/images/64e5ed612820e6e33ee2cf91_skeleton-prayer-L.webp"
    }
    
    # Check if these images exist in the website structure
    for img_name, img_path in skeleton_images.items():
        full_path = os.path.join(base_dir, img_path.lstrip('/'))
        if not os.path.exists(full_path):
            alt_path = os.path.join(base_dir, "assets/images", os.path.basename(img_path))
            if os.path.exists(alt_path):
                print(f"✓ Found skeleton image in alternate location: {alt_path}")
                # Update the path
                skeleton_images[img_name] = "/assets/images/" + os.path.basename(img_path)
            else:
                print(f"⚠️ Skeleton image not found: {img_path}")
                # Try to find it in the repository
                potential_matches = []
                for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
                    for file in files:
                        if "skeleton" in file.lower() and file.endswith((".webp", ".png", ".jpg")):
                            potential_matches.append(os.path.join(root, file))
                
                if potential_matches:
                    print(f"🔍 Found potential skeleton images:")
                    for i, match in enumerate(potential_matches):
                        rel_path = os.path.relpath(match, base_dir)
                        print(f"  {i+1}. /{rel_path}")
                        if "skeleton-prayer" in match.lower():
                            if "r" in os.path.basename(match).lower() and "skeleton-prayer-R" in skeleton_images:
                                skeleton_images["skeleton-prayer-R"] = "/" + rel_path
                                print(f"    ✓ Using this for skeleton-prayer-R")
                            elif "l" in os.path.basename(match).lower() and "skeleton-prayer-L" in skeleton_images:
                                skeleton_images["skeleton-prayer-L"] = "/" + rel_path
                                print(f"    ✓ Using this for skeleton-prayer-L")
    
    # Open and parse the about page
    try:
        with open(about_page, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find broken image tags
        img_tags = soup.find_all('img')
        changes_made = False
        
        for img in img_tags:
            src = img.get('src', '')
            
            # Check if this is a broken skeleton image
            if any(skeleton in src for skeleton in ["skeleton-prayer", "skeleton"]):
                print(f"🔍 Found potential skeleton image tag with src: {src}")
                
                # Determine if it's the left or right skeleton
                if "r" in src.lower() or "right" in src.lower():
                    img['src'] = skeleton_images["skeleton-prayer-R"]
                    changes_made = True
                    print(f"  ✓ Updated right skeleton image to: {skeleton_images['skeleton-prayer-R']}")
                elif "l" in src.lower() or "left" in src.lower():
                    img['src'] = skeleton_images["skeleton-prayer-L"]
                    changes_made = True
                    print(f"  ✓ Updated left skeleton image to: {skeleton_images['skeleton-prayer-L']}")
        
        # If broken images were fixed, save the file
        if changes_made:
            with open(about_page, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"✅ Fixed skeleton images on about page")
            return True
        else:
            # If we've found the skeleton images in the src but they're still broken,
            # let's try a different approach - we'll add the images directly
            
            # Find the main container where skeletons should be
            main_container = soup.find('div', class_=lambda c: c and 'container' in c)
            if main_container:
                # Look for text between skeletons
                text_blocks = main_container.find_all(['p', 'div'], class_=lambda c: c and 'text' in (c or ''))
                
                for text_block in text_blocks:
                    # Check if this is the block that should have skeletons on either side
                    if len(text_block.get_text().strip()) > 100:  # Assuming it's a substantial text block
                        parent = text_block.parent
                        
                        # Add skeleton images before and after
                        left_skeleton = soup.new_tag('img')
                        left_skeleton['src'] = skeleton_images["skeleton-prayer-L"]
                        left_skeleton['alt'] = "Skeleton Prayer Left"
                        left_skeleton['style'] = "width: 150px; height: auto; margin-right: 20px;"
                        
                        right_skeleton = soup.new_tag('img')
                        right_skeleton['src'] = skeleton_images["skeleton-prayer-R"] 
                        right_skeleton['alt'] = "Skeleton Prayer Right"
                        right_skeleton['style'] = "width: 150px; height: auto; margin-left: 20px;"
                        
                        # Create container div for the row
                        container_div = soup.new_tag('div')
                        container_div['style'] = "display: flex; align-items: center; justify-content: center; margin: 30px 0;"
                        
                        # Add left skeleton, text and right skeleton to container
                        container_div.append(left_skeleton)
                        
                        # Create center text div
                        center_text = soup.new_tag('div')
                        center_text['style'] = "background: rgba(0,0,0,0.7); padding: 20px; border-radius: 8px; max-width: 60%;"
                        center_text.append(text_block)
                        
                        container_div.append(center_text)
                        container_div.append(right_skeleton)
                        
                        # Replace the text block with our new container
                        text_block.replace_with(container_div)
                        
                        changes_made = True
                        print(f"✅ Added skeleton images around text block")
                        break
            
            if changes_made:
                with open(about_page, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"✅ Fixed skeleton images on about page")
                return True
            else:
                print(f"❌ Could not locate where to add skeleton images")
                os.remove(backup_path)  # Remove backup as no changes were made
                return False
    
    except Exception as e:
        print(f"❌ Error fixing skeleton images: {e}")
        # Restore from backup
        if os.path.exists(backup_path):
            shutil.copy2(backup_path, about_page)
        return False

def check_style_spectrum():
    """Check the style spectrum art history section"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    style_spectrum_path = os.path.join(base_dir, "the-style-spectrum.html")
    
    if not os.path.exists(style_spectrum_path):
        print(f"⚠️ Style spectrum page not found at: {style_spectrum_path}")
        return
    
    try:
        with open(style_spectrum_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Get main sections
        sections = soup.find_all(['section', 'div'], class_=lambda c: c and 'section' in (c or ''))
        
        print("\n🎨 Style Spectrum Content Overview:")
        print("--------------------------------")
        
        for section in sections:
            # Try to identify the section by heading
            heading = section.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if heading:
                print(f"• Section: {heading.get_text().strip()}")
                
                # Count images
                images = section.find_all('img')
                if images:
                    print(f"  - Contains {len(images)} images")
                
                # Check for text content
                paragraphs = section.find_all('p')
                if paragraphs:
                    total_text = sum(len(p.get_text()) for p in paragraphs)
                    print(f"  - Contains {len(paragraphs)} paragraphs ({total_text} characters)")
        
        print("--------------------------------")
        
    except Exception as e:
        print(f"❌ Error checking style spectrum: {e}")

if __name__ == "__main__":
    print("🔍 Checking for missing skeleton images...")
    fix_skeleton_images()
    
    print("\n🔍 Checking style spectrum art history section...")
    check_style_spectrum() 