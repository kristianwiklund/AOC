#!/bin/bash

# run mutations on the input
F=$1
rm -f tmp*

function mutate() {
    c=0
    p=$1

    (while read i; do

	 if (( c == p )); then
	     echo $i | awk '/nop/ {m=1;print "jmp",$2} /jmp/ {m=1;print "nop",$2} END{ if (m==0) print $0;}'  
	 else
	     echo "$i"
	 fi
	
	 let c++
	 done) < $F


}

max=`wc -l $F|cut -d' ' -f1`
echo "Running $max mutations"
cnt=0
tcnt=1



while (( cnt < max )); do

    mutate $cnt > tmp2

    if diff tmp2 $F > /dev/null; then
	echo "Skipping $cnt"
    else
	diff tmp2 $F | tr '\n' ' '
	echo -n " "
	echo -n "Running test $tcnt for $cnt - "
	if bash -f ./8.sh tmp2 > logg ; then
	    echo -n ""
	else
	    echo ""
	    cat logg
	    exit
	fi
	let tcnt++
	if grep "Crash" logg > /dev/null; then
	    tail -1 logg
	else
	    echo ""
	    cat logg
	    exit
	fi
	
    fi

    let cnt++

done


    
