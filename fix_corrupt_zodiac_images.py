import os
import glob
from bs4 import BeautifulSoup
import re
import base64

def create_svg_zodiac_image(sign):
    """Create an SVG image for a zodiac sign"""
    colors = {
        'aries': '#FF5733',
        'taurus': '#33FF57',
        'gemini': '#3357FF',
        'cancer': '#FF33F5',
        'leo': '#F5FF33',
        'virgo': '#33FFF5',
        'libra': '#F533FF',
        'scorpio': '#FF3333',
        'sagittarius': '#33FF33',
        'capricorn': '#3333FF',
        'aquarius': '#FF3380',
        'pisces': '#80FF33'
    }
    
    color = colors.get(sign.lower(), '#808080')
    
    # Create SVG
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="400" height="300" viewBox="0 0 400 300">
  <rect width="400" height="300" fill="{color}" opacity="0.7"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" 
        font-family="Arial" font-size="40" fill="white">{sign.title()}</text>
</svg>"""
    
    # Convert to data URI
    svg_bytes = svg.encode('utf-8')
    base64_svg = base64.b64encode(svg_bytes).decode('utf-8')
    data_uri = f"data:image/svg+xml;base64,{base64_svg}"
    
    return data_uri

def fix_horoscope_collection_images(file_path):
    """Fix missing or corrupted zodiac images in collection pages"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Extract zodiac sign from file path
        sign_match = re.search(r'/([a-zA-Z]+)/collection\.html$', file_path)
        if not sign_match:
            return False
        
        current_sign = sign_match.group(1).lower()
        
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find image tags with empty or corrupted sources
        images = soup.find_all('img')
        
        fixed_images = 0
        for img in images:
            src = img.get('src', '')
            
            # Check if image is missing, empty or corrupted
            if not src or 'missing' in src.lower() or 'corrupted' in src.lower() or src.startswith('data:'):
                # Create SVG image for this sign
                svg_uri = create_svg_zodiac_image(current_sign)
                
                # Update image source
                img['src'] = svg_uri
                fixed_images += 1
        
        # Only save if changes were made
        if fixed_images > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Fixed {fixed_images} corrupted image(s) in {file_path}")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Find all horoscope collection files
    collection_files = glob.glob(os.path.join(base_dir, "astrology-reading/today/horoscope/*/collection.html"))
    
    fixed_count = 0
    for file in collection_files:
        if fix_horoscope_collection_images(file):
            fixed_count += 1
    
    print(f"\nSummary: Fixed corrupted images in {fixed_count} zodiac collection files.")
    
    if fixed_count > 0:
        print("\nNext steps:")
        print("1. Refresh your browser (Cmd+Shift+R)")
        print("2. Check if zodiac images now display correctly in collection lists")
    else:
        print("\nNo corrupted zodiac images found or fixes needed.")

if __name__ == "__main__":
    main() 