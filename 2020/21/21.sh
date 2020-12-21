#!/bin/bash

cat $1 | sed 's/contains //g' | python3 21.py 
