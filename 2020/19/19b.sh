#!/bin/bash

grep [0-9] $1 | grep -v "^8:" | grep -v "^11:"> tmp2
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

echo "done looping -all but 8 and 11 are done"

grep [0-9] $1 | egrep "^0:|^8:|^11:" | sed -f rules > tmp2


echo "--"
cat tmp | grep "^0:" | tr -d ' ' | cut -d: -f2 | awk '{print "^"$0"$"}' > rules2
egrep -f rules2 $1 | wc -l
