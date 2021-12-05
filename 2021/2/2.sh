#!/bin/bash

(sed -e 's/forward/x = x +/' -e 's/down/y =  y +/' -e 's/up/y = y -/';echo "x*y") | bc -l
