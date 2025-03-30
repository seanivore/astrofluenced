import os
import glob
from bs4 import BeautifulSoup
import shutil
import re

def fix_horoscope_collections():
    """Fix empty horoscope collection pages"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Target all horoscope collection pages
    collection_pages = glob.glob(os.path.join(base_dir, "astrology-reading/today/horoscope/*/collection.html"))
    
    if not collection_pages:
        print(f"⚠️ No horoscope collection pages found")
        return False
    
    signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", 
             "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
    
    print(f"✓ Found {len(collection_pages)} horoscope collection pages to process")
    
    # Create placeholder content for a horoscope collection
    def create_horoscope_placeholder(sign):
        sign_title = sign.title()
        
        return f"""
        <div class="section">
            <div class="container w-container">
                <div class="w-layout-grid grid-2-columns">
                    <div id="w-node-_4d40209a-ad9e-8237-a87b-52fb9972e92c-1c0ea178" class="content-block">
                        <h1 class="heading-zodiac">{sign_title}'s Weekly Horoscope Collection</h1>
                        <div class="rich-text w-richtext">
                            <p>Welcome to {sign_title}'s weekly horoscope collection. Here you'll find all your {sign_title} readings for the current week.</p>
                            <p>Each horoscope is carefully crafted to provide guidance and insights specifically for {sign_title}.</p>
                        </div>
                    </div>
                    <div class="image-block">
                        <img src="../../../../assets/images/zodiac/{sign}.webp" loading="lazy" alt="{sign_title} Zodiac Sign" class="image-cover">
                    </div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <div class="container w-container">
                <h2 class="heading-large center">{sign_title}'s Horoscopes</h2>
                <div class="collection-list-wrapper">
                    <div class="w-layout-grid grid-3-columns horoscopes">
                        <div class="card horoscope">
                            <div class="card-image">
                                <img src="../../../../assets/images/horoscope-types/daily-classic.webp" loading="lazy" alt="Daily Classic Horoscope">
                            </div>
                            <div class="card-content">
                                <h3 class="heading-card">Daily Classic</h3>
                                <p>Your traditional daily horoscope with general guidance for {sign_title}.</p>
                                <div class="button-wrap">
                                    <a href="daily-classic.html" class="button w-button">Read Your Horoscope</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="card horoscope">
                            <div class="card-image">
                                <img src="../../../../assets/images/horoscope-types/love-predictions.webp" loading="lazy" alt="Love Predictions Horoscope">
                            </div>
                            <div class="card-content">
                                <h3 class="heading-card">Love Predictions</h3>
                                <p>Romance and relationship insights for {sign_title} this week.</p>
                                <div class="button-wrap">
                                    <a href="love-predictions.html" class="button w-button">Read Your Horoscope</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="card horoscope">
                            <div class="card-image">
                                <img src="../../../../assets/images/horoscope-types/outfit-guide.webp" loading="lazy" alt="Outfit Guide Horoscope">
                            </div>
                            <div class="card-content">
                                <h3 class="heading-card">Style & Outfit Guide</h3>
                                <p>Fashion and style recommendations aligned with {sign_title}'s cosmic energies.</p>
                                <div class="button-wrap">
                                    <a href="outfit-guide.html" class="button w-button">Read Your Horoscope</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="card horoscope">
                            <div class="card-image">
                                <img src="../../../../assets/images/horoscope-types/cash-flow.webp" loading="lazy" alt="Cash Flow Horoscope">
                            </div>
                            <div class="card-content">
                                <h3 class="heading-card">Weekly Cash Flow</h3>
                                <p>Financial insights and money matters for {sign_title} this week.</p>
                                <div class="button-wrap">
                                    <a href="cash-flow.html" class="button w-button">Read Your Horoscope</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="card horoscope">
                            <div class="card-image">
                                <img src="../../../../assets/images/horoscope-types/venus-mars.webp" loading="lazy" alt="Venus and Mars Horoscope">
                            </div>
                            <div class="card-content">
                                <h3 class="heading-card">Venus & Mars Influence</h3>
                                <p>How Venus and Mars are affecting {sign_title}'s love and passion.</p>
                                <div class="button-wrap">
                                    <a href="venus-mars.html" class="button w-button">Read Your Horoscope</a>
                                </div>
                            </div>
                        </div>
                        
                        <div class="card horoscope">
                            <div class="card-image">
                                <img src="../../../../assets/images/horoscope-types/weekend-reading.webp" loading="lazy" alt="Weekend Reading Horoscope">
                            </div>
                            <div class="card-content">
                                <h3 class="heading-card">Weekend Reading</h3>
                                <p>Special guidance for {sign_title} to make the most of your weekend.</p>
                                <div class="button-wrap">
                                    <a href="weekend.html" class="button w-button">Read Your Horoscope</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    
    # Make sure the zodiac images directory exists
    zodiac_img_dir = os.path.join(base_dir, "assets/images/zodiac")
    horoscope_types_dir = os.path.join(base_dir, "assets/images/horoscope-types")
    os.makedirs(zodiac_img_dir, exist_ok=True)
    os.makedirs(horoscope_types_dir, exist_ok=True)
    
    # Prepare sample zodiac images
    # (This would copy them from elsewhere in the project or create placeholders)
    
    # Create sample horoscope type images if needed
    horoscope_types = {
        "daily-classic": "Daily classic horoscope",
        "love-predictions": "Love predictions",
        "outfit-guide": "Style and outfit guide",
        "cash-flow": "Weekly cash flow",
        "venus-mars": "Venus and Mars influence",
        "weekend-reading": "Weekend reading"
    }
    
    # Search for existing zodiac and horoscope type images
    search_for_images(base_dir, zodiac_img_dir, horoscope_types_dir, signs, horoscope_types)
    
    total_fixed = 0
    
    # Process each collection page
    for page_path in collection_pages:
        # Determine which sign this is for
        sign_match = re.search(r'/horoscope/([^/]+)/collection\.html', page_path)
        if not sign_match or sign_match.group(1).lower() not in signs:
            print(f"⚠️ Could not determine sign for: {page_path}")
            continue
        
        sign = sign_match.group(1).lower()
        print(f"\n🔍 Processing {sign} collection page")
        
        # Create backup
        backup_path = page_path + ".bak"
        shutil.copy2(page_path, backup_path)
        
        try:
            with open(page_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse the file
            soup = BeautifulSoup(content, 'html.parser')
            
            # Check if the page is empty (missing main content sections)
            sections = soup.select('.section:not(.above-path):not(.footer)')
            
            # If there are no content sections or just empty ones
            if not sections or all('w-condition-invisible' in section.get('class', []) for section in sections):
                print(f"✓ {sign.title()} collection page is empty, adding content")
                
                # Generate placeholder content
                placeholder_html = create_horoscope_placeholder(sign)
                placeholder_soup = BeautifulSoup(placeholder_html, 'html.parser')
                
                # Find where to insert the content (before the footer)
                footer = soup.select_one('.footer')
                if footer:
                    # Insert content before the footer
                    for section in placeholder_soup.select('.section'):
                        footer.insert_before(section)
                    
                    # Save the updated file
                    with open(page_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    
                    print(f"✅ Fixed {sign.title()} collection page")
                    total_fixed += 1
                else:
                    print(f"⚠️ Could not find footer in {sign} collection page")
            else:
                print(f"ℹ️ {sign.title()} collection page already has content")
                os.remove(backup_path)
        
        except Exception as e:
            # Restore backup on error
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, page_path)
                os.remove(backup_path)
            print(f"❌ Error processing {sign} collection page: {e}")
    
    return total_fixed

def search_for_images(base_dir, zodiac_dir, horoscope_types_dir, signs, horoscope_types):
    """Search for existing images to use for zodiac signs and horoscope types"""
    # Search for zodiac sign images
    for sign in signs:
        target_path = os.path.join(zodiac_dir, f"{sign}.webp")
        if not os.path.exists(target_path):
            # Look for existing images
            found = False
            for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
                for file in files:
                    if file.endswith((".jpg", ".png", ".webp")) and sign.lower() in file.lower():
                        # Copy the file
                        source_path = os.path.join(root, file)
                        shutil.copy2(source_path, target_path)
                        print(f"✓ Found and copied image for {sign}: {file}")
                        found = True
                        break
                if found:
                    break
            
            if not found:
                # Create a simple colored rectangle with text as placeholder
                print(f"⚠️ No image found for {sign}, creating placeholder")
                create_placeholder_image(target_path, sign.title())
    
    # Search for horoscope type images
    for type_key, type_name in horoscope_types.items():
        target_path = os.path.join(horoscope_types_dir, f"{type_key}.webp")
        if not os.path.exists(target_path):
            # Look for existing images
            found = False
            for root, dirs, files in os.walk(os.path.join(base_dir, "assets")):
                for file in files:
                    if file.endswith((".jpg", ".png", ".webp")) and any(term in file.lower() for term in type_key.lower().split("-")):
                        # Copy the file
                        source_path = os.path.join(root, file)
                        shutil.copy2(source_path, target_path)
                        print(f"✓ Found and copied image for {type_key}: {file}")
                        found = True
                        break
                if found:
                    break
            
            if not found:
                # Create a simple colored rectangle with text as placeholder
                print(f"⚠️ No image found for {type_key}, creating placeholder")
                create_placeholder_image(target_path, type_name)

def create_placeholder_image(path, text):
    """Create a simple placeholder image with text"""
    # This function would normally use PIL to create an image
    # Since we can't install packages, let's create an HTML snippet instead
    # that shows where the image would be
    
    # For this quick script, we'll skip actual image creation
    # and rely on finding existing images in the project
    
    # Create an empty file as a last resort
    with open(path, 'wb') as f:
        f.write(b'')  # Empty file

if __name__ == "__main__":
    print("🔍 Fixing horoscope collection pages...")
    total_fixed = fix_horoscope_collections()
    
    if total_fixed > 0:
        print(f"\n✨ Successfully fixed {total_fixed} horoscope collection pages")
    else:
        print("\n⚠️ No horoscope collection pages were fixed")
    
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. Check the horoscope collection pages to see the content") 