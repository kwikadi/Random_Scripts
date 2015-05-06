#1. Check if 'Templates' and 'Static' are made or not. If no, create.
#2. Check inside 'Static' for 'css', 'js' , 'img' folders.
#3. Scan complete folder.
#4. If file is css, js, or {img}, put in resp folders
#5. If html, scan line by line, and replace sources with {url_for()}

import os
from glob import glob

dirs = ["templates", "static", "static\css", "static\js", "static\img"]

for directory in dirs:
	if not os.path.isdir(directory):
		os.makedirs(directory)

css_files = glob(*.css)
js_files = glob(*.js)
img_files = glob(*.jpg)
