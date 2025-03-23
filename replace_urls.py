import os
import re

# Setup
html_dir = "/Users/seanivore/Development/astrofluenced"

def process_srcset(srcset_value, cdn_pattern):
    """Process srcset attributes which contain multiple URLs with size descriptors."""
    if not srcset_value:
        return srcset_value
        
    parts = srcset_value.split(',')
    new_parts = []
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
            
        # Split the URL from the size descriptor
        space_pos = part.find(' ')
        if space_pos > 0:
            url = part[:space_pos].strip()
            size = part[space_pos:].strip()
        else:
            url = part
            size = ""
            
        # Replace the URL if it matches our pattern
        if re.search(cdn_pattern, url):
            new_url = f"assets/downloaded/images/{url.split('/')[-1]}"
            new_parts.append(f"{new_url} {size}".strip())
        else:
            new_parts.append(part)
            
    return ', '.join(new_parts)

def replace_urls_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Store original content to check if changes were made
    original_content = content
    
    # Define the CDN pattern we want to replace
    cdn_pattern = r'https://cdn\.prod\.website-files\.com/[^\'"<>() \t]+'
    
    # Handle srcset attributes separately with our special function
    def handle_srcset(match):
        srcset_value = match.group(1)
        new_srcset = process_srcset(srcset_value, cdn_pattern)
        return f'srcset="{new_srcset}"'
    
    # Replace srcset attributes
    content = re.sub(r'srcset="([^"]*)"', handle_srcset, content)
    
    # Handle data-src attributes for lazy loading
    content = re.sub(
        r'data-src="(' + cdn_pattern + r'\.(jpg|jpeg|png|webp|gif|svg))"',
        lambda m: f'data-src="assets/downloaded/images/{m.group(1).split("/")[-1]}"',
        content
    )
    
    # Replace image URLs in src attributes
    content = re.sub(
        r'src="(' + cdn_pattern + r'\.(jpg|jpeg|png|webp|gif|svg))"',
        lambda m: f'src="assets/downloaded/images/{m.group(1).split("/")[-1]}"',
        content
    )
    
    # Replace CSS URLs in link tags
    content = re.sub(
        r'href="(' + cdn_pattern + r'\.css[^"]*)"',
        lambda m: f'href="assets/downloaded/css/{m.group(1).split("/")[-1]}"',
        content
    )
    
    # Replace JS URLs
    content = re.sub(
        r'src="(' + cdn_pattern + r'\.js[^"]*)"',
        lambda m: f'src="assets/downloaded/js/{m.group(1).split("/")[-1]}"',
        content
    )
    
    # Replace lottie animation URLs
    content = re.sub(
        r'data-src="(' + cdn_pattern + r'\.lottie)"',
        lambda m: f'data-src="assets/downloaded/lottie/{m.group(1).split("/")[-1]}"',
        content
    )
    
    # Replace background image URLs in inline styles
    content = re.sub(
        r'background-image:\s*url\(["\']?(' + cdn_pattern + r')["\']?\)',
        lambda m: f'background-image: url("assets/downloaded/images/{m.group(1).split("/")[-1]}")',
        content
    )
    
    # Replace og:image and other meta tag URLs
    content = re.sub(
        r'content="(' + cdn_pattern + r'\.(jpg|jpeg|png|webp|gif|svg))"',
        lambda m: f'content="assets/downloaded/images/{m.group(1).split("/")[-1]}"',
        content
    )

    # Handle favicon and apple-touch-icon
    content = re.sub(
        r'href="(' + cdn_pattern + r'\.(ico|png))"(\s+rel="(shortcut icon|apple-touch-icon)")',
        lambda m: f'href="assets/downloaded/images/{m.group(1).split("/")[-1]}"{m.group(3)}',
        content
    )
    
    # Write the file back only if changes were made
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error writing to {file_path}: {e}")
            return False
    return False

def main():
    # Count of files updated
    updated_files = 0
    
    # Process all HTML, CSS, and JS files
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.endswith(('.html', '.css', '.js')):
                file_path = os.path.join(root, file)
                try:
                    if replace_urls_in_file(file_path):
                        updated_files += 1
                        print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    print(f"\nFinished replacing URLs in {updated_files} files.")
    print("Next steps:")
    print("1. Make sure all assets were downloaded properly")
    print("2. Test the site with a local server to verify it works correctly")
    
if __name__ == "__main__":
    main()
