#!/bin/bash

rm -f tmp
(cat template.sh
cat $1 | tr -d '+' | awk -f 8.awk
cat template2.sh) > tmp
bash -f tmp
rm -f tmp
