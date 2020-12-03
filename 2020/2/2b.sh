#!/bin/bash

function x {
     read  -a U <<< `tr '-' '\n' <<< $1`
     C=`tr -d ':' <<< $2`

     D=`expr ${U[1]} - ${U[0]} - 1`

     if [ "$D" != "0" ]; then
	 (head -c ${U[0]} < /dev/zero ; echo -n $C; head -c $D < /dev/zero;echo "[^$C]") | tr '\0' '.' | sed 's/./^/' > tmp
	 (head -c ${U[0]} < /dev/zero ; echo -n "[^$C]"; head -c $D < /dev/zero;echo "$C") | tr '\0' '.' | sed 's/./^/' >> tmp
     else
	 (head -c ${U[0]} < /dev/zero ; echo -n $C; echo "[^$C]") | tr '\0' '.' | sed 's/./^/' > tmp
	 (head -c ${U[0]} < /dev/zero ; echo -n "[^$C]"; echo "$C") | tr '\0' '.' | sed 's/./^/' >> tmp
     fi
     
     echo $3 | grep -f tmp
}

(cat input | while read i; do
     x $i
done) | wc -l 
