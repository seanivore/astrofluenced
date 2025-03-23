import os
import re
import requests
from urllib.parse import urlparse, unquote
from pathlib import Path

def collect_asset_paths_from_html(html_dir):
    """Scan all HTML files and collect assets referenced in them"""
    asset_paths = set()
    cdn_base = "https://cdn.prod.website-files.com"
    
    for root, _, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                    # Find all asset paths in src, href, data-src attributes
                    pattern = r'(src|href|data-src|content)="\.\.\/?(assets\/downloaded\/[^"]+)"'
                    matches = re.findall(pattern, content)
                    for _, path in matches:
                        # Normalize the path (remove ../ prefix if present)
                        normalized_path = path
                        if normalized_path.startswith('../'):
                            normalized_path = normalized_path[3:]
                        asset_paths.add(normalized_path)
                        
                    # Find background images
                    bg_pattern = r'background-image:\s*url\(["\']?\.\.\/?(assets\/downloaded\/[^"\'\)]+)["\']?\)'
                    bg_matches = re.findall(bg_pattern, content)
                    for path in bg_matches:
                        normalized_path = path
                        if normalized_path.startswith('../'):
                            normalized_path = normalized_path[3:]
                        asset_paths.add(normalized_path)
                    
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return asset_paths

def download_missing_assets(asset_paths, base_dir):
    """Download missing assets from CDN"""
    cdn_base = "https://cdn.prod.website-files.com/63eeb040bbd9e6ee6a1ef49e/"
    missing_assets = []
    downloaded = 0
    
    for asset_path in asset_paths:
        local_path = os.path.join(base_dir, asset_path)
        
        # Skip if asset already exists
        if os.path.exists(local_path):
            continue
            
        # Extract the filename part (after the last /)
        filename = asset_path.split('/')[-1]
        
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # Convert local path to CDN URL
        # Expected format: assets/downloaded/TYPE/FILENAME
        asset_type = asset_path.split('/')[2]  # images, css, js, lottie
        
        # Handle the case where asset_path doesn't follow the expected pattern
        if len(asset_path.split('/')) < 4:
            missing_assets.append(asset_path)
            continue
            
        cdn_url = f"{cdn_base}{filename}"
        
        try:
            print(f"Downloading {cdn_url} to {local_path}...")
            response = requests.get(cdn_url, stream=True)
            
            if response.status_code == 200:
                with open(local_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                downloaded += 1
                print(f"Successfully downloaded {local_path}")
            else:
                missing_assets.append(asset_path)
                print(f"Failed to download {cdn_url}: Status code {response.status_code}")
        except Exception as e:
            missing_assets.append(asset_path)
            print(f"Error downloading {cdn_url}: {e}")
    
    return downloaded, missing_assets

def main():
    base_dir = "/Users/seanivore/Development/astrofluenced"
    asset_paths = collect_asset_paths_from_html(base_dir)
    print(f"Found {len(asset_paths)} asset references in HTML files")
    
    downloaded, missing_assets = download_missing_assets(asset_paths, base_dir)
    print(f"Downloaded {downloaded} missing assets")
    
    if missing_assets:
        print(f"Failed to download {len(missing_assets)} assets:")
        for path in missing_assets:
            print(f"  {path}")
    
    print("\nNext steps:")
    if missing_assets:
        print("1. Check the list of missing assets and download them manually if needed")
    print("2. Restart the local server to view the updated site")
    print("   python start_local_server.py")
    
if __name__ == "__main__":
    main() 