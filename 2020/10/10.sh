#/!bin/sh

cat input | sort -n | awk 'BEGIN {pre=0} {print $1-pre;pre=$1}'  | sort | uniq -c | awk '{print $1}' | tr '\n' ' ' | awk '{print $1*($2+1)}'

