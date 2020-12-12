#!/bin/sh

echo -n "A=";(sed 's/^\(.\)/\1 /' < input  | awk -f 12.awk|tail -1|cut -d ' ' -f3)
echo -n "B=";(sed 's/^\(.\)/\1 /' < input  | awk -f 12b.awk|tail -1|cut -d ' ' -f3)

