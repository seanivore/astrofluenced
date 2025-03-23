import os
import re

def fix_paths_in_file(file_path):
    # Determine the depth from root
    rel_path = os.path.relpath(file_path, "/Users/seanivore/Development/astrofluenced")
    depth = len(rel_path.split(os.sep)) - 1  # -1 because we're counting directories, not the file itself
    
    prefix = "../" * depth if depth > 0 else ""
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Store original content to check if changes were made
    original_content = content
    
    # Fix paths that start with assets/ to include the proper number of ../ based on directory depth
    if depth > 0:
        content = re.sub(
            r'(href|src)="(assets/)',
            f'\\1="{prefix}\\2',
            content
        )
        
        # Fix paths for lottie animations
        content = re.sub(
            r'data-src="(assets/)',
            f'data-src="{prefix}\\1',
            content
        )
        
        # Fix other content URLs like og:image
        content = re.sub(
            r'content="(assets/)',
            f'content="{prefix}\\1',
            content
        )
        
        # Fix background-image URLs
        content = re.sub(
            r'background-image:\s*url\(["\']?(assets/)',
            f'background-image: url(""{prefix}\\1',
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
    # Root directory
    html_dir = "/Users/seanivore/Development/astrofluenced"
    
    # Count of files updated
    updated_files = 0
    
    # Process all HTML files
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    if fix_paths_in_file(file_path):
                        updated_files += 1
                        print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    print(f"\nFinished fixing paths in {updated_files} files.")
    
if __name__ == "__main__":
    main() 