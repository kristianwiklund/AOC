#!/bin/bash

grep [0-9] $1 > tmp2
rm -f tmp
touch tmp

function f() {

    grep [ab] tmp | tr -d '":'| awk '{s = ""; for (i = 2; i <= NF; i++) s = s $i " ";print "s/ "$1" / ( "s") /g";print "s/ "$1"$/ ( "s") /g"}' | sed -e 's/( a )/a/g' -e 's/( b )/b/g' > rules
    sed -f rules < tmp > tmp2
}

until diff tmp tmp2 > /dev/null; do
    mv tmp2 tmp
    echo "invoking translator"
    f x
    echo "done translating"

done

echo "done looping"
#f
#mv tmp2 tmp
#f
#mv tmp2 tmp
#f
#mv tmp2 tmp
#f
echo "--"
cat tmp | grep "^0:"  | tr -d ' ' | cut -d: -f2 | awk '{print "^"$0"$"}' | sed -e 's/(a)/a/g' -e 's/(b)/b/g' | sed 's/(\([^|]\))/\1/g' > rules2
cat rules2 |   sed 's/[(]/(?:/g' | sed -e 's/ax/)/' -e 's/xa/(/' > rules3
cat rules3 | sed 's/bobarob/\\1/' | tr -d "'" > rules2
grep -P -f rules2 $1  | wc -l
grep 1 rules2
