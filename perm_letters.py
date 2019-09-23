#!/usr/local/bin/python3

# for given list of letters, show all permutations
# that are found in a dictionary

from itertools import permutations

l = ['t', 'i', 'e', 'r', 'e', 'h']
l = ['c', 'a', 's', 'i', 'n', 'o']
s = 'tiereh'
s = 'casino'
s = 'hurdle'
s = 'snuiqt'

debug=False

words = []

for l in 3, 4, 5, 6:
    perm = permutations( list(s), l)
    for i in perm:
        w = ''.join(i)
        words.append(w)

if debug:
    print('permutations:')
    print(words)

from spellchecker import SpellChecker

spell = SpellChecker( distance=1 )

known = spell.known( words )

print('known words:')
print('\n'.join(known))
