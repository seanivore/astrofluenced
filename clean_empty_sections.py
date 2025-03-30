import os
import glob
from bs4 import BeautifulSoup
import re
import shutil

def clean_empty_sections():
    """Remove empty horoscope and other placeholder sections from chart analysis and daily reading pages"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Target files in significant-aspects directory AND daily reading pages
    target_patterns = [
        os.path.join(base_dir, "astrology-reading/significant-aspects/*.html"),
        os.path.join(base_dir, "astrology-reading/today/*.html"),
        os.path.join(base_dir, "astrology-reading/today/horoscope/*/*.html")
    ]
    
    total_cleaned = 0
    
    # Process each pattern
    for pattern in target_patterns:
        files = glob.glob(pattern)
        
        for file_path in files:
            try:
                print(f"Checking {os.path.basename(file_path)}...")
                
                # Create backup
                backup_path = file_path + ".bak"
                shutil.copy2(file_path, backup_path)
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Parse the file
                soup = BeautifulSoup(content, 'html.parser')
                
                changes_made = False
                
                # 1. AGGRESSIVELY Remove ALL Horoscope Collections sections
                horoscope_sections = []
                
                # Find by heading text
                for text in ["Horoscope Collections", "Horoscope", "Collections"]:
                    headings = soup.find_all(string=re.compile(text, re.IGNORECASE))
                    for heading in headings:
                        # Get all parent divs and sections to find the outer container
                        for parent in heading.parents:
                            if parent.name in ['section', 'div'] and parent not in horoscope_sections:
                                # Check if this is likely a main section
                                if parent.get('class') and ('section' in ' '.join(parent.get('class')) or 'container' in ' '.join(parent.get('class'))):
                                    horoscope_sections.append(parent)
                
                # Remove all identified horoscope sections
                for section in horoscope_sections:
                    section.decompose()
                    changes_made = True
                    print(f"  - Removed Horoscope section")
                
                # 2. AGGRESSIVELY Remove Astro-Planning sections
                astro_sections = []
                
                # Find by heading text
                for text in ["Astro-Planning", "Plan the week", "Astro Planning"]:
                    headings = soup.find_all(string=re.compile(text, re.IGNORECASE))
                    for heading in headings:
                        # Get all parent divs and sections to find the outer container
                        for parent in heading.parents:
                            if parent.name in ['section', 'div'] and parent not in astro_sections:
                                # Check if this is likely a main section
                                if parent.get('class') and ('section' in ' '.join(parent.get('class')) or 'container' in ' '.join(parent.get('class'))):
                                    astro_sections.append(parent)
                
                # Remove all identified astro-planning sections
                for section in astro_sections:
                    section.decompose()
                    changes_made = True
                    print(f"  - Removed Astro-Planning section")
                
                # 3. Remove all "This content is updated weekly" placeholders and their container sections
                placeholder_sections = []
                placeholders = soup.find_all(string=re.compile("This content is updated weekly", re.IGNORECASE))
                for placeholder in placeholders:
                    # Find the largest container that makes sense to remove
                    for parent in placeholder.parents:
                        if parent.name in ['div', 'section'] and 'class' in parent.attrs:
                            parent_classes = ' '.join(parent.get('class', []))
                            # Look for meaningful container classes
                            if ('section' in parent_classes or 'container' in parent_classes) and parent not in placeholder_sections:
                                placeholder_sections.append(parent)
                                break
                
                # Remove all identified placeholder sections
                for section in placeholder_sections:
                    section.decompose()
                    changes_made = True
                    print(f"  - Removed placeholder section")
                
                # 4. Remove any empty .w-dyn-empty containers completely
                empty_containers = soup.select('.w-dyn-empty')
                for container in empty_containers:
                    # Find the largest parent that should be removed
                    for parent in container.parents:
                        if parent.name in ['div', 'section'] and 'class' in parent.attrs:
                            parent_classes = ' '.join(parent.get('class', []))
                            if 'section' in parent_classes or 'container' in parent_classes:
                                parent.decompose()
                                changes_made = True
                                print(f"  - Removed empty dynamic container and its section")
                                break
                    else:
                        # If no suitable parent found, remove the container itself
                        container.decompose()
                        changes_made = True
                        print(f"  - Removed empty dynamic container")
                
                # 5. Remove rainbow lottie separators
                lottie_divs = soup.find_all('div', class_=lambda c: c and ('lottie' in c.lower() if c else False))
                for lottie in lottie_divs:
                    # Remove most lottie elements as they're likely decorative
                    if not ('hero' in str(lottie).lower() or 'header' in str(lottie).lower()):
                        lottie.decompose()
                        changes_made = True
                        print(f"  - Removed lottie animation")
                
                # 6. DIRECTLY target elements in daily reading pages by looking for specific CSS classes
                # Target the specific section with the horoscope collections
                if "today" in file_path or "significant-aspects" in file_path:
                    # Look for sections with classes that typically contain the horoscope collections
                    sections_to_check = soup.find_all(['section', 'div'], class_=lambda c: c and any(x in ' '.join(c) for x in ['horoscope', 'collection', 'astro-planning']))
                    for section in sections_to_check:
                        section.decompose()
                        changes_made = True
                        print(f"  - Removed section by class match")
                
                # Save changes if any were made
                if changes_made:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    print(f"✅ Cleaned {os.path.basename(file_path)}")
                    total_cleaned += 1
                else:
                    # Restore from backup if no changes
                    os.remove(backup_path)
            
            except Exception as e:
                # Restore from backup on error
                if os.path.exists(backup_path):
                    shutil.copy2(backup_path, file_path)
                    os.remove(backup_path)
                print(f"❌ Error processing {os.path.basename(file_path)}: {e}")
    
    return total_cleaned

def clean_specific_chart_page():
    """Clean the specific chart analysis page shown in screenshots"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Target specifically the page in the screenshot
    target_files = [
        os.path.join(base_dir, "astrology-reading/significant-aspects/chart-analysis-wednesday-10-18-2023.html")
    ]
    
    cleaned = False
    
    for file_path in target_files:
        if not os.path.exists(file_path):
            print(f"⚠️ File not found: {file_path}")
            continue
            
        try:
            print(f"🎯 Directly targeting {os.path.basename(file_path)}...")
            
            # Create backup
            backup_path = file_path + ".bak"
            shutil.copy2(file_path, backup_path)
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse the file
            soup = BeautifulSoup(content, 'html.parser')
            
            changes_made = False
            
            # VERY SPECIFIC TARGETING: Find and remove Astro-Planning and Horoscope Collections sections
            sections_to_remove = []
            
            # 1. Find all h2 tags that might contain these headings
            for h_tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'div']):
                h_text = h_tag.get_text().strip()
                if "Horoscope Collections" in h_text or "Astro-Planning" in h_text:
                    # Find the parent section
                    for parent in h_tag.parents:
                        if parent.name in ['section', 'div'] and parent not in sections_to_remove:
                            if parent.get('class') and ('section' in ' '.join(parent.get('class', [])) or 'container' in ' '.join(parent.get('class', []))):
                                sections_to_remove.append(parent)
                                print(f"  - Found section with '{h_text}'")
                                break
            
            # 2. Remove these specific sections
            for section in sections_to_remove:
                section.decompose()
                changes_made = True
                print(f"  - Directly removed specific section")
            
            # 3. Remove all "This content is updated weekly" elements
            for placeholder in soup.find_all(string=re.compile("This content is updated weekly", re.IGNORECASE)):
                # Find a suitable parent to remove
                for parent in placeholder.parents:
                    if parent.name in ['div', 'section'] and not any('navbar' in c for c in parent.get('class', [])):
                        parent.decompose()
                        changes_made = True
                        print(f"  - Directly removed placeholder text and container")
                        break
            
            # 4. Save the changes
            if changes_made:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"✅ Successfully cleaned specific page")
                cleaned = True
            else:
                # Restore from backup if no changes
                os.remove(backup_path)
                print("❌ No changes needed for specific page")
                
        except Exception as e:
            # Restore from backup on error
            if os.path.exists(backup_path):
                shutil.copy2(backup_path, file_path)
                os.remove(backup_path)
            print(f"❌ Error processing specific page: {e}")
    
    return cleaned

def main():
    print("🧹 Cleaning up empty sections from chart analysis and daily reading pages...")
    
    # First try very specific targeting for the page in the screenshot
    specific_cleaned = clean_specific_chart_page()
    if specific_cleaned:
        print("✅ Successfully cleaned the specific chart page from screenshots")
    
    # Then clean all other pages
    cleaned_count = clean_empty_sections()
    
    print(f"\n✨ Successfully cleaned {cleaned_count} files.")
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. Check chart analysis pages - they should be cleaner without empty sections")

if __name__ == "__main__":
    main() 