#!/bin/bash

echo 'for i in `seq 0 999` ; do for j in `seq 0 999`; do arr[$i*1000+$j]=0; done; done' > tmp

cat $1 | tr ',' ' ' | sed -e 's/through//' -e 's/turn on/turnon/' -e 's/turn off/turnoff/' | awk '/turnon/ {k="let arr[$i*1000+$j]+=1"} /turnoff/ {k="let arr[$i*1000+$j]=arr[$i*1000+$j]?arr[$i*1000+$j]-1:0"} /toggle/ {k="let arr[$i*1000+$j]+=2"} {c=c+1;print ">&2 echo",c,";for i in `seq",$2,$4"`; do for j in `seq",$3,$5"`; do "k"; done; done" }' >> tmp
echo 'echo ${arr[@]} | tr " " "\n" | sort | uniq -c | sed "s/$/ * +/"' >> tmp
(echo "0";source tmp;echo "p") | dc
