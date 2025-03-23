import os
import glob
from bs4 import BeautifulSoup
import re
import shutil

def get_chart_analysis_links():
    """Get all chart analysis links from the significant-aspects directory"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    links_path = os.path.join(base_dir, "astrology-reading/significant-aspects")
    
    links = []
    
    # Find all chart analysis HTML files
    chart_files = glob.glob(os.path.join(links_path, "chart-analysis-*.html"))
    
    for file in chart_files:
        # Extract just the filename from the path
        filename = os.path.basename(file)
        # Convert to relative path
        relative_path = f"../significant-aspects/{filename}"
        
        # Extract date from filename for display
        match = re.search(r'chart-analysis-([a-z]+)-(\d{2}-\d{2}-\d{4})', filename)
        if match:
            day_name = match.group(1).capitalize()
            date_str = match.group(2).replace('-', '/')
            display_text = f"{day_name} {date_str}"
            
            links.append({
                'href': relative_path,
                'text': display_text
            })
    
    # Sort links by date (newer first)
    links.sort(reverse=True, key=lambda x: x['text'])
    return links

def get_chart_links_html():
    """Create HTML for chart analysis links"""
    links = get_chart_analysis_links()
    
    html = '<div class="w-dyn-items chart-links-wrapper">\n'
    
    for link in links:
        html += f'  <div class="w-dyn-item">\n'
        html += f'    <a href="{link["href"]}" class="chart-link w-inline-block">\n'
        html += f'      <div class="chart-link-text">{link["text"]}</div>\n'
        html += f'    </a>\n'
        html += f'  </div>\n'
    
    html += '</div>'
    
    return html

def fix_cms_placeholders(file_path):
    """Replace CMS placeholders with actual content"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find CMS placeholders
        cms_placeholders = soup.find_all(string=re.compile("Your personalized reading will appear here when connected"))
        
        if not cms_placeholders:
            return False
        
        fixes_applied = 0
        
        # Get chart links HTML
        chart_links_html = get_chart_links_html()
        chart_links_soup = BeautifulSoup(chart_links_html, 'html.parser')
        
        # Sample content for chart analysis
        chart_content = """
        <div class="daily-chart-content">
            <h3>Daily Astrological Influences</h3>
            <p>The planets continue their cosmic dance, creating unique energies each day. 
            Below are links to daily chart analyses that track these celestial movements 
            and interpret their influences on all zodiac signs.</p>
            
            <h4>Key aspects for this period:</h4>
            <ul>
                <li>Mercury forms a trine with Pluto, enhancing mental depth</li>
                <li>Venus squares Saturn, creating tension in relationships</li>
                <li>Mars sextiles Jupiter, boosting energy and confidence</li>
                <li>Sun opposes Uranus, bringing unexpected changes</li>
            </ul>
            
            <p>Explore the daily analysis for more specific influences.</p>
        </div>
        """
        chart_content_soup = BeautifulSoup(chart_content, 'html.parser')
        
        for placeholder in cms_placeholders:
            # Check if we're in a chart content area
            parent_el = placeholder.parent
            
            # Is this in a Daily Chart section?
            chart_headers = parent_el.find_previous(["h1", "h2", "h3"], string=re.compile("Daily Chart", re.IGNORECASE))
            if chart_headers or "chart" in str(parent_el).lower():
                # Replace with chart content
                new_div = soup.new_tag("div")
                new_div.append(chart_content_soup)
                new_div.append(chart_links_soup)
                
                # Replace the placeholder
                placeholder.replace_with(new_div)
                fixes_applied += 1
            else:
                # Generic placeholder replacement
                new_text = "This content is updated weekly with new astrological insights."
                placeholder.replace_with(new_text)
                fixes_applied += 1
        
        # Fix empty chart list containers
        empty_chart_lists = soup.select('.w-dyn-empty')
        for empty_list in empty_chart_lists:
            # Check if it's likely a chart list
            parent = empty_list.parent
            if 'chart' in str(parent).lower() or 'aspect' in str(parent).lower():
                empty_list.replace_with(chart_links_soup)
                fixes_applied += 1
        
        if fixes_applied > 0:
            # Write the fixed content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            print(f"Fixed {fixes_applied} CMS placeholders in {file_path}")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def fix_read_more_sections(file_path):
    """Fix 'Read More' sections by finding working ones and copying their structure"""
    try:
        # First check if this is a file that needs fixing
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        if "read more" not in content.lower():
            return False
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find working read more sections (those with links)
        working_sections = []
        read_more_headings = soup.find_all(string=re.compile("Read More", re.IGNORECASE))
        
        for heading in read_more_headings:
            # Find the nearest parent that might contain the whole section
            parent_section = heading.find_parent(['div', 'section'])
            if parent_section:
                links = parent_section.find_all('a')
                if links and len(links) > 5:  # Assuming a working section has several links
                    working_sections.append(parent_section)
        
        if not working_sections:
            # If we can't find a working section in this file, let's look in a known good file
            try:
                good_file = "/Users/seanivore/Development/astrofluenced/astrology-reading/improve-life/change-your-outlook.html"
                with open(good_file, 'r', encoding='utf-8', errors='ignore') as f:
                    good_content = f.read()
                
                good_soup = BeautifulSoup(good_content, 'html.parser')
                good_headings = good_soup.find_all(string=re.compile("Read More", re.IGNORECASE))
                
                for heading in good_headings:
                    parent_section = heading.find_parent(['div', 'section'])
                    if parent_section:
                        links = parent_section.find_all('a')
                        if links and len(links) > 5:
                            working_sections.append(parent_section)
                            break
            except Exception as e:
                print(f"Error finding template section: {e}")
            
            if not working_sections:
                # Still no template found, create a generic one
                generic_html = """
                <div class="read-more-section">
                    <h3>Read More Daily Chart Analysis</h3>
                    <div class="chart-links-wrapper">
                        <!-- Chart links will be inserted here -->
                    </div>
                </div>
                """
                generic_section = BeautifulSoup(generic_html, 'html.parser')
                chart_links_html = get_chart_links_html()
                chart_links_soup = BeautifulSoup(chart_links_html, 'html.parser')
                
                # Insert links into the generic template
                link_container = generic_section.select_one('.chart-links-wrapper')
                if link_container:
                    link_container.append(chart_links_soup)
                    working_sections.append(generic_section)
                
                if not working_sections:
                    return False
        
        # Now find empty or broken read more sections
        fixes_applied = 0
        
        for heading in read_more_headings:
            parent_section = heading.find_parent(['div', 'section'])
            if parent_section:
                links = parent_section.find_all('a')
                if not links or len(links) < 3:  # This section needs fixing
                    # Replace with a copy of a working section (safely)
                    if working_sections:
                        parent_section.replace_with(working_sections[0].prettify())
                        fixes_applied += 1
        
        if fixes_applied > 0:
            # Write the fixed content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            print(f"Fixed {fixes_applied} Read More sections in {file_path}")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error fixing Read More sections in {file_path}: {e}")
        return False

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Get all HTML files
    html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)
    
    print(f"Processing {len(html_files)} HTML files...")
    
    # Track results
    cms_fixes = 0
    read_more_fixes = 0
    
    for html_file in html_files:
        if fix_cms_placeholders(html_file):
            cms_fixes += 1
        
        if fix_read_more_sections(html_file):
            read_more_fixes += 1
    
    print(f"\nSummary:")
    print(f"- Fixed CMS placeholders in {cms_fixes} files")
    print(f"- Fixed Read More sections in {read_more_fixes} files")
    
    if cms_fixes > 0 or read_more_fixes > 0:
        print("\nNext steps:")
        print("1. Refresh your browser (hard refresh with Cmd+Shift+R)")
        print("2. Check if Daily Chart Analysis sections now show content")
        print("3. Verify Read More sections have proper links")
    else:
        print("\nNo fixes needed. All files appear to be working correctly.")

if __name__ == "__main__":
    main() 