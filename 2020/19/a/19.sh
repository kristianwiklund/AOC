#!/bin/sh

echo "grammar ap;"> ap.g4
grep [0-9] $1 | sed 's/\([0-9][0-9]*\)/T\1/g' | sed 's/$/;/' >> ap.g4
antlr4 -Dlanguage=Python3 ap.g4
