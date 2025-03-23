import os
import re

# Set the directory containing your HTML files
html_dir = "/Users/seanivore/Development/astrofluenced"
output_file = "/Users/seanivore/Development/astrofluenced/urls.txt"
download_script = "/Users/seanivore/Development/astrofluenced/download_assets.sh"
replace_script = "/Users/seanivore/Development/astrofluenced/replace_urls.py"

# Regex to match asset URLs
url_patterns = [
    r'<link[^>]+href="([^"]+)"',
    r'<img[^>]+src="([^"]+)"',
    r'<script[^>]+src="([^"]+)"',
    r'data-src="([^"]+)"',
    r'srcset="([^"]*)"',
    r'href="([^"]+\.lottie)"',
    r'background-image: *url\(["\']*([^"\'\)]+)["\'\)]'
]

# Set to store unique URLs
urls = set()

# Iterate through all .html files
for root, _, files in os.walk(html_dir):
    for file in files:
        if file.endswith(".html"):
            with open(os.path.join(root, file), "r", encoding="utf-8", errors='ignore') as f:
                content = f.read()
                for pattern in url_patterns:
                    matches = re.findall(pattern, content)
                    if pattern == r'srcset="([^"]*)"':  # Handle srcset which has multiple URLs
                        for srcset in matches:
                            # Split by commas and extract URLs
                            srcset_parts = srcset.split(',')
                            for part in srcset_parts:
                                url = part.strip().split(' ')[0]
                                if url.startswith("http"):
                                    urls.add(url)
                    else:
                        urls.update([m for m in matches if m.startswith("http")])

# Write URLs to the output file
cdn_urls = []
with open(output_file, "w") as f:
    for url in sorted(urls):
        if "cdn.prod.website-files.com" in url:
            cdn_urls.append(url)
            f.write(url + "\n")

print(f"Extracted {len(cdn_urls)} unique CDN URLs. Saved to {output_file}.")

# Create a download script
with open(download_script, "w") as f:
    f.write("#!/bin/bash\n\n")
    f.write("mkdir -p assets/downloaded/images\n")
    f.write("mkdir -p assets/downloaded/js\n")
    f.write("mkdir -p assets/downloaded/css\n")
    f.write("mkdir -p assets/downloaded/lottie\n\n")
    
    for url in cdn_urls:
        file_name = url.split('/')[-1]
        file_path = None
        
        if any(ext in file_name.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg']):
            file_path = f"assets/downloaded/images/{file_name}"
        elif file_name.endswith('.js'):
            file_path = f"assets/downloaded/js/{file_name}"
        elif file_name.endswith('.css'):
            file_path = f"assets/downloaded/css/{file_name}"
        elif file_name.endswith('.lottie'):
            file_path = f"assets/downloaded/lottie/{file_name}"
        else:
            file_path = f"assets/downloaded/{file_name}"
            
        f.write(f'curl -o "{file_path}" "{url}"\n')

print(f"Download script created at {download_script}")

# Create a replace script
with open(replace_script, "w") as f:
    f.write("""
import os
import re

# Setup
html_dir = "/Users/seanivore/Development/astrofluenced"

# Function to replace URLs in a file
def replace_urls_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Replace cdn URLs with local paths
    modified_content = content
    
    # Replace image URLs
    modified_content = re.sub(
        r'(https://cdn.prod.website-files.com/[^"\'\\s]+?\\.(?:jpg|jpeg|png|webp|gif|svg))',
        lambda m: f"assets/downloaded/images/{m.group(1).split('/')[-1]}",
        modified_content
    )
    
    # Replace JS URLs
    modified_content = re.sub(
        r'(https://cdn.prod.website-files.com/[^"\'\\s]+?\\.js)',
        lambda m: f"assets/downloaded/js/{m.group(1).split('/')[-1]}",
        modified_content
    )
    
    # Replace CSS URLs
    modified_content = re.sub(
        r'(https://cdn.prod.website-files.com/[^"\'\\s]+?\\.css)',
        lambda m: f"assets/downloaded/css/{m.group(1).split('/')[-1]}",
        modified_content
    )
    
    # Replace lottie URLs
    modified_content = re.sub(
        r'(https://cdn.prod.website-files.com/[^"\'\\s]+?\\.lottie)',
        lambda m: f"assets/downloaded/lottie/{m.group(1).split('/')[-1]}",
        modified_content
    )
    
    # Write modified content back
    if content != modified_content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        return True
    return False

# Process all HTML files
replaced_count = 0
for root, _, files in os.walk(html_dir):
    for file in files:
        if file.endswith(('.html', '.css', '.js')):
            file_path = os.path.join(root, file)
            if replace_urls_in_file(file_path):
                replaced_count += 1
                print(f"Updated: {file_path}")

print(f"Finished replacing URLs in {replaced_count} files.")
""")

print(f"Replace script created at {replace_script}")