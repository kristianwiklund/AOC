#!/bin/bash

echo -n "Task 1: "
(echo "0";for i in `cat input`; do (echo $i | tr 'x' '\n'|sort -n|tr '\n' ' '|awk '{print $1,$2,"*",$1,$3,"*",$2,$3,"*","+","+","2 *",$1,$2,"* + +"}'); done; echo "p") | dc
echo -n "Task 2: "
(echo "0";for i in `cat input`; do (echo $i | tr 'x' '\n'|sort -n|tr '\n' ' '|awk '{print $1,$1,"+",$2,$2,"+",$1,$2,$3,"* * + + +"}'); done; echo "p") | dc
