import os
from bs4 import BeautifulSoup
import time
import glob
import shutil

def find_zodiac_backups():
    """Find any zodiac image backups we may have created"""
    backup_dir = "/Users/seanivore/Development/astrofluenced/assets/downloaded/found_images"
    backup_files = {}
    
    if os.path.exists(backup_dir):
        for file in os.listdir(backup_dir):
            for sign in ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                         'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']:
                if sign in file.lower():
                    backup_files[sign] = os.path.join(backup_dir, file)
    
    return backup_files

def find_alternate_images():
    """Find any alternate zodiac images in the system"""
    base_dir = "/Users/seanivore/Development/astrofluenced/assets/downloaded"
    alternate_files = {}
    
    for sign in ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']:
        # Look for any image with the sign name
        pattern = os.path.join(base_dir, f"**/*{sign}*.webp")
        matches = glob.glob(pattern, recursive=True)
        
        if matches:
            # Use the first match that's not already in a 'found_images' directory
            for match in matches:
                if 'found_images' not in match:
                    alternate_files[sign] = match
                    break
    
    return alternate_files

def create_inline_svg_placeholders():
    """Create inline SVG placeholders for each zodiac sign"""
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
    
    svg_placeholders = {}
    
    for sign, color in colors.items():
        # Create data URI for inline SVG
        svg = f"""<svg xmlns='http://www.w3.org/2000/svg' width='600' height='400' viewBox='0 0 600 400'>
  <rect width='600' height='400' fill='{color}' opacity='0.7'/>
  <text x='50%' y='50%' dominant-baseline='middle' text-anchor='middle' font-family='Arial' font-size='40' fill='white'>{sign.title()}</text>
</svg>"""
        
        # Convert to data URI
        svg_uri = f"data:image/svg+xml;charset=utf-8,{svg}"
        svg_placeholders[sign] = svg_uri
    
    return svg_placeholders

def fix_homepage_zodiac_images(homepage_path):
    """Ensure all zodiac sign images are displayed on the homepage"""
    try:
        with open(homepage_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all horoscope collection items on the homepage
        horoscope_items = soup.select('.collection-item-13.homepage.horoscopes')
        
        # Find existing backup images
        backup_files = find_zodiac_backups()
        
        # Find alternate images
        alternate_files = find_alternate_images()
        
        # Create SVG placeholders
        svg_placeholders = create_inline_svg_placeholders()
        
        # Destination for copying files
        target_dir = "/Users/seanivore/Development/astrofluenced/assets/downloaded/zodiac_fixed"
        os.makedirs(target_dir, exist_ok=True)
        
        # Track fixed items
        fixed_count = 0
        current_signs = []
        
        for item in horoscope_items:
            # Find the zodiac sign name
            sign_text = item.select_one('.text.homepage.reverse')
            if not sign_text:
                continue
            
            sign = sign_text.text.strip().lower()
            if sign.endswith('\n'):
                sign = sign.split('\n')[0].strip().lower()
            
            current_signs.append(sign)
            
            # Find the image
            img_tag = item.select_one('img')
            if not img_tag:
                continue
            
            # Check if the image is missing or potentially broken
            src = img_tag.get('src', '')
            missing = src == '' or 'replacement_images' in src
            
            if missing or 'placeholder' in src:
                # Try to use a backup if available
                if sign in backup_files:
                    # Copy file to the fixed folder
                    filename = os.path.basename(backup_files[sign])
                    target_path = os.path.join(target_dir, filename)
                    shutil.copy(backup_files[sign], target_path)
                    
                    # Update src with cache-busting parameter
                    new_src = f"assets/downloaded/zodiac_fixed/{filename}?v={int(time.time())}"
                    img_tag['src'] = new_src
                    print(f"Updated {sign} image with backup: {new_src}")
                    fixed_count += 1
                
                # Try alternate image if no backup
                elif sign in alternate_files:
                    # Copy file to the fixed folder
                    filename = os.path.basename(alternate_files[sign])
                    target_path = os.path.join(target_dir, filename)
                    shutil.copy(alternate_files[sign], target_path)
                    
                    # Update src with cache-busting parameter
                    new_src = f"assets/downloaded/zodiac_fixed/{filename}?v={int(time.time())}"
                    img_tag['src'] = new_src
                    print(f"Updated {sign} image with alternate: {new_src}")
                    fixed_count += 1
                
                # Use SVG placeholder as last resort
                else:
                    img_tag['src'] = svg_placeholders[sign]
                    print(f"Updated {sign} image with SVG placeholder")
                    fixed_count += 1
        
        # Check for missing signs
        all_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                    'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
        
        missing_signs = [sign for sign in all_signs if sign not in current_signs]
        if missing_signs:
            print(f"Warning: These zodiac signs are not found on the homepage: {', '.join(missing_signs)}")
        
        if fixed_count > 0:
            # Save the modified file
            with open(homepage_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Successfully fixed {fixed_count} zodiac images on the homepage")
            return True
        else:
            print("No zodiac images needed to be fixed")
            return False
        
    except Exception as e:
        print(f"Error fixing homepage zodiac images: {e}")
        return False

def main():
    homepage_path = "/Users/seanivore/Development/astrofluenced/index.html"
    
    # Fix homepage zodiac images
    success = fix_homepage_zodiac_images(homepage_path)
    
    if success:
        print("\nNext steps:")
        print("1. Hard refresh your browser (Cmd+Shift+R)")
        print("2. Check that all zodiac signs now have images on the homepage")
        print("3. Note that some images may be placeholders if we couldn't find suitable replacements")
    else:
        print("\nNo changes were made to the homepage. All zodiac images may already be properly displayed.")

if __name__ == "__main__":
    main() 