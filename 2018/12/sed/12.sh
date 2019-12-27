#!/bin/bash

INPUT=shortinput

echo "h"> sed.tmp
cat ${INPUT}_actions.txt | sed -e "s/ => /?/" -e "s/$/?g/" -e "s/^/s?/" -e "s/?#?/?\\\1#\\\2?/" -e "s/?-?/?\\\1-\\\2?/" -e "s/s?\(..\)\(.\)\(..\)/s?\\\\(\1\\\\)\2\\\\(\3\\\)/" -e "s/\./-/g" | sed 's/$/\np\ng/' >> sed.tmp


sed -f sed.tmp $INPUT.txt | sort -u | grep -v $INPUT.txt
