import os
import glob
from bs4 import BeautifulSoup
import re
import shutil

def fix_specific_horoscope_pages():
    """Fix specific horoscope sections with direct HTML insertion"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Target files in today and significant-aspects directories
    target_patterns = [
        os.path.join(base_dir, "astrology-reading/significant-aspects/*.html"),
        os.path.join(base_dir, "astrology-reading/today/*.html"),
        os.path.join(base_dir, "*.html")  # Root HTML files
    ]
    
    total_fixed = 0
    
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
                
                # 1. Look for "Horoscope Collections" or similar headings
                horoscope_headings = soup.find_all(string=re.compile("Horoscope", re.IGNORECASE))
                for heading in horoscope_headings:
                    parent_div = heading.find_parent('div')
                    if parent_div:
                        # Look for empty placeholders or containers that need content
                        placeholders = parent_div.find_all(string=re.compile("This content is updated", re.IGNORECASE))
                        empty_divs = parent_div.select('.w-dyn-empty')
                        
                        if placeholders or empty_divs:
                            # Create simplified horoscope grid - use proper relative paths
                            relative_path = "../today/" if "significant-aspects" in file_path else "today/"
                            if "astrology-reading" not in file_path and "index.html" in file_path:
                                relative_path = "astrology-reading/today/"
                            
                            horoscope_html = f"""
                            <div class="horoscope-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 15px; margin-top: 20px;">
                                <a href="{relative_path}horoscope/aries/collection.html" style="text-decoration: none; color: inherit; background: rgba(255, 87, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                    <h3 style="margin-top: 0; color: #FF5733;">Aries</h3>
                                </a>
                                <a href="{relative_path}horoscope/taurus/collection.html" style="text-decoration: none; color: inherit; background: rgba(51, 255, 87, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                    <h3 style="margin-top: 0; color: #33FF57;">Taurus</h3>
                                </a>
                                <a href="{relative_path}horoscope/gemini/collection.html" style="text-decoration: none; color: inherit; background: rgba(51, 87, 255, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                    <h3 style="margin-top: 0; color: #3357FF;">Gemini</h3>
                                </a>
                                <a href="{relative_path}horoscope/leo/collection.html" style="text-decoration: none; color: inherit; background: rgba(245, 255, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                    <h3 style="margin-top: 0; color: #F5FF33;">Leo</h3>
                                </a>
                                <a href="{relative_path}horoscope/sagittarius/collection.html" style="text-decoration: none; color: inherit; background: rgba(51, 255, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                    <h3 style="margin-top: 0; color: #33FF33;">Sagittarius</h3>
                                </a>
                                <a href="{relative_path}horoscope/pisces/collection.html" style="text-decoration: none; color: inherit; background: rgba(128, 255, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                    <h3 style="margin-top: 0; color: #80FF33;">Pisces</h3>
                                </a>
                            </div>
                            <div style="text-align: center; margin-top: 20px;">
                                <a href="{relative_path}horoscopes.html" style="display: inline-block; padding: 10px 20px; background-color: #8dd9c0; color: #0e1e14; text-decoration: none; border-radius: 5px; font-weight: bold;">View All Horoscopes</a>
                            </div>
                            """
                            
                            # Replace placeholders or empty divs
                            if placeholders:
                                for placeholder in placeholders:
                                    # Create a new div to hold our content
                                    new_content = BeautifulSoup(horoscope_html, 'html.parser')
                                    placeholder.replace_with(new_content)
                                    changes_made = True
                            
                            if empty_divs:
                                for empty_div in empty_divs:
                                    # Replace empty div with our content
                                    new_content = BeautifulSoup(horoscope_html, 'html.parser')
                                    empty_div.replace_with(new_content)
                                    changes_made = True
                
                # 2. Fix "Read More" sections - specifically for Chart Analysis and Improve Life
                read_more_sections = soup.find_all(string=re.compile("Read More", re.IGNORECASE))
                for section in read_more_sections:
                    parent = section.find_parent('div')
                    if parent:
                        # Determine section type based on context
                        if "Chart" in str(parent) or "Analysis" in str(parent):
                            # Fix path based on location
                            if "astrology-reading" in file_path:
                                chart_path = "../significant-aspects/"
                            else:
                                chart_path = "astrology-reading/significant-aspects/"
                            
                            # Add Chart Analysis links
                            chart_html = f"""
                            <div style="margin-top: 15px;">
                                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 15px;">
                                    <a href="{chart_path}chart-analysis-friday-10-20-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Friday 10/20</h5>
                                        <p>Planetary influences and aspects</p>
                                    </a>
                                    <a href="{chart_path}chart-analysis-thursday-10-19-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Thursday 10/19</h5>
                                        <p>Planetary influences and aspects</p>
                                    </a>
                                    <a href="{chart_path}chart-analysis-wednesday-10-18-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Wednesday 10/18</h5>
                                        <p>Planetary influences and aspects</p>
                                    </a>
                                </div>
                                <div style="text-align: center; margin-top: 20px;">
                                    <a href="{chart_path}index.html" style="display: inline-block; padding: 10px 20px; background-color: #8dd9c0; color: #0e1e14; text-decoration: none; border-radius: 5px; font-weight: bold;">View All Chart Analyses</a>
                                </div>
                            </div>
                            """
                            
                            # Find empty containers
                            empty_containers = parent.select('.w-dyn-empty')
                            if empty_containers:
                                for container in empty_containers:
                                    new_content = BeautifulSoup(chart_html, 'html.parser')
                                    container.replace_with(new_content)
                                    changes_made = True
                            else:
                                # Add after the heading as a sibling
                                chart_soup = BeautifulSoup(chart_html, 'html.parser')
                                section.parent.append(chart_soup)
                                changes_made = True
                        
                        # Improve Life section
                        elif "Improve" in str(parent) or "Life" in str(parent):
                            # Fix path based on location
                            if "astrology-reading" in file_path:
                                improve_path = "../improve-life/"
                            else:
                                improve_path = "astrology-reading/improve-life/"
                            
                            # Add Improve Life links
                            improve_html = f"""
                            <div style="margin-top: 15px;">
                                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 15px;">
                                    <a href="{improve_path}growth-through-introspection.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Growth Through Introspection</h5>
                                        <p>Harness the power of self-reflection</p>
                                    </a>
                                    <a href="{improve_path}change-your-outlook.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Change Your Outlook</h5>
                                        <p>Transform your perspective with astrology</p>
                                    </a>
                                    <a href="{improve_path}internal-external-personal-growth.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Internal & External Growth</h5>
                                        <p>Balance inner and outer development</p>
                                    </a>
                                </div>
                            </div>
                            """
                            
                            # Find empty containers
                            empty_containers = parent.select('.w-dyn-empty')
                            if empty_containers:
                                for container in empty_containers:
                                    new_content = BeautifulSoup(improve_html, 'html.parser')
                                    container.replace_with(new_content)
                                    changes_made = True
                            else:
                                # Add after the heading as a sibling
                                improve_soup = BeautifulSoup(improve_html, 'html.parser')
                                section.parent.append(improve_soup)
                                changes_made = True
                
                # 3. Fix the "This Week's Readings" section seen in the second screenshot
                week_headings = soup.find_all(string=re.compile("Full Week|Week's Reading", re.IGNORECASE))
                for heading in week_headings:
                    # Find the parent section
                    parent_section = heading.find_parent('div')
                    if parent_section:
                        # Check for placeholders
                        placeholders = parent_section.find_all(string=re.compile("This content is updated", re.IGNORECASE))
                        if placeholders:
                            # Prepare path prefix based on file location
                            if "astrology-reading" in file_path:
                                path_prefix = "../significant-aspects/"
                            else:
                                path_prefix = "astrology-reading/significant-aspects/"
                                
                            weekly_html = f"""
                            <div style="margin-top: 20px;">
                                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px;">
                                    <a href="{path_prefix}chart-analysis-monday-10-16-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Monday 10/16</h5>
                                    </a>
                                    <a href="{path_prefix}chart-analysis-tuesday-10-17-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Tuesday 10/17</h5>
                                    </a>
                                    <a href="{path_prefix}chart-analysis-wednesday-10-18-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Wednesday 10/18</h5>
                                    </a>
                                    <a href="{path_prefix}chart-analysis-thursday-10-19-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Thursday 10/19</h5>
                                    </a>
                                    <a href="{path_prefix}chart-analysis-friday-10-20-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Friday 10/20</h5>
                                    </a>
                                    <a href="{path_prefix}chart-analysis-saturday-10-21-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Saturday 10/21</h5>
                                    </a>
                                    <a href="{path_prefix}chart-analysis-sunday-10-22-2023.html" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Sunday 10/22</h5>
                                    </a>
                                </div>
                            </div>
                            """
                            
                            for placeholder in placeholders:
                                new_content = BeautifulSoup(weekly_html, 'html.parser')
                                placeholder.replace_with(new_content)
                                changes_made = True
                
                # Save changes if any were made
                if changes_made:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(str(soup))
                    print(f"✅ Fixed content in {os.path.basename(file_path)}")
                    total_fixed += 1
                else:
                    # Restore from backup if no changes
                    os.remove(backup_path)
            
            except Exception as e:
                # Restore from backup on error
                if os.path.exists(backup_path):
                    shutil.copy2(backup_path, file_path)
                    os.remove(backup_path)
                print(f"❌ Error processing {os.path.basename(file_path)}: {e}")
    
    return total_fixed

def main():
    print("🔍 Fixing specific horoscope and Read More sections...")
    fixed_count = fix_specific_horoscope_pages()
    
    print(f"\n✨ Successfully fixed {fixed_count} files.")
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. Check if horoscopes and Read More sections are now properly visible")

if __name__ == "__main__":
    main() 