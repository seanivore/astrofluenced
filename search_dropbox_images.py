import os
import glob
import re
import shutil
from bs4 import BeautifulSoup
import time

def extract_original_filenames():
    """Extract original filenames from the problematic Webflow URLs"""
    # Problematic images with their Webflow IDs
    problematic_images = {
        'sagittarius': '6519e1c3ba01c1e23430833e_09-25-2023-sagittarius-horoscope collection.webp',
        'leo': '6519e262b2d820de93ef9144_09-25-2023-leo-horoscope collection.webp',
        'gemini': '6519e29e538e0b47baf4482c_09-25-2023-gemini-horoscope collection.webp',
        'taurus': '6519e2b9f5bb2df8dd5d4711_09-25-2023-taurus-horoscope collection.webp',
    }
    
    # Extract the original filename part (after the underscore)
    original_filenames = {}
    for sign, webflow_name in problematic_images.items():
        match = re.search(r'_(.+)$', webflow_name)
        if match:
            original_filenames[sign] = match.group(1).replace('%20', ' ')
        else:
            original_filenames[sign] = webflow_name
    
    return original_filenames

def search_system_for_files(base_paths, original_filenames):
    """Search for the original files across the system"""
    found_files = {}
    
    for sign, filename in original_filenames.items():
        # Create search patterns (exact and partial matches)
        name_part = filename.split('.')[0]
        patterns = [
            f"**/*{filename}",  # Exact match
            f"**/*{name_part}*",  # Partial match with the name part
            f"**/*{sign}*horoscope*.webp",  # Matching by sign name and type
            f"**/*{sign}*.webp",  # Any file with the sign name and webp ext
        ]
        
        found = False
        
        for base_path in base_paths:
            if not os.path.exists(base_path):
                print(f"Path does not exist: {base_path}")
                continue
                
            for pattern in patterns:
                search_pattern = os.path.join(base_path, pattern)
                matches = glob.glob(search_pattern, recursive=True)
                
                if matches:
                    found_files[sign] = matches[0]  # Use the first match
                    print(f"Found file for {sign}: {matches[0]}")
                    found = True
                    break
            
            if found:
                break
        
        if not found:
            print(f"No file found for {sign} with patterns: {patterns}")
    
    return found_files

def update_homepage_with_found_files(homepage_path, found_files):
    """Update the homepage with the found files"""
    try:
        with open(homepage_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Parse the HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all horoscope collection items
        horoscope_items = soup.select('.collection-item-13.homepage.horoscopes')
        
        for item in horoscope_items:
            # Find the zodiac sign name from the text
            sign_text = item.select_one('.text.homepage.reverse')
            if not sign_text:
                continue
            
            sign = sign_text.text.strip().lower()
            
            # Check if this is one of our problem signs and we found a file
            if sign in found_files:
                img_tag = item.select_one('img')
                if img_tag:
                    # Copy the found file to our assets directory
                    found_file = found_files[sign]
                    filename = os.path.basename(found_file)
                    
                    target_dir = "/Users/seanivore/Development/astrofluenced/assets/downloaded/found_images"
                    os.makedirs(target_dir, exist_ok=True)
                    
                    target_path = os.path.join(target_dir, f"{sign}_{filename}")
                    shutil.copy(found_file, target_path)
                    
                    # Update the image source
                    rel_path = f"assets/downloaded/found_images/{os.path.basename(target_path)}?v={int(time.time())}"
                    old_src = img_tag.get('src', '')
                    
                    print(f"Updating {sign} image src: {old_src} -> {rel_path}")
                    img_tag['src'] = rel_path
        
        # Save the modified file
        with open(homepage_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"Successfully updated homepage with found zodiac images")
        
    except Exception as e:
        print(f"Error updating homepage: {e}")

def main():
    homepage_path = "/Users/seanivore/Development/astrofluenced/index.html"
    
    # Paths to search for the original files
    search_paths = [
        "/Users/seanivore/Dropbox",  # Primary Dropbox location
        "/Users/seanivore/Downloads",  # Downloads folder
        "/Users/seanivore/Desktop",  # Desktop folder
        "/Users/seanivore/Documents",  # Documents folder
        "/Users/seanivore/Pictures",  # Pictures folder
    ]
    
    # Extract original filenames
    original_filenames = extract_original_filenames()
    print(f"Looking for original files: {original_filenames}")
    
    # Search for files
    found_files = search_system_for_files(search_paths, original_filenames)
    
    if found_files:
        # Update homepage with found files
        update_homepage_with_found_files(homepage_path, found_files)
        
        print("\nNext steps:")
        print("1. Hard refresh your browser (Cmd+Shift+R)")
        print("2. Check if the previously missing zodiac images are now visible")
    else:
        print("\nNo matching files were found. Try the following alternatives:")
        print("1. Check if the placeholder images from the previous script are visible")
        print("2. Use the browser's developer tools to see if there are errors loading the images")
        print("3. Try downloading the images directly from the Webflow CDN")

if __name__ == "__main__":
    main() 