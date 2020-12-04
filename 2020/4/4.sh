#!/bin/bash

cat input | sed ':a;N;$!ba;s/\([a-zA-Z0-9]\)\n/\1/g' | grep byr | grep iyr | grep eyr | grep hgt | grep hcl  | grep ecl | grep pid | wc -l
