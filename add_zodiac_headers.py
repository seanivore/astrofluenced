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

def create_header_html(sign):
    """Create HTML for a header section with a zodiac sign image"""
    svg_uri = create_svg_zodiac_image(sign)
    
    header_html = f"""
    <div class="zodiac-header-section" style="width: 100%; padding: 20px 0; margin-bottom: 20px; text-align: center;">
        <img src="{svg_uri}" alt="{sign.title()} Horoscope" style="max-width: 100%; height: auto; margin-bottom: 20px;">
        <h1 style="font-size: 2.5em; font-weight: bold; margin-bottom: 10px; color: white;">{sign.title()} Horoscope</h1>
        <p style="font-size: 1.2em; color: #d0d0d0;">Weekly horoscope and personalized astrological insights</p>
    </div>
    """
    
    return header_html

def add_header_to_collection(file_path):
    """Add a header section to a zodiac collection page"""
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
        
        # Check if we already added a header
        if soup.select('.zodiac-header-section'):
            print(f"Header already exists in {file_path}")
            return False
        
        # Create the header HTML
        header_html = create_header_html(current_sign)
        header_soup = BeautifulSoup(header_html, 'html.parser')
        
        # Insert the header at the beginning of the body
        body = soup.find('body')
        if body:
            # If there's a main content div, insert before that
            main_content = body.select_one('main, .main-content, .content-wrapper, .container')
            
            if main_content:
                main_content.insert(0, header_soup)
            else:
                # Otherwise, insert at beginning of body
                body.insert(0, header_soup)
            
            print(f"Added header to {file_path}")
            
            # Save the modified file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def enhance_main_horoscope_page():
    """Enhance the main horoscopes page with better thumbnails"""
    try:
        file_path = "/Users/seanivore/Development/astrofluenced/astrology-reading/today/horoscopes.html"
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check if custom title already exists
        if soup.select('.custom-horoscopes-title'):
            print("Main horoscope page already enhanced")
            return False
        
        # Add custom title
        title_html = """
        <div class="custom-horoscopes-title" style="width: 100%; text-align: center; margin: 40px 0;">
            <h1 style="font-size: 3em; font-weight: bold; color: white;">Today's Horoscopes</h1>
            <p style="font-size: 1.5em; color: #d0d0d0;">Choose your zodiac sign below to read your personalized horoscope</p>
        </div>
        """
        
        title_soup = BeautifulSoup(title_html, 'html.parser')
        
        # Insert at the beginning of main content
        main_content = soup.select_one('main, .main-content, .content-wrapper, .container')
        if main_content:
            main_content.insert(0, title_soup)
        else:
            # Fallback to body
            body = soup.find('body')
            if body:
                body.insert(0, title_soup)
        
        # Find all collection items for zodiac signs
        collection_items = soup.select('.collection-item, .w-dyn-item, .w-col')
        enhanced_items = 0
        
        for item in collection_items:
            # Find if this item contains a zodiac sign name
            text = item.get_text().lower()
            
            for sign in ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 
                        'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']:
                if sign in text:
                    # Find the image or create a container for one
                    img = item.find('img')
                    
                    if not img:
                        # Create a new image element
                        img_html = f'<img src="{create_svg_zodiac_image(sign)}" alt="{sign.title()}" style="width: 100%; height: auto; border-radius: 8px;">'
                        img_soup = BeautifulSoup(img_html, 'html.parser')
                        
                        # Insert it at the beginning of the item
                        item.insert(0, img_soup)
                    else:
                        # Replace the image source
                        img['src'] = create_svg_zodiac_image(sign)
                        img['style'] = "width: 100%; height: auto; border-radius: 8px;"
                    
                    # Add better styling to the entire item
                    item['style'] = "padding: 15px; margin-bottom: 20px; transition: transform 0.2s; cursor: pointer;"
                    
                    # Add hover effect with JavaScript
                    hover_script = soup.new_tag('script')
                    hover_script.string = f"""
                    document.addEventListener('DOMContentLoaded', function() {{
                        var item = document.currentScript.parentElement;
                        item.addEventListener('mouseenter', function() {{
                            this.style.transform = 'scale(1.05)';
                        }});
                        item.addEventListener('mouseleave', function() {{
                            this.style.transform = 'scale(1)';
                        }});
                    }});
                    """
                    item.append(hover_script)
                    
                    enhanced_items += 1
                    break
        
        if enhanced_items > 0:
            print(f"Enhanced {enhanced_items} zodiac items on main horoscope page")
            
            # Save the modified file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            return True
        
        return False
    
    except Exception as e:
        print(f"Error enhancing main horoscope page: {e}")
        return False

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Enhance the main horoscopes page
    enhance_main_horoscope_page()
    
    # Process all collection pages
    collection_files = glob.glob(os.path.join(base_dir, "astrology-reading/today/horoscope/*/collection.html"))
    
    headers_added = 0
    for file in collection_files:
        if add_header_to_collection(file):
            headers_added += 1
    
    print(f"\nSummary: Added headers to {headers_added} zodiac collection pages")
    
    if headers_added > 0:
        print("\nNext steps:")
        print("1. Refresh your browser (Cmd+Shift+R)")
        print("2. Check if zodiac collection pages now have proper headers")
        print("3. Verify the enhanced main horoscopes page looks good")
    else:
        print("\nNo changes were needed or all pages already had headers.")

if __name__ == "__main__":
    main() 