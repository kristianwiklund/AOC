#!/bin/bash

function x {
    IFS=- read -a L <<< $1
    C=`tr -d ':' <<< $2`
    seq ${L[0]} ${L[1]}|sed -e 's/^/^/' -e "s/\$/$C/" > tmp

    sed 's/\(.\)/\1 /g' <<< $3 | tr ' ' '\n' | sort | uniq -c | tr -d ' ' | grep $C | grep -f tmp
}

(cat input | while read i; do 
    x $i
done) | wc -l
