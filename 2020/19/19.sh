#!/bin/bash

grep [0-9] $1 > tmp2
rm -f tmp
touch tmp

function f() {

    grep [ab] tmp | tr -d '":'| awk '{s = ""; for (i = 2; i <= NF; i++) s = s $i " ";print "s/ "$1" / ( "s") /g";print "s/ "$1"$/ ( "s") /g"}' > rules
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
cat tmp | grep "^0:" | tr -d ' ' | cut -d: -f2 | awk '{print "^"$0"$"}' > rules2
egrep -f rules2 $1 | wc -l
