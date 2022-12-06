#!/bin/sh

I=input.txt

cut -d' ' -f1 $I | sort -u | awk '{print $1"=0"}' > gen.py
echo "m=0">>gen.py
cat $I  | sed -e 's/dec/-/' -e 's/inc/+/' | awk '{print $1"=("$0,"else",$1")";print "m=max(m,"$1")"}' >> gen.py
echo -n "print(\"Part 1\",max(" >> gen.py
cut -d' ' -f1 $I | sort -u | tr '\n' ',' >> gen.py
echo "))">>gen.py
echo "print(\"Part 2\",m)">>gen.py
python3 gen.py
