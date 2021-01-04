#!/bin/bash

cp $1 $1.tmp
cat $1| cut -d' ' -f1|sort -u | sed 's/^/Me would gain 0 happiness units by sitting next to /' >> $1.tmp
cat $1| cut -d' ' -f1|sort -u | sed 's/$/ would gain 0 happiness units by sitting next to Me/' >> $1.tmp

./13.sh $1.tmp
