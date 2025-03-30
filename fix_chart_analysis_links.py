import os
import glob
from bs4 import BeautifulSoup
import re

def fix_chart_links(file_path):
    """Fix links to chart analysis pages, including pagination parameters"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if there are any chart analysis links in this file
        if "chart-analysis" not in content:
            return False
        
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find all links
        links = soup.find_all('a', href=True)
        
        # Track changes
        fixed_links = 0
        
        for link in links:
            href = link['href']
            
            # Check if this is a chart analysis link with pagination
            if 'chart-analysis' in href and '?' in href:
                # Fix the encoded characters in the URL
                new_href = href.replace('?79bf6db2_page=', '-page')
                new_href = new_href.replace('%3F', '-')
                new_href = new_href.replace('%3D', '-')
                
                # Update the link
                link['href'] = new_href
                fixed_links += 1
        
        # Only save if changes were made
        if fixed_links > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Fixed {fixed_links} chart analysis links in {file_path}")
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def rename_chart_files():
    """Rename chart analysis files to a more consistent naming pattern"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    chart_dir = os.path.join(base_dir, "astrology-reading/significant-aspects")
    
    # Find chart analysis files
    chart_files = glob.glob(os.path.join(chart_dir, "chart-analysis-*.html"))
    
    renamed_count = 0
    
    for file_path in chart_files:
        # Extract the current filename
        filename = os.path.basename(file_path)
        
        # Check if it has pagination parameters
        if '?' in filename:
            # Create a new filename with consistent formatting
            new_filename = filename.replace('?79bf6db2_page=', '-page')
            new_filename = new_filename.replace('%3F', '-')
            new_filename = new_filename.replace('%3D', '-')
            
            # Create the full path for the new file
            new_path = os.path.join(chart_dir, new_filename)
            
            # Rename the file
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} → {new_filename}")
            renamed_count += 1
    
    return renamed_count

def update_directory_links():
    """Create an index page with links to all chart analysis files"""
    base_dir = "/Users/seanivore/Development/astrofluenced"
    chart_dir = os.path.join(base_dir, "astrology-reading/significant-aspects")
    
    # Find all chart analysis files (after renaming)
    chart_files = glob.glob(os.path.join(chart_dir, "chart-analysis-*.html"))
    
    # Sort files by date
    chart_files.sort(reverse=True)
    
    # Create an HTML index page
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Chart Analysis Archive</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0e1e14;
            color: #e0e0e0;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #8dd9c0;
            margin-bottom: 40px;
        }
        .intro {
            text-align: center;
            margin-bottom: 30px;
        }
        .days-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 20px;
        }
        .day-group {
            background-color: rgba(30, 60, 50, 0.5);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            width: calc(50% - 20px);
        }
        @media (max-width: 768px) {
            .day-group {
                width: 100%;
            }
        }
        .day-group h2 {
            color: #8dd9c0;
            border-bottom: 1px solid #5a8d7e;
            padding-bottom: 10px;
            margin-top: 0;
        }
        .day-group ul {
            list-style-type: none;
            padding: 0;
        }
        .day-group li {
            margin-bottom: 10px;
        }
        .day-group a {
            color: #b0e0d0;
            text-decoration: none;
            display: block;
            padding: 8px 12px;
            border-radius: 4px;
            transition: background-color 0.2s;
        }
        .day-group a:hover {
            background-color: rgba(80, 140, 120, 0.3);
        }
        .page-link {
            font-size: 0.9em;
            color: #8abca9;
        }
        .back-link {
            display: block;
            text-align: center;
            margin-top: 40px;
            color: #8dd9c0;
            text-decoration: none;
        }
        .back-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Daily Chart Analysis Archive</h1>
    
    <div class="intro">
        <p>Browse our comprehensive collection of daily astrological chart analyses. Each day's analysis is broken into multiple pages for detailed insights.</p>
    </div>
    
    <div class="days-container">
"""
    
    # Group files by day
    day_groups = {}
    for file_path in chart_files:
        filename = os.path.basename(file_path)
        
        # Extract day name and date
        match = re.search(r'chart-analysis-([a-z]+)-(\d{2}-\d{2}-\d{4})', filename)
        if match:
            day_name = match.group(1).capitalize()
            date_str = match.group(2)
            
            # Create a key for this day
            day_key = f"{day_name} {date_str}"
            
            if day_key not in day_groups:
                day_groups[day_key] = []
            
            # Add this file to the day group
            day_groups[day_key].append({
                'filename': filename,
                'path': os.path.relpath(file_path, chart_dir)
            })
    
    # Add each day group to the HTML
    for day_key, files in sorted(day_groups.items()):
        # Sort files by page number
        files.sort(key=lambda x: 'page' in x['filename'] and int(re.search(r'page(\d+)', x['filename']).group(1)) or 0)
        
        index_html += f"""
        <div class="day-group">
            <h2>{day_key}</h2>
            <ul>
"""
        
        # Add links for each file
        for file_info in files:
            # Determine if this is a specific page
            if 'page' in file_info['filename']:
                page_match = re.search(r'page(\d+)', file_info['filename'])
                if page_match:
                    page_num = page_match.group(1)
                    link_text = f"{day_key} <span class='page-link'>(Page {page_num})</span>"
                else:
                    link_text = file_info['filename']
            else:
                link_text = f"{day_key} <span class='page-link'>(Main)</span>"
            
            index_html += f"""                <li><a href="{file_info['path']}">{link_text}</a></li>
"""
        
        index_html += """            </ul>
        </div>
"""
    
    # Close the HTML
    index_html += """    </div>
    
    <a href="../../index.html" class="back-link">← Back to Homepage</a>
</body>
</html>
"""
    
    # Write the index file
    index_path = os.path.join(chart_dir, "index.html")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f"Created chart analysis index page at {index_path}")
    return True

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # First rename chart analysis files to consistent format
    renamed_count = rename_chart_files()
    print(f"Renamed {renamed_count} chart analysis files to consistent format")
    
    # Create a nice index page for all chart analysis files
    update_directory_links()
    
    # Fix links in all HTML files
    html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)
    
    fixed_files = 0
    for file in html_files:
        if fix_chart_links(file):
            fixed_files += 1
    
    print(f"\nSummary: Fixed chart analysis links in {fixed_files} files")
    
    print("\nNext steps:")
    print("1. Refresh your browser (Cmd+Shift+R)")
    print("2. Visit the new chart analysis index page: /astrology-reading/significant-aspects/index.html")
    print("3. Check that all chart analysis links now work correctly")

if __name__ == "__main__":
    main() 