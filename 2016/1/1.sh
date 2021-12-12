#!/bin/sh

tr -d ' '| tr ',' '\n' | sed -e 's/R/R /' -e 's/L/L /' | awk -f 1.awk > /tmp/blahonga
echo -n "Answer 1: "
grep -v P /tmp/blahonga
rm -f /tmp/blahonga
