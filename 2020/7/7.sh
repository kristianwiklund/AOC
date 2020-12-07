#!/bin/bash

function k() {
    cat $1 | grep "[0-9] shiny gold" | cut -d ' ' -f 1-3 | sed 's/bags/bag/' | sed 's#\(.*\)#s/\1/shiny gold bag/#'  > tmp
    sed -f tmp < $1 > $2
}

rm -f tmp2
touch tmp2
cp input tmp3

until diff tmp2 tmp3 > /dev/null; do
    echo bopp
    mv tmp3 tmp2
    k tmp2 tmp3
done


grep "[0-9] shiny gold" tmp3  | wc -l
