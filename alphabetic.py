import sys
word = sys.argv[1]
print "".join(sorted(list(word), key=lambda s: s.lower()))
