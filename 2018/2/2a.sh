#!/bin/bash

rm -f foo.tmp

while IFS= read -r line
      do 
	  t=`echo $line | sed 's/\(.\)/\1\n/g' | sort | uniq -c | egrep '(2|3)' | tr -d '\n' | tr -d ' '`
	  echo $line " " $t >> foo.tmp
done < input.txt
two=`grep 2 foo.tmp | wc -l`
three=`grep 3 foo.tmp | wc -l`
echo $(($two * $three))
