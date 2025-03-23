import os
from bs4 import BeautifulSoup
import time
import shutil
import requests

def download_specific_images():
    """Download backup images for the problematic zodiac signs"""
    cdn_base = "https://cdn.prod.website-files.com/63eeb040bbd9e6ee6a1ef49e/"
    zodiac_images = {
        'sagittarius': '6519e1c3ba01c1e23430833e_09-25-2023-sagittarius-horoscope%20collection.webp',
        'leo': '6519e262b2d820de93ef9144_09-25-2023-leo-horoscope%20collection.webp',
        'gemini': '6519e29e538e0b47baf4482c_09-25-2023-gemini-horoscope%20collection.webp',
        'taurus': '6519e2b9f5bb2df8dd5d4711_09-25-2023-taurus-horoscope%20collection.webp',
    }
    
    backup_dir = "/Users/seanivore/Development/astrofluenced/assets/downloaded/backup_images"
    os.makedirs(backup_dir, exist_ok=True)
    
    for sign, filename in zodiac_images.items():
        # Try to download directly from CDN
        cdn_url = cdn_base + filename
        local_path = f"/Users/seanivore/Development/astrofluenced/assets/downloaded/images/{filename}"
        backup_path = f"{backup_dir}/{sign}_backup.webp"
        
        print(f"Attempting to download image for {sign} from {cdn_url}")
        
        # First check if the file exists
        if os.path.exists(local_path):
            print(f"Original file exists at {local_path}, creating backup")
            # Create a backup copy
            shutil.copy(local_path, backup_path)
        else:
            # Try to download
            try:
                response = requests.get(cdn_url, stream=True)
                if response.status_code == 200:
                    with open(local_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print(f"Successfully downloaded {local_path}")
                    # Also create a backup
                    shutil.copy(local_path, backup_path)
                else:
                    # Download generic zodiac image as backup
                    print(f"Failed to download from CDN, creating generic backup for {sign}")
                    with open(backup_path, 'wb') as f:
                        # This creates an empty file as a placeholder
                        pass
            except Exception as e:
                print(f"Error downloading {cdn_url}: {e}")

def fix_specific_zodiac_images(homepage_path):
    """Fix specific zodiac image references"""
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
            
            # Check if this is one of our problem signs
            if sign in ['sagittarius', 'leo', 'gemini', 'taurus']:
                img_tag = item.select_one('img')
                if img_tag:
                    # Get current src
                    current_src = img_tag.get('src', '')
                    
                    # Log the current src for debugging
                    print(f"Found {sign} image with src: {current_src}")
                    
                    # If image path exists but image might be corrupt, try with backup
                    local_path = current_src.split('?')[0] if '?' in current_src else current_src
                    backup_path = f"assets/downloaded/backup_images/{sign}_backup.webp?v={int(time.time())}"
                    
                    # Use direct file existence check
                    full_path = f"/Users/seanivore/Development/astrofluenced/{local_path}"
                    if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
                        # Force a cache refresh
                        img_tag['src'] = f"{local_path}?v={int(time.time())}"
                        print(f"Updated {sign} to use refresh: {img_tag['src']}")
                    else:
                        # Use backup image
                        img_tag['src'] = backup_path
                        print(f"Updated {sign} to use backup: {backup_path}")
        
        # Save the modified file
        with open(homepage_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"Successfully updated homepage with fixed zodiac image references")
        
    except Exception as e:
        print(f"Error processing homepage: {e}")

def main():
    homepage_path = "/Users/seanivore/Development/astrofluenced/index.html"
    
    # First download/backup images
    download_specific_images()
    
    # Then fix references in homepage
    fix_specific_zodiac_images(homepage_path)
    
    print("\nNext steps:")
    print("1. Refresh the homepage in your browser (Cmd+Shift+R)")
    print("2. Check if the previously missing zodiac images are now visible")

if __name__ == "__main__":
    main() 