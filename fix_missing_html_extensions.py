import os
import re
from bs4 import BeautifulSoup
import glob

def fix_links_in_file(file_path):
    """Fix links that are missing .html extension in the given file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Parse HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        # Track changes
        links_fixed = 0
        
        # Fix links in href attributes
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            
            # Skip external links, anchors, and links that already have extensions
            if (href.startswith('http://') or href.startswith('https://') or 
                href.startswith('#') or href.startswith('mailto:') or 
                href.startswith('tel:') or '.' in os.path.basename(href)):
                continue
            
            # Skip links to directories that end with '/'
            if href.endswith('/'):
                continue
            
            # Add .html extension to links
            a_tag['href'] = f"{href}.html"
            links_fixed += 1
        
        # Fix links in other attributes that might contain URLs
        for tag in soup.find_all(attrs={"data-href": True}):
            href = tag['data-href']
            
            if (href.startswith('http://') or href.startswith('https://') or 
                href.startswith('#') or href.startswith('mailto:') or 
                href.startswith('tel:') or '.' in os.path.basename(href)):
                continue
            
            if href.endswith('/'):
                continue
                
            tag['data-href'] = f"{href}.html"
            links_fixed += 1
        
        # Only save if changes were made
        if links_fixed > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Fixed {links_fixed} links in {file_path}")
            return links_fixed
        
        return 0
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0

def fix_links_in_css_files(file_path):
    """Fix URL references in CSS files that might be missing .html extension"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Track changes
        links_fixed = 0
        
        # Pattern to find url() references in CSS that might need .html appended
        # This is a simplistic approach - might need refinement
        modified_content = re.sub(
            r'url\([\'"]?([^\'")]+/[a-zA-Z0-9_-]+)(?![.\'")/])[\'"]?\)', 
            r'url(\1.html)', 
            content
        )
        
        if modified_content != content:
            links_fixed = modified_content.count('.html') - content.count('.html')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            print(f"Fixed {links_fixed} CSS references in {file_path}")
            return links_fixed
        
        return 0
    
    except Exception as e:
        print(f"Error processing CSS file {file_path}: {e}")
        return 0

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Count total files to process
    html_files = glob.glob(os.path.join(base_dir, "**/*.html"), recursive=True)
    css_files = glob.glob(os.path.join(base_dir, "**/*.css"), recursive=True)
    
    print(f"Processing {len(html_files)} HTML files and {len(css_files)} CSS files...")
    
    # Process HTML files
    total_html_links_fixed = 0
    for html_file in html_files:
        total_html_links_fixed += fix_links_in_file(html_file)
    
    # Process CSS files
    total_css_links_fixed = 0
    for css_file in css_files:
        total_css_links_fixed += fix_links_in_css_files(css_file)
    
    print(f"\nSummary:")
    print(f"- Fixed {total_html_links_fixed} links in HTML files")
    print(f"- Fixed {total_css_links_fixed} URL references in CSS files")
    print(f"- Total fixed: {total_html_links_fixed + total_css_links_fixed}")
    
    if total_html_links_fixed + total_css_links_fixed > 0:
        print("\nNext steps:")
        print("1. Refresh your browser (hard refresh with Cmd+Shift+R)")
        print("2. Check if links to collection pages now work correctly")
        print("3. Verify that image and other media URLs are loading properly")
    else:
        print("\nNo changes were made. All links appear to already have proper extensions.")

if __name__ == "__main__":
    main() 