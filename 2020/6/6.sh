#!/bin/bash

sed ':a;N;$!ba;s/\([a-zA-Z0-9]\)\n/\1/g' < input |while read j; do (while read -n 1 i ; do echo $i; done|sort -u|tr -d '\n') <<< $j; done | wc -c



