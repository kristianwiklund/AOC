#!/bin/bash

cat input.txt | sed -e 's/(/.+1\n/g' -e 's/)/.-1\n/g' -e 's/^/0\n/' | bc -l  | nl -v 0 | grep -- "-1$" | head -1
