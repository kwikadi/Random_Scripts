import os
from glob import glob

dirs = ["templates", "static", "static\css", "static\js", "static\img"]

for directory in dirs:
	if not os.path.isdir(directory):
		os.makedirs(directory)

css_files = glob("*.css")
js_files = glob("*.js")
img_files = glob("*.jpg")
html_files = glob("*.html")

for i in css_files:
	os.rename(i, "static\css\\" + i)

for i in js_files:
	os.rename(i, "static\js\\" + i)

for i in img_files:
	os.rename(i, "static\img\\" + i)

for i in html_files:
	with open(i, "w") as f:
		lines = f.readlines()
		for line in lines:
			#if reference to css/js/img found, replace.
	os.rename(i, "templates\\" + i)

