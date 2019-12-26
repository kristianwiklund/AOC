#!/bin/sh
(tr -d '\n' < input.txt;echo "") | sed 's/^+//' | bc 
