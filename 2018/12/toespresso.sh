#!/bin/bash

# http://www.ecs.umass.edu/ece/labs/vlsicad/ece667/links/espresso.5.html

INPUT=`basename $1 .txt`

echo ".i 5" > $INPUT.esp
echo ".o 1" >> $INPUT.esp
echo ".type fr" >> $INPUT.esp

cat $1|sed -e 's/ => / /' | tr '.#' '01' >> $INPUT.esp
espresso $INPUT.esp | fgrep -v . | tr '01-' '.#_'  > patterns.tmp
cat patterns.tmp  | awk -f patterns.awk  > matcher.erl
erlc matcher.erl

