import os
from bs4 import BeautifulSoup
import re

def fix_external_links(html_dir):
    """Replace external links with local ones"""
    external_patterns = [
        'http://www.august.style/',
        'https://www.august.style/',
        'http://august.style/',
        'https://august.style/',
    ]
    
    modified_files = 0
    
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                modified = False
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Replace direct URL references
                    original_content = content
                    for pattern in external_patterns:
                        # Calculate the relative path to the root based on the file's depth
                        rel_depth = os.path.relpath(html_dir, os.path.dirname(file_path))
                        if rel_depth == '.':
                            # File is at root, no need for path adjustment
                            replacement = ''
                        else:
                            # File is in subdirectory, need to go up to root
                            replacement = rel_depth + '/'
                        
                        content = content.replace(pattern, replacement)
                    
                    # Now parse HTML to fix attributes
                    if content != original_content:
                        modified = True
                    
                    # Parse HTML to fix more complex cases
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    # Find all links
                    for a_tag in soup.find_all('a', href=True):
                        href = a_tag['href']
                        
                        # Check if it's an external link to august.style
                        for pattern in external_patterns:
                            if href.startswith(pattern):
                                # Get the path part after the domain
                                path = href.replace(pattern, '')
                                
                                # Calculate relative path
                                rel_depth = os.path.relpath(html_dir, os.path.dirname(file_path))
                                if rel_depth == '.':
                                    new_href = path
                                else:
                                    new_href = rel_depth + '/' + path
                                
                                # Add .html extension if it's a bare page reference
                                if not new_href.endswith('.html') and not new_href.endswith('/') and '.' not in new_href.split('/')[-1]:
                                    new_href += '.html'
                                
                                # Replace href
                                a_tag['href'] = new_href
                                modified = True
                                break
                    
                    if modified:
                        # Save the modified file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(str(soup))
                        modified_files += 1
                        print(f"Fixed external links in {file_path}")
                
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return modified_files

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Fix external links
    modified_files = fix_external_links(base_dir)
    print(f"Fixed external links in {modified_files} files")
    
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. Try clicking on links - they should now navigate within your local site")
    print("3. Use http://localhost:8000/ as your starting point")

if __name__ == "__main__":
    main() 