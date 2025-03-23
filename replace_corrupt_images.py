import os
import requests
from bs4 import BeautifulSoup
import time
import shutil

def download_replacement_images():
    """Download replacement images for the problematic zodiac signs"""
    # Using placeholder image URLs (replace with actual URLs if needed)
    zodiac_replacements = {
        'sagittarius': 'https://dummyimage.com/600x400/c157e8/fff&text=Sagittarius',
        'leo': 'https://dummyimage.com/600x400/e8578c/fff&text=Leo',
        'gemini': 'https://dummyimage.com/600x400/57e883/fff&text=Gemini',
        'taurus': 'https://dummyimage.com/600x400/5792e8/fff&text=Taurus'
    }
    
    # Create the replacement directory
    replacement_dir = "/Users/seanivore/Development/astrofluenced/assets/downloaded/replacement_images"
    os.makedirs(replacement_dir, exist_ok=True)
    
    for sign, url in zodiac_replacements.items():
        replacement_path = f"{replacement_dir}/{sign}.webp"
        
        try:
            print(f"Downloading replacement image for {sign} from {url}")
            response = requests.get(url, stream=True)
            
            if response.status_code == 200:
                with open(replacement_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Successfully downloaded replacement for {sign}")
            else:
                print(f"Failed to download replacement for {sign}: Status code {response.status_code}")
        except Exception as e:
            print(f"Error downloading replacement for {sign}: {e}")

def replace_problematic_images(homepage_path):
    """Replace problematic zodiac images with new ones"""
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
                    # Replace with new image
                    new_src = f"assets/downloaded/replacement_images/{sign}.webp?v={int(time.time())}"
                    old_src = img_tag.get('src', '')
                    
                    print(f"Replacing {sign} image src: {old_src} -> {new_src}")
                    img_tag['src'] = new_src
        
        # Save the modified file
        with open(homepage_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        print(f"Successfully updated homepage with replacement zodiac images")
        
    except Exception as e:
        print(f"Error replacing images: {e}")

def main():
    homepage_path = "/Users/seanivore/Development/astrofluenced/index.html"
    
    # First download replacement images
    download_replacement_images()
    
    # Then update the HTML
    replace_problematic_images(homepage_path)
    
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. The problematic zodiac images should now be replaced with placeholders")
    print("3. Once confirmed working, you can replace the placeholders with proper zodiac images")

if __name__ == "__main__":
    main() 