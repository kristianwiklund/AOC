#!/bin/sh

(echo ibase=2;cat input.txt | tr 'FBLR' '0101' ) | bc | sort -n | tail -1
(echo ibase=2;cat input.txt | tr 'FBLR' '0101' ) | bc | sort -n > tmp
seq `head -1 tmp` `tail -1 tmp` > tmp2
grep -v -f tmp tmp2

