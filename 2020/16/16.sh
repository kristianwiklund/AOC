#!/bin/bash

echo "def check(x):" > tmp.py
echo -n "    return " >> tmp.py
cat $1 | cut -d: -f2 | sed -e 's/or//' -e 's/^ //' | tr -s ' ' | grep -- -| awk -f 16.awk >> tmp.py
echo "    False" >> tmp.py

awk '/nearby tickets:/ {f=1} {if(f==1) print ($0)}' < $1 | tail +2 | python3 16.py 
