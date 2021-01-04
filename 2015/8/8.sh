#!/bin/bash

ES=`cat $1 | grep -v "^$" | tr -d '\n' |  wc -c`

cat $1 | grep -v "^$" | sed 's/^"\(.*\)"$/\1/' > bop
read DS < <(for i in `cat bop`; do printf $i; done | wc -c)

echo -n "Answer 1: "
expr $ES - $DS

read PC < <(for i in `cat $1`; do printf "\"%q\"" "$i" ; done| wc -c)


echo -n "Answer 2: "
expr $PC - $ES
