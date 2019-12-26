#!/bin/sh
tr -d "+" < input.txt > input.tmp
cat input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp input.tmp > input2.tmp
cat input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp input2.tmp > input3.tmp

cat input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp input3.tmp | awk -f calc.awk 

