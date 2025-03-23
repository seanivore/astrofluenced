# Astrofluenced

Static website export from Webflow with local fixes for offline viewing.

## Overview

This is a static export of the Astrofluenced website, enhanced with various scripts to make the content viewable offline and fix common issues with static Webflow exports.

## Features

- Fixed relative paths for assets and links
- Added HTML extensions to internal links
- Fixed conditional content that would normally require CMS connectivity
- Fixed zodiac images and created placeholders where needed
- Added art style interpretations and visual timelines
- Created collection pages for horoscopes
- Local server for easy viewing

## Scripts

Various Python scripts have been created to fix common issues:

- `fix_conditional_content.py` - Makes conditionally hidden content visible
- `fix_external_links.py` - Converts external links to local ones
- `fix_zodiac_images.py` - Ensures zodiac images display correctly
- `fix_horoscope_collections.py` - Creates content for horoscope collection pages
- `fix_art_deco_images.py` - Fixes art deco images
- `fix_artist_interpretations.py` - Adds artist interpretation images
- `fix_timeline_interpretations.py` - Adds visual timeline images
- And many more to address specific issues

## Local Development

1. Clone this repository
2. Run the local server:
   ```
   python start_local_server.py
   ```
3. Open your browser to http://localhost:8000

## GitHub Pages Deployment

To deploy to GitHub Pages:

1. Push this repository to GitHub
2. Go to Repository Settings > Pages
3. Select the branch you want to publish from (usually `main`)
4. Choose the root folder `/` as the source
5. Click Save
6. Your site will be published at `https://[your-username].github.io/astrofluenced/`

## Notes

- The site is large (over 100MB) due to the comprehensive content and assets
- All scripts are small and stored in the root directory for easy access
- This is a static version and does not include dynamic CMS features

## Site Recovery Status

This site is in deep recovery, pulled from the depths of the internet and clawed from the clenched jaws of Webflow. The static export has been transformed from a broken shell into a functioning archive through numerous rescue operations and script-based CPR. While not every corner has been fully resuscitated, the core experience has been salvaged and made navigable.

Many of the beautiful design elements and intricate details from the original site have been preserved, though some dynamic features that relied on Webflow's CMS remain in a simplified state. Consider this a functional archaeological exhibit - showing what once was while still being completely usable.