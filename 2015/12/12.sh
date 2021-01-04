#!/bin/bash

echo -n "Answer to part 1: "
(echo -n  0;cat $1 | sed 's/[^-0-9]/ /g' |  tr -d '\n' | tr -s ' ' | sed 's/ / + /g'; echo 0)|paste| bc

echo -n "Answer to part 2: "

(echo -n  0;./12b.py $1 | sed 's/[^-0-9]/ /g' |  tr -d '\n' | tr -s ' ' | sed 's/ / + /g'; echo 0)|paste| bc
