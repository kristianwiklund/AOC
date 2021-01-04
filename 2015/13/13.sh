#!/bin/bash

echo "def b(G):" > bop.py
read MIN < <(cat $1  | sed -e 's/gain//' -e 's/lose /-/' | tr -d '.' | tr -s ' '  | cut -d ' ' -f3 | sort -nr | tail -1)
echo " MIN=$MIN" >> bop.py

cat $1  | sed -e 's/gain//' -e 's/lose /-/' | tr -d '.' | awk '{print " G.add_edge(\""$1"\",\""$NF"\",weight="$3"-MIN+MIN)"}' >> bop.py
echo ""

read N < <(cat $1| cut -d' ' -f1|sort -u| wc -l)

echo "def corr(): " >> bop.py
echo " return ($MIN*$N)" >> bop.py

echo -n "Answer: "
./13.py





