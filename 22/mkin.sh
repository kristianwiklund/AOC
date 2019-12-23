#!/bin/bash

echo "-module(input)."> input.erl
echo "-export([input/1])". >>input.erl
echo "input(D1)->" >> input.erl

awk -f awk.awk <  $1 | grep D >> input.erl
erlc input.erl

# reverse the input file
tac $1 > $1.tmp


echo "-module(rinput)."> rinput.erl
echo "-export([rinput/1])". >>rinput.erl
echo "rinput(D1)->" >> rinput.erl

awk -f rawk.awk <  $1.tmp | grep D >> rinput.erl
rm $1.tmp

erlc rinput.erl

echo "-module(tinput)."> tinput.erl
echo "-export([tinput/1])". >>tinput.erl
echo "tinput(D1)->" >> tinput.erl

awk -f tawk.awk <  $1 | grep D >> tinput.erl
erlc tinput.erl
