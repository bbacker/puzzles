#!/usr/local/bin/python3

# for wordscapes app:
# for given list of letters, show all permutations
# that are found in a dictionary

# usage: ./perm_letters  -s casino
#        ./perm_letters -v 2 -s lremot

import argparse
from itertools import permutations

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", type=int, help="verbose level, default 0", default=0)
parser.add_argument("-s", "--string", type=str, help="string of target letters to permute, e.g. tireeh")

args=parser.parse_args()
ss=args.string

verbose=args.verbose

perms = []

for l in 3, 4, 5, 6:
    perm = permutations( list(ss), l)
    for i in perm:
        w = ''.join(i)
        perms.append(w)

if verbose > 2:
    print('permutations:')
    print(perms)

from spellchecker import SpellChecker

spell = SpellChecker( distance=1 )

known = spell.known( perms )

print('\n'.join( sorted(known) ))
