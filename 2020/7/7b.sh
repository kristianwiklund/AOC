#!/bin/bash

cat $1 | tr -d '.' |sed 's/contain no other bags/1/' | tr ',' '+' > tmp3

function l() {
    
    cat $1 | grep -v contain | sed 's/bags/bag/' | sed "s/\(.* .* .*\) \(.*\)/s#\1s*#*\2#/"

    # | cut -d ' ' -f 1-3 | sed 's/bags/bag/' | sed 's#\(.*\)#s/\1/shiny gold bag/#'  > tmp
}

l tmp3 > pattern
sed -f pattern < tmp3  | grep -v ^*
