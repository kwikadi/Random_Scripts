import sys
word = sys.argv[1]
new_word = list(word)
print "".join(sorted(new_word, key=lambda s: s.lower()))
