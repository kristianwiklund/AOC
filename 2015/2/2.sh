#!/bin/bash

(echo "0";for i in `cat input`; do (echo $i | tr 'x' '\n'|sort -n|tr '\n' ' '|awk '{print $1,$2,"*",$1,$3,"*",$2,$3,"*","+","+","2 *",$1,$2,"* + +"}'); done; echo "p") | dc
