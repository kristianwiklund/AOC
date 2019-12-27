#!/bin/bash
IFS=$'\n'

rm -f input.tmp

# sort in time order
for i in `cat shortinput.txt`;do

    X=`echo $i | cut -d] -f1| tr -d '['`
    echo `date --date=$X +%s` `echo $i| cut -d "]" -f2`| tr -s " " >> input.tmp

done

rm -f processed.tmp

# extract the sleeping periods and sort per guard
for i in `sort -n input.tmp`;do

    X=`echo $i | cut -d " " -f1`
    echo `date --date=@$X +"%m-%d %M"` `echo $i|cut -d " " -f2-` >> processed.tmp
done

awk -f 4.awk < processed.tmp | tr -d "#" > combined.tmp

# strategy 1: which guard have the most sleepy time
worstguard=`awk '{guard[$1]=guard[$1]+$2} END {for (i in guard) {print guard[i],i}}' < combined.tmp | sort -n  | tail -1| cut -d ' ' -f2`
echo -n "the worst guard is $worstguard, sleeping "

(grep "^$worstguard" combined.tmp| cut -d ' ' -f4,7 | sed 's/^/seq /' | bash) | sort | uniq -c | sort -n | tail -1 | tr -s " " | sed -e 's/^ //' -e 's/ / times on minute /'








