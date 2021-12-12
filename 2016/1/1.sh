#!/bin/sh

tr -d ' '| tr ',' '\n' | sed -e 's/R/R /' -e 's/L/L /' | awk -f 1.awk > /tmp/blahonga
echo -n "Answer 1: "
grep -v P /tmp/blahonga

grep P /tmp/blahonga > /tmp/bluhonga
rm -f /tmp/blahonga
sort /tmp/bluhonga  | uniq -c | grep -v "^ *1 " | sed 's/ *[0-9]* //' > /tmp/bohonga
grep -f /tmp/bohonga /tmp/bluhonga | head -1 | awk '{print "Answer 2:",sqrt($2*$2)+sqrt($3*$3)}'
rm -f /tmp/bohonga
rm -f /tmp/bluhonga
