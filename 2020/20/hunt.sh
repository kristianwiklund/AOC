#!/bin/bash

function f() {
    cat $1 | tr -d "\n" > flat

#echo $BOP
# without monster

    # the sed fails since it has more than 9 backrefernces
    echo "" >s2
    echo "--- sea ---">>s2
    cat flat | ./notsed.py "$BOP" | sed -E "s/(.{96})/\1\n/g" | grep -v '^$' >>s2
#    echo $1
   cat flat | ./notsed.py "$BOP" | sed 's/\(.\)/\1\n/g' | sort | uniq -c | grep "#"

# 2443 is too high
}
#echo "Hunting the monster"
sed -e '1,/--- sea ---/ d' | tr '01' ' #' > sea
#cat sea | rev > searev
#./rot.py < sea > searot
#cat searot | rev > searotrev
#./rot.py < searev > searevrot
#cat searot | ./rot.py > searotrot
#cat searotrot | ./rot.py > searotrotrot
#cat searotrot | rev > searotrotrev

# searotrev is the match in the example btw

MAX=`cat sea | wc -l`
let MAX+=8
echo $MAX

# to get the monsters to the right place, we need to put them on MAX characters distance _start to start_"
M1="#(."
M2=")#(....)##(....)##(....)###("
M3=".)#(..)#(..)#(..)#(..)#(..)#"
M2x=`printf %${MAX}s $M2 | tr ' ' '.'` #24 + number of (
#M2x=`printf %104s $M2 | tr ' ' '.'` #24 + number of (
M3x=`printf %${MAX}s $M3 | tr ' ' '.'` #21 +number of (
#M3x=`printf %104s $M3 | tr ' ' '.'` #21 +number of ( 
BOP="($M1$M2x$M3x)"

#f searotrot
#f searotrotrot
#f searotrotrev
#f searevrot
f sea>/dev/null
f s2>/dev/null
f s2>/dev/null
f s2
#f searot
#f searotrev
