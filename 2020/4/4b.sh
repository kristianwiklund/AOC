#!/bin/bash

cat input | sed ':a;N;$!ba;s/\([a-zA-Z0-9]\)\n/\1 /g' \
    | egrep "byr:(19[2-9][0-9]|200[0-2]) " \
    | egrep "iyr:(201[0-9]|2020) " \
    | egrep "eyr:(202[0-9]|2030) " \
    | egrep "hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in) " \
    | grep -E "hcl:#[0-9a-f]{6} " \
    | egrep "ecl:(amb|blu|brn|gry|grn|hzl|oth) " \
    | grep -E "pid:[0-9]{9} " | wc -l



