#!/bin/sh

echo "Hunting the monster"
sed -e '1,/--- sea ---/ d' | tr '01' ' #' > sea
cat sea | rev > searev
./rot.py < sea > searot
cat searot | rev > searotrev


