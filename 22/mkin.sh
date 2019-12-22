#!/bin/bash

echo "-module(input)."> input.erl
echo "-export([input/1])". >>input.erl
echo "input(D1)->" >> input.erl

awk -f awk.awk <  $1 | grep D >> input.erl
erlc input.erl

