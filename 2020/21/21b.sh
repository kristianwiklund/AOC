#!/bin/bash

# start by running part 1

echo -n "Part 1 answer: "
./21.sh $1
echo ""

# part 2

# tmp contains the list of all foods
# tmp7 contains the list of all foods without allergies
# hence, tmp11 becomes the list of all foods with allergies and tmp10 is a filter to remove foods without allergies from the input

grep -f tmp7 tmp | sed -e 's/\(.*\)/s#\1 ##/' > tmp10
grep -f tmp7 tmp  | sed -e 's/\(.*\)/s#\1$##/' >> tmp10
grep -v -f tmp7 tmp > tmp11
grep -f tmp11 $1 | sed -f tmp10 > $1.tmp

# slice the espresso file to get rid of everything except the foods with allergies
awk '{print "s#"$1"#[01]#"}'  < tmp7 > tmp12
awk '{print "s#"$1"#([01])#"}'  < tmp11 >> tmp12

(
    echo -n "s#^";
    sed -E -f tmp12 < tmp | tr -d '\n';
    c=1;
    echo -n "#"
    for i in `cat tmp11`; do
	echo -n "\\$c"
	let c=c+1
    done;
    echo "#"
) > tmp13

echo ".type fd" > tmp14
sed -E -f tmp13 < esp.result | sed -f tmp10 | sed 's/.i 7/.i 3/' | sed 's/.i 200/.i 8/'  >> tmp14
espresso tmp14 | tr '01' '10'







