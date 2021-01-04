#!/bin/bash

# count the encoded size

echo -n "Encoded size: "
ES=`cat $1 | grep -v "^$" | tr -d '\n' |  wc -c`
echo $ES

# decode

echo -n "Decoded size: "
cat $1 | grep -v "^$" | sed 's/^"\(.*\)"$/\1/' > bop
read DS < <(for i in `cat bop`; do printf $i; done | wc -c)

echo $DS

echo -n "Difference: "
expr $ES - $DS 
