import os
import re
from bs4 import BeautifulSoup
import time

def add_cache_buster_to_images(html_dir):
    """Add cache-busting parameter to image URLs to force reload"""
    timestamp = int(time.time())
    modified_files = 0
    
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                modified = False
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Parse the HTML
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    # Find all images
                    images = soup.find_all('img')
                    
                    for img in images:
                        if img.get('src') and 'assets/downloaded/' in img.get('src'):
                            # Add or update cache-busting parameter
                            current_src = img['src']
                            if '?' in current_src:
                                new_src = current_src.split('?')[0] + f'?v={timestamp}'
                            else:
                                new_src = current_src + f'?v={timestamp}'
                            
                            img['src'] = new_src
                            modified = True
                    
                    if modified:
                        # Save the modified file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(str(soup))
                        modified_files += 1
                        print(f"Added cache-busting to images in {file_path}")
                
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return modified_files

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Add cache-busting parameters
    modified_files = add_cache_buster_to_images(base_dir)
    print(f"Added cache-busting parameters to images in {modified_files} files")
    
    print("\nNext steps:")
    print("1. Restart the browser and access the site again at http://localhost:8000")
    print("2. The images should now load fresh from the server")

if __name__ == "__main__":
    main() 