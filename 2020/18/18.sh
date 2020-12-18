#!/bin/bash

# idea: parse the input with sed or something, generate a file for dc to process...
# the examples are done backwards:
# 1+2*3+4*5+6 becomes 6 5 4 3 2 1 + * + * + in RPN
#echo -n "Example: 1+2*3+4*5+6 = "
#echo "6 5 4 3 2 1 + * + * + p" | dc

# how to handle the ()?
# each () signifies that the stuff in it need to be handled as a separate chain of calculations

#echo -n "Example: 1 + (2 * 3) + (4 * (5 + 6)) = "
#echo "6 5 + 4 * 3 2 * + 1 + p" | dc


function cs() {
    # simple fulkod without () +
    T=$1
    EXP=`echo $T|tr  '[0-9]' ' '`
    NUM=`echo $T|tr  '+*' '  '|rev`
    echo "$NUM $EXP"
}

#echo -n "Example: 1+2*3+4*5+6 = "
#(cs "1+2*3+4*5+6";echo " p") | dc

# idea: break the string at () then run each part as above
#read -a X < <(echo "1 + (2 * 3) + (4 * (5 + 6))"|rev|tr -d ' '|tr '()' '  ' )

# this almost work, but it doesn't descend properly if we have ((
function c {

 read -a X < <(echo "$@"|tr '(' '\n'  | tac | tr -d ') '|tr '\n' ' '  )
 echo ${X[@]}
 (for i in `seq 0 ${#X[@]}`; do
      cs `echo ${X[$i]}`
  done; echo "p")
}

#c "1 + (2 * 3) + (4 * (5 + 6))"
#c "2 * 3 + (4 * 5)"
#c "5 + (8 * 3 + 9 + 3 * 4 * 3)"
#c "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
c "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"



