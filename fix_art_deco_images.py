import os
import glob
from bs4 import BeautifulSoup
import shutil
import re

def fix_art_deco_images():
    """Fix art deco images on both timeline and main pages"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Target art deco pages
    art_deco_pages = []
    
    # Main art deco page
    main_page = os.path.join(base_dir, "learn-design-trends/art-deco-evolving-maximalism-geometry.html")
    if os.path.exists(main_page):
        art_deco_pages.append(main_page)
    
    # Timeline page
    timeline_page = os.path.join(base_dir, "learn-design-trends/modern-relevant-art-history/art-deco-visual-timeline.html")
    if os.path.exists(timeline_page):
        art_deco_pages.append(timeline_page)
    
    if not art_deco_pages:
        print(f"⚠️ No Art Deco pages found")
        return False
    
    print(f"✓ Found {len(art_deco_pages)} Art Deco pages to process")
    
    # Search for art deco images in the entire project
    art_deco_images = []
    
    # First check assets directory
    for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
        for file in files:
            if file.endswith((".jpg", ".png", ".webp", ".jpeg", ".gif")):
                if "art" in file.lower() and "deco" in file.lower():
                    art_deco_images.append(os.path.join(root, file))
    
    # Dropbox path
    dropbox_path = "/Users/seanivore/Dropbox"
    
    # If not enough images found, check Dropbox
    if len(art_deco_images) < 5 and os.path.exists(dropbox_path):
        print(f"🔍 Looking for Art Deco images in Dropbox...")
        for root, dirs, files in os.walk(dropbox_path):
            for file in files:
                if file.endswith((".jpg", ".png", ".webp", ".jpeg", ".gif")):
                    if "art" in file.lower() and "deco" in file.lower():
                        art_deco_images.append(os.path.join(root, file))
                        if len(art_deco_images) >= 20:  # Limit search
                            break
    
    # Try broader search if still not enough
    if len(art_deco_images) < 5:
        print(f"🔍 Broadening search for Art Deco images...")
        for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
            for file in files:
                if file.endswith((".jpg", ".png", ".webp", ".jpeg", ".gif")):
                    if "deco" in file.lower() or ("art" in file.lower() and "1920" in file.lower()):
                        if file not in art_deco_images:
                            art_deco_images.append(os.path.join(root, file))
    
    if not art_deco_images:
        print(f"⚠️ No Art Deco images found")
        return False
    
    print(f"✓ Found {len(art_deco_images)} Art Deco images to use")
    
    # Create directories for images
    timeline_img_dir = os.path.join(base_dir, "assets/images/visual-timelines")
    artist_img_dir = os.path.join(base_dir, "assets/images/artist-interpretations")
    os.makedirs(timeline_img_dir, exist_ok=True)
    os.makedirs(artist_img_dir, exist_ok=True)
    
    total_fixed = 0
    
    # Process each page
    for page_path in art_deco_pages:
        page_name = os.path.basename(page_path)
        print(f"\n🔍 Processing page: {page_name}")
        
        # Create backup
        backup_path = page_path + ".bak"
        shutil.copy2(page_path, backup_path)
        
        try:
            with open(page_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse the file
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find all images on the page
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
                elif any(x in src.lower() for x in ['/art-deco/', 'art-deco-', 'art_deco']):
                    # Check if the image actually exists
                    img_path = os.path.join(base_dir, src.lstrip('/'))
                    if not os.path.exists(img_path):
                        print(f"⚠️ Image does not exist: {src}")
                        broken_imgs.append(img)
            
            if broken_imgs:
                print(f"✓ Found {len(broken_imgs)} broken/missing images")
                
                # Copy Art Deco images to appropriate folders
                copied_images = []
                
                for img_path in art_deco_images[:len(broken_imgs) + 5]:  # Get a few extra
                    img_name = os.path.basename(img_path)
                    
                    # Determine target directory based on context
                    if "timeline" in page_name.lower():
                        target_dir = timeline_img_dir
                        prefix = "art-deco-timeline-"
                    else:
                        target_dir = artist_img_dir
                        prefix = "art-deco-"
                    
                    # Add prefix if not already there
                    if not img_name.startswith("art-deco"):
                        img_name = f"{prefix}{img_name}"
                    
                    target_path = os.path.join(target_dir, img_name)
                    
                    # Copy the image if it doesn't exist
                    if not os.path.exists(target_path):
                        shutil.copy2(img_path, target_path)
                        print(f"  ✓ Copied {img_name}")
                    
                    # Add to list with web path
                    if "timeline" in page_name.lower():
                        web_path = f"/assets/images/visual-timelines/{img_name}"
                    else:
                        web_path = f"/assets/images/artist-interpretations/{img_name}"
                    
                    copied_images.append(web_path)
                    
                    # If we have enough images, break
                    if len(copied_images) >= len(broken_imgs) + 5:
                        break
                
                # Fix broken images
                changes_made = False
                
                for i, img in enumerate(broken_imgs):
                    if i < len(copied_images):
                        img['src'] = copied_images[i]
                        print(f"  ✓ Fixed image: {img.get('alt', 'No alt')} -> {copied_images[i]}")
                        changes_made = True
                
                # Save changes
                if changes_made:
                    with open(page_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    print(f"✅ Fixed images on {page_name}")
                    total_fixed += 1
                else:
                    print(f"ℹ️ No changes made to {page_name}")
                    os.remove(backup_path)
            else:
                print(f"✓ No broken images found on {page_name}")
                os.remove(backup_path)
        
        except Exception as e:
            # Restore backup on error
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, page_path)
                os.remove(backup_path)
            print(f"❌ Error processing {page_name}: {e}")
    
    return total_fixed

if __name__ == "__main__":
    print("🔍 Fixing Art Deco images...")
    total_fixed = fix_art_deco_images()
    
    if total_fixed > 0:
        print(f"\n✨ Successfully fixed images on {total_fixed} Art Deco pages")
    else:
        print("\n⚠️ No Art Deco pages were fixed")
    
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. Check Art Deco pages to see if the images are displaying correctly") 