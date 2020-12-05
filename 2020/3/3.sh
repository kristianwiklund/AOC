#!/bin/bash

function f {

    dx=$1
    dy=$2
    f=$3
    x=0
    sx=`tail -1 $f|tr -d '\n'|wc -c`

    if [ $dy -gt 1 ]; then

	k=`(head -1 $f;tail -n +1 $f)|sed -n "0~${dy}p"|tr '\n' ' '`
    else
	k=`sed -n "0~${dy}p"<$f|tr '\n' ' '`
    fi

    (for i in $k; do
	sed "s/.\{$x\}\(.\).*\$/\1/" <<<$i | grep "#"
	x=`expr $x + $dx `
	x=`expr $x % $sx`
    done) | wc -l
	     
    

}


# answer to problem 3/1
b=`f 3 1 input`
echo "A=$b"

a=`f 1 1 input`
# b done above
c=`f 5 1 input`
d=`f 7 1 input`
e=`f 1 2 input`

echo -n "B="
echo "$a * $b*$c* $d* $e" | bc

