import os
import glob
from bs4 import BeautifulSoup
import re

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
        # Convert to relative path for proper linking
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

def create_chart_analysis_content():
    """Create the HTML content for chart analysis sections"""
    links = get_chart_analysis_links()
    
    # Create the HTML structure
    html = """
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
        
        <div class="chart-links-container">
    """
    
    # Add the links
    for link in links:
        html += f'<div class="chart-link-item"><a href="{link["href"]}" class="chart-link">{link["text"]}</a></div>\n'
    
    # Close the div containers
    html += """
        </div>
    </div>
    """
    
    return html

def fix_file(file_path):
    """Replace CMS placeholders with actual chart analysis content"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        if "Your personalized reading will appear here when connected" not in content:
            return False
            
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find CMS placeholders
        placeholders = soup.find_all(string=re.compile("Your personalized reading will appear here when connected"))
        
        if not placeholders:
            return False
        
        # Get chart analysis content
        chart_content = create_chart_analysis_content()
        
        # Count replacements
        replacements = 0
        
        # Replace placeholders 
        for placeholder in placeholders:
            # Find the parent element
            parent = placeholder.parent
            
            # Create new element with chart content
            new_content = BeautifulSoup(chart_content, 'html.parser')
            
            # Replace the placeholder with new content
            placeholder.replace_with(new_content)
            replacements += 1
        
        # Only save if changes were made
        if replacements > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Fixed {replacements} placeholder(s) in {file_path}")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Get specific files that need fixing
    target_files = [
        os.path.join(base_dir, "astrology-reading/improve-life/growth-through-introspection.html"),
        os.path.join(base_dir, "astrology-reading/improve-life/change-your-outlook.html"),
        os.path.join(base_dir, "astrology-reading/improve-life/internal-external-personal-growth.html"),
        os.path.join(base_dir, "astrology-reading/energy-planning/mid-week-integrate.html"),
        os.path.join(base_dir, "astrology-reading/energy-planning/weekend-perfect.html"),
        os.path.join(base_dir, "astrology-reading/energy-planning/start-week-aspects.html"),
        os.path.join(base_dir, "astrology-reading/today/chart-briefing.html"),
        os.path.join(base_dir, "astrology-reading/today/horoscopes.html"),
        os.path.join(base_dir, "astrology-reading/today/create-positive-life-changes.html"),
        os.path.join(base_dir, "astrology-reading/today/energy-planner.html")
    ]
    
    fixed_count = 0
    for file in target_files:
        if os.path.exists(file) and fix_file(file):
            fixed_count += 1
    
    print(f"\nSummary: Fixed {fixed_count} files with chart analysis content.")
    
    if fixed_count > 0:
        print("\nNext steps:")
        print("1. Refresh your browser (Cmd+Shift+R)")
        print("2. Check if Daily Chart Analysis sections now show content")
    else:
        print("\nNo fixes needed or placeholders could not be found.")

if __name__ == "__main__":
    main() 