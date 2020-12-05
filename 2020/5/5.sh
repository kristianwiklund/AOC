#!/bin/sh

(echo ibase=2;cat input.short | tr 'FBLR' '0101' | sed 's/\(.......\)\(...\)/\1*8+\2/') | bc | sort -n | tail -1

