import os
import re
from bs4 import BeautifulSoup

def fix_conditional_content(html_dir):
    """Make all conditionally displayed content visible"""
    modified_files = 0
    
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                modified = False
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Parse HTML
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    # Fix 1: Make all hidden elements visible
                    for elem in soup.select('[style*="display: none"]'):
                        style = elem.get('style', '')
                        new_style = re.sub(r'display:\s*none\s*;?', '', style)
                        elem['style'] = new_style
                        modified = True
                    
                    # Fix 2: Remove w-condition classes that control visibility
                    for elem in soup.select('.w-condition-invisible'):
                        # Only remove the class, keep the element
                        if 'class' in elem.attrs:
                            classes = elem['class']
                            if 'w-condition-invisible' in classes:
                                classes.remove('w-condition-invisible')
                                modified = True
                    
                    # Fix 3: Replace empty CMS lists with placeholder content
                    for elem in soup.select('.w-dyn-empty'):
                        placeholder = soup.new_tag('div')
                        placeholder['class'] = 'placeholder-content'
                        placeholder['style'] = 'padding: 20px; background-color: #f8f8f8; border-radius: 8px; margin: 10px 0;'
                        
                        context = "content"
                        if "horoscope" in file_path.lower() or "zodiac" in file_path.lower():
                            context = "horoscope information"
                        elif "reading" in file_path.lower():
                            context = "astrological reading"
                        
                        placeholder.string = f'This {context} is updated weekly in the live site. This static version shows a snapshot in time.'
                        
                        elem.replace_with(placeholder)
                        modified = True
                    
                    # Fix 4: If there are collection lists with no items, add sample items
                    for collection in soup.select('.w-dyn-items'):
                        if len(collection.contents) == 0 or (len(collection.contents) == 1 and 'w-dyn-empty' in str(collection.contents[0])):
                            # Look at parent to determine what kind of items to create
                            parent_classes = ' '.join(collection.parent.get('class', []))
                            
                            # Determine item type based on context
                            item_context = "Content item"
                            if "horoscope" in parent_classes.lower() or "zodiac" in parent_classes.lower():
                                item_context = "Horoscope entry"
                            elif "reading" in parent_classes.lower():
                                item_context = "Reading"
                            
                            # Create sample items
                            for i in range(3):
                                item = soup.new_tag('div')
                                item['class'] = 'placeholder-collection-item'
                                item['style'] = 'padding: 15px; background-color: #f8f8f8; border-radius: 8px; margin: 10px 0;'
                                
                                title = soup.new_tag('h4')
                                title.string = f'Sample {item_context} {i+1}'
                                
                                desc = soup.new_tag('p')
                                desc.string = 'This would typically display content from the CMS that updates weekly.'
                                
                                item.append(title)
                                item.append(desc)
                                collection.append(item)
                            
                            modified = True
                    
                    # Fix 5: Check for data-wf-collection attributes (indicates CMS content)
                    for elem in soup.select('[data-wf-collection]'):
                        # If it has no children, add explanation
                        if not elem.contents or (len(elem.contents) == 1 and 'w-dyn-empty' in str(elem.contents[0])):
                            explanation = soup.new_tag('div')
                            explanation['class'] = 'cms-explanation'
                            explanation['style'] = 'padding: 15px; background-color: #f5f5f5; border: 1px solid #eee; margin: 10px 0; font-style: italic;'
                            
                            collection_id = elem.get('data-wf-collection', 'unknown')
                            explanation.string = f'This area would display content from Webflow CMS collection "{collection_id}" in the live site.'
                            
                            # Add it as a child if the element can have children
                            if elem.name not in ['img', 'input', 'br', 'hr']:
                                elem.append(explanation)
                                modified = True
                    
                    # Fix 6: Look for empty image tags, especially in collection templates
                    for img in soup.select('img[src=""], img:not([src])'):
                        parent_classes = ' '.join(img.parent.get('class', []))
                        is_collection_item = any(cls in parent_classes for cls in ['w-dyn-item', 'collection-item'])
                        
                        # If it's in a collection, add a placeholder image
                        if is_collection_item:
                            img['src'] = f"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='200' viewBox='0 0 300 200'%3E%3Crect width='300' height='200' fill='%23CCCCCC'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='Arial' font-size='16' fill='%23333333'%3EPlaceholder Image%3C/text%3E%3C/svg%3E"
                            img['alt'] = "Placeholder for CMS image"
                            modified = True
                    
                    # Fix 7: Convert Webflow's JS bindings to static content where possible
                    for bind_elem in soup.select('[data-w-id]'):
                        # Check if this is an animation that should be visible
                        if 'animated' in ' '.join(bind_elem.get('class', [])) and 'opacity:0' in bind_elem.get('style', ''):
                            # Make animations visible by default
                            style = bind_elem.get('style', '')
                            new_style = style.replace('opacity:0', 'opacity:1')
                            bind_elem['style'] = new_style
                            modified = True
                    
                    if modified:
                        # Save the modified file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(str(soup))
                        modified_files += 1
                        print(f"Fixed conditional content in {file_path}")
                
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    return modified_files

def scan_for_cms_issues(html_dir):
    """Scan files for potential CMS issues without modifying them"""
    cms_related_files = []
    
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Check for CMS-related classes and attributes
                    if any(marker in content for marker in [
                        'w-dyn-', 'data-wf-collection', 'w-condition-', 
                        'collection-list-', 'collection-item-'
                    ]):
                        cms_related_files.append(file_path)
                
                except Exception as e:
                    print(f"Error scanning {file_path}: {e}")
    
    return cms_related_files

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    
    # First scan for potential CMS issues
    print("Scanning for files with potential CMS-related issues...")
    cms_files = scan_for_cms_issues(base_dir)
    
    if cms_files:
        print(f"Found {len(cms_files)} files with potential CMS content:")
        for i, file_path in enumerate(cms_files[:10]):  # Show first 10
            rel_path = os.path.relpath(file_path, base_dir)
            print(f"  {i+1}. {rel_path}")
        
        if len(cms_files) > 10:
            print(f"  ... and {len(cms_files) - 10} more files")
    
    # Fix conditional content
    print("\nFixing conditional content issues...")
    modified_files = fix_conditional_content(base_dir)
    print(f"Fixed conditional content in {modified_files} files")
    
    print("\nNext steps:")
    print("1. Hard refresh your browser (Cmd+Shift+R)")
    print("2. All conditionally displayed content should now be visible")
    print("3. Empty CMS elements should be replaced with placeholders")
    print("4. For the best experience, focus on fixed pages instead of dynamic CMS pages")

if __name__ == "__main__":
    main() 