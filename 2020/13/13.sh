#!/bin/bash

read -a A  < <(cat input | tr ',' '\n' | grep -v x | sed 's/^\(.*\)/-(1000510-(1000510\/\1)*(\1)-\1)/' | bc | tr '\n' ' ')

read -a B < <(cat input | tr ',\n' '  '|tr -d x | tr -s ' ')

let c=${#A[@]}-1
(for i in `seq 1 $c` ; do
    let G="${A[$i]} * ${B[$i]}"
    echo "${A[$i]} * ${B[$i]} = $G"
done) | sort -nr | tail -1 | cut -d ' ' -f5
