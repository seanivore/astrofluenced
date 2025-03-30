import os
import glob
from bs4 import BeautifulSoup
import re

def enhance_chart_analysis_pages():
    """Add horoscope links to chart analysis pages"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    chart_dir = os.path.join(base_dir, "astrology-reading/significant-aspects")
    
    # Get all chart analysis files
    chart_files = glob.glob(os.path.join(chart_dir, "chart-analysis-*.html"))
    
    enhanced_count = 0
    
    for file_path in chart_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Check if we need to enhance this file
            if "Horoscope Collections" in content and "This content is updated weekly" in content:
                # Parse HTML
                soup = BeautifulSoup(content, 'html.parser')
                
                # Find the horoscope collections section
                horoscope_section = soup.find(string="Horoscope Collections")
                
                if horoscope_section:
                    # Find the parent containing the section
                    section_parent = horoscope_section.find_parent(['div', 'section'])
                    
                    if section_parent:
                        # Find the placeholder text
                        placeholder = section_parent.find(string="This content is updated weekly with new astrological insights.")
                        
                        if placeholder:
                            # Create horoscope links
                            horoscope_html = """
                            <div class="horoscope-links">
                                <div class="horoscope-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px;">
                                    <a href="../today/horoscope/aries/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(255, 87, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #FF5733;">Aries</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/taurus/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(51, 255, 87, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #33FF57;">Taurus</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/gemini/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(51, 87, 255, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #3357FF;">Gemini</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/cancer/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(255, 51, 245, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #FF33F5;">Cancer</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/leo/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(245, 255, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #F5FF33;">Leo</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/virgo/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(51, 255, 245, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #33FFF5;">Virgo</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/libra/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(245, 51, 255, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #F533FF;">Libra</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/scorpio/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(255, 51, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #FF3333;">Scorpio</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/sagittarius/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(51, 255, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #33FF33;">Sagittarius</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/capricorn/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(51, 51, 255, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #3333FF;">Capricorn</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/aquarius/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(255, 51, 128, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #FF3380;">Aquarius</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                    <a href="../today/horoscope/pisces/collection.html" class="horoscope-item" style="text-decoration: none; color: inherit; background: rgba(128, 255, 51, 0.2); padding: 15px; border-radius: 8px; text-align: center;">
                                        <h3 style="margin-top: 0; color: #80FF33;">Pisces</h3>
                                        <p>Daily horoscope and insights</p>
                                    </a>
                                </div>
                                <div class="view-all" style="text-align: center; margin-top: 20px;">
                                    <a href="../today/horoscopes.html" style="display: inline-block; padding: 10px 20px; background-color: #8dd9c0; color: #0e1e14; text-decoration: none; border-radius: 5px; font-weight: bold;">View All Horoscopes</a>
                                </div>
                            </div>
                            """
                            
                            # Replace the placeholder with the horoscope grid
                            horoscope_soup = BeautifulSoup(horoscope_html, 'html.parser')
                            placeholder.replace_with(horoscope_soup)
                            
                            # Save the changes
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(str(soup))
                            
                            print(f"Enhanced horoscopes in {os.path.basename(file_path)}")
                            enhanced_count += 1
        
        except Exception as e:
            print(f"Error enhancing {file_path}: {e}")
    
    return enhanced_count

def improve_read_more_sections():
    """Add links to 'Read More' sections with weekly chart analyses and improve-life blogs"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Get all HTML files
    html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)
    
    improved_count = 0
    
    for file_path in html_files:
        try:
            # Skip files we've already enhanced
            if "significant-aspects/index.html" in file_path:
                continue
                
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Check if this file has a "Read More" section
            if "Read More" not in content:
                continue
            
            # Parse HTML
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find all "Read More" headings
            read_more_headings = soup.find_all(string=re.compile("Read More"))
            
            changes_made = False
            
            for heading in read_more_headings:
                # Find the nearest parent section
                section = heading.find_parent(['div', 'section'])
                
                if section:
                    # Check the heading text to determine the type of content
                    heading_text = heading.string.strip()
                    
                    # Chart Analysis section
                    if "Chart" in heading_text or "Analysis" in heading_text:
                        # Find any empty lists or placeholders
                        empty_lists = section.select('.w-dyn-empty')
                        placeholders = section.find_all(string="This content is updated weekly with new astrological insights.")
                        
                        if empty_lists or placeholders:
                            # Create list of latest chart analyses
                            chart_html = """
                            <div class="latest-charts" style="margin-top: 15px;">
                                <h4 style="color: #8dd9c0; margin-bottom: 15px;">Latest Chart Analyses</h4>
                                <div class="chart-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px;">
                                    <a href="significant-aspects/chart-analysis-wednesday-10-25-2023.html" class="chart-item" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 15px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Wednesday 10/25</h5>
                                        <p>Planetary influences and aspects</p>
                                    </a>
                                    <a href="significant-aspects/chart-analysis-tuesday-10-24-2023.html" class="chart-item" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 15px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Tuesday 10/24</h5>
                                        <p>Planetary influences and aspects</p>
                                    </a>
                                    <a href="significant-aspects/chart-analysis-monday-10-23-2023.html" class="chart-item" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 15px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Monday 10/23</h5>
                                        <p>Planetary influences and aspects</p>
                                    </a>
                                </div>
                                <div class="view-all" style="text-align: center; margin-top: 20px;">
                                    <a href="significant-aspects/index.html" style="display: inline-block; padding: 10px 20px; background-color: #8dd9c0; color: #0e1e14; text-decoration: none; border-radius: 5px; font-weight: bold;">View All Chart Analyses</a>
                                </div>
                            </div>
                            """
                            
                            # Fix paths based on file location
                            if "astrology-reading/" in file_path:
                                chart_html = chart_html.replace('significant-aspects/', '../significant-aspects/')
                            
                            # Replace empty lists or add to section
                            chart_soup = BeautifulSoup(chart_html, 'html.parser')
                            
                            if empty_lists:
                                for empty_list in empty_lists:
                                    empty_list.replace_with(chart_soup)
                                    changes_made = True
                            elif placeholders:
                                for placeholder in placeholders:
                                    placeholder.replace_with(chart_soup)
                                    changes_made = True
                            else:
                                section.append(chart_soup)
                                changes_made = True
                    
                    # Improve Life section
                    elif "Improve" in heading_text or "Life" in heading_text:
                        # Find any empty lists or placeholders
                        empty_lists = section.select('.w-dyn-empty')
                        placeholders = section.find_all(string="This content is updated weekly with new astrological insights.")
                        
                        if empty_lists or placeholders:
                            # Create list of improve life articles
                            improve_html = """
                            <div class="improve-life-articles" style="margin-top: 15px;">
                                <h4 style="color: #8dd9c0; margin-bottom: 15px;">Personal Growth Articles</h4>
                                <div class="article-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px;">
                                    <a href="improve-life/growth-through-introspection.html" class="article-item" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 15px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Growth Through Introspection</h5>
                                        <p>Harness the power of self-reflection</p>
                                    </a>
                                    <a href="improve-life/change-your-outlook.html" class="article-item" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 15px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Change Your Outlook</h5>
                                        <p>Transform your perspective with astrology</p>
                                    </a>
                                    <a href="improve-life/internal-external-personal-growth.html" class="article-item" style="text-decoration: none; color: inherit; background: rgba(30, 60, 50, 0.5); padding: 15px; border-radius: 8px;">
                                        <h5 style="margin-top: 0; color: #8dd9c0;">Internal & External Growth</h5>
                                        <p>Balance inner and outer development</p>
                                    </a>
                                </div>
                            </div>
                            """
                            
                            # Fix paths based on file location
                            if "astrology-reading/" in file_path:
                                improve_html = improve_html.replace('improve-life/', '../improve-life/')
                            
                            # Replace empty lists or add to section
                            improve_soup = BeautifulSoup(improve_html, 'html.parser')
                            
                            if empty_lists:
                                for empty_list in empty_lists:
                                    empty_list.replace_with(improve_soup)
                                    changes_made = True
                            elif placeholders:
                                for placeholder in placeholders:
                                    placeholder.replace_with(improve_soup)
                                    changes_made = True
                            else:
                                section.append(improve_soup)
                                changes_made = True
                    
                    # Horoscopes section
                    elif "Horoscope" in heading_text:
                        # Find any empty lists or placeholders
                        empty_lists = section.select('.w-dyn-empty')
                        placeholders = section.find_all(string="This content is updated weekly with new astrological insights.")
                        
                        if empty_lists or placeholders:
                            # Create horoscope zodiac links
                            horoscope_html = """
                            <div class="horoscope-links" style="margin-top: 15px;">
                                <h4 style="color: #8dd9c0; margin-bottom: 15px;">Today's Horoscopes by Sign</h4>
                                <div class="sign-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 15px;">
                                    <a href="today/horoscope/aries/collection.html" class="sign-item" style="text-decoration: none; color: inherit; background: rgba(255, 87, 51, 0.2); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #FF5733;">Aries</h5>
                                    </a>
                                    <a href="today/horoscope/taurus/collection.html" class="sign-item" style="text-decoration: none; color: inherit; background: rgba(51, 255, 87, 0.2); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #33FF57;">Taurus</h5>
                                    </a>
                                    <a href="today/horoscope/gemini/collection.html" class="sign-item" style="text-decoration: none; color: inherit; background: rgba(51, 87, 255, 0.2); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #3357FF;">Gemini</h5>
                                    </a>
                                    <a href="today/horoscope/cancer/collection.html" class="sign-item" style="text-decoration: none; color: inherit; background: rgba(255, 51, 245, 0.2); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #FF33F5;">Cancer</h5>
                                    </a>
                                    <a href="today/horoscope/leo/collection.html" class="sign-item" style="text-decoration: none; color: inherit; background: rgba(245, 255, 51, 0.2); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #F5FF33;">Leo</h5>
                                    </a>
                                    <a href="today/horoscope/virgo/collection.html" class="sign-item" style="text-decoration: none; color: inherit; background: rgba(51, 255, 245, 0.2); padding: 12px; border-radius: 8px; text-align: center;">
                                        <h5 style="margin-top: 0; color: #33FFF5;">Virgo</h5>
                                    </a>
                                </div>
                                <div class="view-all" style="text-align: center; margin-top: 20px;">
                                    <a href="today/horoscopes.html" style="display: inline-block; padding: 10px 20px; background-color: #8dd9c0; color: #0e1e14; text-decoration: none; border-radius: 5px; font-weight: bold;">View All Horoscopes</a>
                                </div>
                            </div>
                            """
                            
                            # Fix paths based on file location
                            if "astrology-reading/" in file_path:
                                horoscope_html = horoscope_html.replace('today/', '../today/')
                            
                            # Replace empty lists or add to section
                            horoscope_soup = BeautifulSoup(horoscope_html, 'html.parser')
                            
                            if empty_lists:
                                for empty_list in empty_lists:
                                    empty_list.replace_with(horoscope_soup)
                                    changes_made = True
                            elif placeholders:
                                for placeholder in placeholders:
                                    placeholder.replace_with(horoscope_soup)
                                    changes_made = True
                            else:
                                section.append(horoscope_soup)
                                changes_made = True
            
            if changes_made:
                # Save the changes
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                
                print(f"Improved Read More sections in {os.path.basename(file_path)}")
                improved_count += 1
        
        except Exception as e:
            print(f"Error improving {file_path}: {e}")
    
    return improved_count

def main():
    # Enhance chart analysis pages with horoscope links
    enhanced_count = enhance_chart_analysis_pages()
    print(f"Enhanced {enhanced_count} chart analysis pages with horoscope links")
    
    # Improve "Read More" sections
    improved_count = improve_read_more_sections()
    print(f"Improved Read More sections in {improved_count} files")
    
    print("\nNext steps:")
    print("1. Refresh your browser (Cmd+Shift+R)")
    print("2. Check chart analysis pages for horoscope links")
    print("3. Verify that Read More sections now display properly")

if __name__ == "__main__":
    main() 