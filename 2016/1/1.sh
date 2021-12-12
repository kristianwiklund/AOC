#!/bin/sh

cat input | tr -d ' '| tr ',' '\n' | sed -e 's/R/R /' -e 's/L/L /' | awk -f 1.awk
