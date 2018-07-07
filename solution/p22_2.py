"""
Filename: p22.py

"""

score = lambda word: sum(ord(c)-64 for c in word)
names = sorted(open('p022_names.txt').read().rstrip().replace('"', '').split(','))

s = sum(ln * score(name) for ln, name in enumerate(names, 1))
print "Total name score =", s
