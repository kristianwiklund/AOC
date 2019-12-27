#!/bin/bash

rm -f sed.tmp

for i in {a..z}; do
    echo "s/$i${i^^}//g" >> sed.tmp
    echo "s/${i^^}$i//g" >> sed.tmp
done


cp input.txt input.tmp

i=-1
j=0

while [ "$i" -ne "$j" ]; do
    i=$j
    sed -f sed.tmp < input.tmp > apa.tmp
    mv apa.tmp input.tmp
    j=`wc -c input.tmp|cut -d ' ' -f 1`
    echo $j
done

cat input.tmp | tr -d " \n" | wc -c

# part 2

rm -f result.tmp

for l in {a..z}; do

    echo "$l"
    cat input.txt | tr -d " \n$l${l^^}" > input.tmp
    
    i=-1
    j=0

    while [ "$i" -ne "$j" ]; do
	i=$j
	sed -f sed.tmp < input.tmp > apa.tmp
	mv apa.tmp input.tmp
	j=`wc -c input.tmp|cut -d ' ' -f 1`
    done

    echo "$j $l" >> result.tmp
    
done

sort -rn result.tmp | tail -1
