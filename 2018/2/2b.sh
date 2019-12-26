#!/bin/bash

for i in $(seq 1 `head -1 input.txt|wc -c`); do
 sed   "s/^\(.\{$(($i-1))\}\)./\1./" < input.txt | xargs -I X -n 1 bash -c '(echo -n "X ";grep -c X input.txt)'|grep 2| tr -d '.'
done
