import os
import re
from bs4 import BeautifulSoup

def fix_cms_content(html_dir):
    """Find and fix pages with missing CMS content"""
    fixed_files = 0
    
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
                    
                    # Find all empty CMS elements
                    empty_elements = soup.select('.w-dyn-empty')
                    
                    if empty_elements:
                        for element in empty_elements:
                            # Create placeholder content
                            placeholder = soup.new_tag('div')
                            placeholder['class'] = 'placeholder-content'
                            placeholder['style'] = 'padding: 20px; background-color: #f8f8f8; border-radius: 8px; margin: 10px 0;'
                            
                            # Add different placeholders based on context
                            if 'horoscope' in file_path.lower() or 'zodiac' in file_path.lower():
                                placeholder.string = 'Astrological content will appear here when connected to the live CMS.'
                            elif 'reading' in file_path.lower():
                                placeholder.string = 'Your personalized reading will appear here when connected to the live CMS.'
                            elif 'growth' in file_path.lower() or 'introspection' in file_path.lower():
                                placeholder.string = 'Growth and introspection content will appear here when connected to the live CMS.'
                            else:
                                placeholder.string = 'Content from the CMS will appear here in the live version.'
                            
                            # Replace the empty element with our placeholder
                            element.replace_with(placeholder)
                            modified = True
                    
                    # Also look for collection-item wrappers that might be missing items
                    collection_lists = soup.select('.w-dyn-items')
                    for collection in collection_lists:
                        if len(collection.contents) == 0 or (len(collection.contents) == 1 and 'w-dyn-empty' in str(collection.contents[0])):
                            # Create sample items
                            for i in range(3):
                                item = soup.new_tag('div')
                                item['class'] = 'placeholder-item'
                                item['style'] = 'padding: 15px; background-color: #f8f8f8; border-radius: 8px; margin: 10px 0;'
                                item.string = f'Sample item {i+1} - will be populated from CMS in the live version.'
                                collection.append(item)
                            modified = True
                    
                    if modified:
                        # Save the modified file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(str(soup))
                        fixed_files += 1
                        print(f"Fixed CMS content in {file_path}")
                
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return fixed_files

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Fix CMS content
    fixed_files = fix_cms_content(base_dir)
    print(f"Fixed CMS content in {fixed_files} files")
    
    print("\nNext steps:")
    print("1. Run the local server to view the updated site")
    print("   python start_local_server.py")

if __name__ == "__main__":
    main() 