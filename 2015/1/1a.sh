#!/bin/sh

cat input.txt | sed -e 's/(/+1/g' -e 's/)/-1/g' -e 's/^/0/' | bc -l
