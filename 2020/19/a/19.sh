#!/bin/sh

echo "grammar ap;"> ap.g4
echo "start: T0 '\\\n' {print(\"yay!\")};" >> ap.g4

grep [0-9] $1 | sed 's/\([0-9][0-9]*\)/T\1/g' | sed 's/$/;/' | tr '"' "'">> ap.g4
antlr4 -Dlanguage=Python3 ap.g4

(for i in `grep -v -e "[0-9]" -e "^$" $1`; do
     echo $i
    echo $i | python3 hello.py
 done) | tee tmp3

grep yay tmp3 | wc -l

