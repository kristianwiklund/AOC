#!/bin/bash

function f {

    dx=$1
    dy=$2
    f=$3
    x=0
    sx=`tail -1 $f|tr -d '\n'|wc -c`
    
    k=`sed -n "0~${dy}p"<$f|tr '\n' ' '`

    (for i in $k; do
	sed "s/.\{$x\}\(.\).*\$/\1/" <<<$i | grep "#"
	x=`expr $x + $dx `
	x=`expr $x % $sx`
    done) | wc -l
	     
    

}


# answer to problem 3/1
b=`f 3 1 input.short`
echo $b

a=`f 1 1 input.short`
# b done above
c=`f 5 1 input.short`
d=`f 7 1 input.short`
e=`f 1 2 input.short`

echo $a
echo $b
echo $c
echo $d
echo $e
