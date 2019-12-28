#!/bin/bash

INPUT=input

echo "h"> sed.tmp
cat ${INPUT}_actions.txt | sed -e "s/ => /?/" -e "s/$/?g/" -e "s/^/s?/" -e "s/?#?/?\\\1#\\\2?/" -e "s/?-?/?\\\1-\\\2?/" -e "s/s?\(..\)\(.\)\(..\)/s?\\\\(\1\\\\)\2\\\\(\3\\\)/" -e "s/\./-/g" | sed 's/$/\np\ng/' >> sed.tmp


sed -f sed.tmp $INPUT.txt | sort -u | grep -v -f $INPUT.txt > tmp.tmp

#sed "s/^\(.\{7\}\)./\1-/"

rm -f sed2.tmp

for i in `cat tmp.tmp`; do
    echo $i | cmp -l $INPUT.txt - 
    echo $i | cmp -l $INPUT.txt - | awk '{printf("s/^\\(.\\{%d\\}\\)./\\1%c/\n",$1-1,strtonum("0"$3))}' >> sed2.tmp

    #| awk '{print "s/^\\(.\\{"$5-1"\\}\\)./\\1"$12"/"}' >>sed2.tmp
done

cat $INPUT.txt | sed -f sed2.tmp

