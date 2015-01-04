import os, sys

source = str(sys.argv[1])

for root,dirs,files in os.walk(source):
	for name in files:
		paths = os.path.join(root,name)
		if os.stat(paths).st_size == 0:
			print paths
			os.remove(paths)
