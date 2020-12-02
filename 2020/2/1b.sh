#!/bin/bash

function x {
     read  -a U <<< `tr '-' '\n' <<< $1`
     C=`tr -d ':' <<< $2`
     
     (head -c ${U[0]} < /dev/zero ; echo -n $C; head -c `expr ${U[1]} - ${U[0]}` < /dev/zero;echo "[^$C]") | tr '\0' '.' | sed 's/.//' > tmp
     (head -c ${U[0]} < /dev/zero ; echo -n "[^$C]"; head -c `expr ${U[1]} - ${U[0]}` < /dev/zero;echo "$C") | tr '\0' '.' | sed 's/.//' >> tmp
     echo $3 | grep -f tmp
}

(cat input.short | while read i; do
     x $i
done) 
