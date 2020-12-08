#!/bin/bash

(cat template.sh
cat input.b | tr -d '+' | awk -f 8.awk
cat template2.sh) > tmp
bash -f tmp
