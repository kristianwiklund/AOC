#!/bin/bash

sed ':a;N;$!ba;s/\([a-zA-Z0-9]\)\n/\1 /g' < input > tmp

# of persons per group
mapfile -t C < <(cat tmp | while read i; do tr -d 'a-z'<<<$i | wc -c; done)

cnt=0
sed ':a;N;$!ba;s/\([a-zA-Z0-9]\)\n/\1/g' < input |while read j; do
    (while read -n 1 i ;do
	 echo $i;
     done) <<< $j | grep -v "^$" | sort | uniq -c | sort -nr | grep ${C[$cnt]}|wc -l
    let cnt++
    done |paste -sd+ | bc







