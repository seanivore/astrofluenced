import os
import glob
from bs4 import BeautifulSoup
import re
import base64
import shutil

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
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="600" viewBox="0 0 1200 600">
  <rect width="1200" height="600" fill="{color}" opacity="0.7"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" 
        font-family="Arial" font-size="80" fill="white">{sign.title()} Horoscope</text>
</svg>"""
    
    # Convert to data URI
    svg_bytes = svg.encode('utf-8')
    base64_svg = base64.b64encode(svg_bytes).decode('utf-8')
    data_uri = f"data:image/svg+xml;base64,{base64_svg}"
    
    return data_uri

def find_alternate_zodiac_image(sign):
    """Search for alternative zodiac images in the assets directory"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Try a few potential locations
    potential_paths = [
        os.path.join(base_dir, f"assets/downloaded/images/*{sign}*.{ext}") 
        for ext in ['jpg', 'jpeg', 'png', 'webp', 'svg']
    ]
    
    # Add potential paths in subdirectories
    potential_paths.extend([
        os.path.join(base_dir, f"assets/downloaded/**/*{sign}*.{ext}")
        for ext in ['jpg', 'jpeg', 'png', 'webp', 'svg']
    ])
    
    # Check if any of these files exist
    for pattern in potential_paths:
        matches = glob.glob(pattern, recursive=True)
        if matches:
            # Return the first match
            return matches[0]
    
    return None

def fix_header_images(file_path):
    """Fix missing or corrupted header images in collection pages"""
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
        
        # Look specifically for header images - likely in a hero section or banner
        header_sections = soup.select('.hero-section, .banner, .header, header, .masthead, .hero')
        
        if not header_sections:
            # If no specific header sections, try to find the first large image at the top of the page
            header_sections = [soup.find('body')]  # Use body as fallback
        
        fixed_images = 0
        
        for section in header_sections:
            # Find images in this section
            images = section.find_all('img')
            
            for img in images:
                src = img.get('src', '')
                
                # Check if image is missing, empty or corrupted
                if not src or 'missing' in src.lower() or 'corrupted' in src.lower() or src.startswith('data:'):
                    # Try to find an alternate image first
                    alt_image = find_alternate_zodiac_image(current_sign)
                    
                    if alt_image:
                        # Create a copy in a consistent location
                        target_dir = os.path.join("/Users/seanivore/Development/astrofluenced/assets/downloaded/zodiac_headers")
                        os.makedirs(target_dir, exist_ok=True)
                        
                        file_ext = os.path.splitext(alt_image)[1]
                        target_file = os.path.join(target_dir, f"{current_sign}_header{file_ext}")
                        
                        # Copy the file
                        shutil.copy(alt_image, target_file)
                        
                        # Use a relative path
                        rel_path = os.path.relpath(target_file, start=os.path.dirname(file_path))
                        
                        # Update the source
                        img['src'] = rel_path
                        print(f"Updated header image for {current_sign} with alternate image")
                    else:
                        # No alternate found, use SVG
                        svg_uri = create_svg_zodiac_image(current_sign)
                        img['src'] = svg_uri
                        print(f"Updated header image for {current_sign} with SVG placeholder")
                    
                    fixed_images += 1
                    break  # Just fix the first corrupted image in each section
        
        # Next, check images in collection list items that might be thumbnails
        list_items = soup.select('.collection-item, .w-dyn-item')
        
        for item in list_items:
            # Find images in this list item
            images = item.find_all('img')
            
            for img in images:
                src = img.get('src', '')
                
                # Check if image is missing, empty or corrupted
                if not src or 'missing' in src.lower() or 'corrupted' in src.lower() or src.startswith('data:'):
                    # Create SVG image for this sign
                    svg_uri = create_svg_zodiac_image(current_sign)
                    
                    # Update image source with smaller thumbnail size
                    img['src'] = svg_uri
                    img['width'] = '300'
                    img['height'] = '200'
                    fixed_images += 1
        
        # Only save if changes were made
        if fixed_images > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Fixed {fixed_images} image(s) in {file_path}")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def fix_main_horoscope_page():
    """Fix the main horoscopes.html page that shows thumbnails of all signs"""
    try:
        file_path = "/Users/seanivore/Development/astrofluenced/astrology-reading/today/horoscopes.html"
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find collection item images - these are likely thumbnails for each sign
        collection_items = soup.select('.collection-item, .w-dyn-item')
        
        fixed_images = 0
        
        # Go through each collection item
        for item in collection_items:
            # Try to find which zodiac sign this is for
            sign_text = item.get_text().lower()
            
            # Check for any zodiac sign name in the text
            sign = None
            for zodiac in ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                          'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']:
                if zodiac in sign_text:
                    sign = zodiac
                    break
            
            if not sign:
                continue
                
            # Find images in this item
            images = item.find_all('img')
            
            for img in images:
                src = img.get('src', '')
                
                # Check if image is missing, empty or corrupted
                if not src or 'missing' in src.lower() or 'corrupted' in src.lower() or src.startswith('data:'):
                    # Create SVG image for this sign
                    svg_uri = create_svg_zodiac_image(sign)
                    
                    # Update image source
                    img['src'] = svg_uri
                    img['width'] = '300'
                    img['height'] = '200'
                    
                    fixed_images += 1
        
        # Only save if changes were made
        if fixed_images > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Fixed {fixed_images} image(s) in main horoscopes page")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error fixing main horoscopes page: {e}")
        return False

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Find all horoscope collection files
    collection_files = glob.glob(os.path.join(base_dir, "astrology-reading/today/horoscope/*/collection.html"))
    
    # Fix the main horoscopes page first
    fix_main_horoscope_page()
    
    # Then fix individual collection pages
    fixed_count = 0
    for file in collection_files:
        if fix_header_images(file):
            fixed_count += 1
    
    print(f"\nSummary: Fixed header images in {fixed_count} zodiac collection files.")
    
    if fixed_count > 0:
        print("\nNext steps:")
        print("1. Refresh your browser (Cmd+Shift+R)")
        print("2. Check if zodiac header images now display correctly")
        print("3. Verify thumbnail images on the main horoscopes page")
    else:
        print("\nNo corrupted zodiac images found or fixes needed.")

if __name__ == "__main__":
    main() 