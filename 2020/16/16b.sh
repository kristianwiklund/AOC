#!/bin/sh

echo "def check(x):" > tmp.py
echo "    l=list()" >> tmp.py
cat $1| sed -e 's/or//' -e 's/^ //' | tr -s ' ' | grep -- - | tr -d ':' | awk -f 16b.awk >> tmp.py
echo "    return l" >> tmp.py

awk '/nearby tickets:/ {f=1} {if(f==1) print ($0)}' < $1 | tail +2 | python3 16b.py 

