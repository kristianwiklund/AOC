#!/bin/bash

(sed -e 's/forward \([0-9]*\)/ x = x + \1;y=y+a*\1/' -e 's/down/a =  a +/' -e 's/up/a = a -/';echo "x*y") | bc -l
