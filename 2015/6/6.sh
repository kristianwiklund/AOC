#!/bin/bash

echo 'for i in `seq 0 999` ; do for j in `seq 0 999`; do arr[$i*1000+$j]=0; done; done' > tmp

cat $1 | tr ',' ' ' | sed -e 's/through//' -e 's/turn on/turnon/' -e 's/turn off/turnoff/' | awk '/turnon/ {k="arr[$i*1000+$j]=1"} /turnoff/ {k="arr[$i*1000+$j]=0"} /toggle/ {k="let p=1-arr[$i*1000+$j];arr[$i*1000+$j]=$p"} {c=c+1;print "echo",c,";for i in `seq",$2,$4"`; do for j in `seq",$3,$5"`; do "k"; done; done" }' >> tmp
echo 'echo ${arr[@]} | tr " " "\n" | sort | uniq -c' >> tmp
source tmp
