#!/bin/sh

#echo "Hunting the monster"
sed -e '1,/--- sea ---/ d' | tr '01' ' #' > sea
cat sea | rev > searev
./rot.py < sea > searot
cat searot | rev > searotrev

# searotrev is the match in the example btw

MAX=`tail -1 sea | wc -c`

# to get the monsters to the right place, we need to put them on MAX characters distance _start to start_"
M1="#(."
M2=")#(....)##(....)##(....)###("
M3=".)#(..)#(..)#(..)#(..)#(..)#"
M2x=`printf %104s $M2 | tr ' ' '.'` #24 + number of (
M3x=`printf %104s $M3 | tr ' ' '.'` #21 +number of ( 

cat sea | tr -d "\n" > flat
BOP="($M1$M2x$M3x)"
#echo $BOP
# without monster

# the sed fails since it has more than 9 backrefernces
cat flat | ./notsed.py "$BOP" | sed -E "s/(.{96})/\1\n/g" 
cat flat | ./notsed.py "$BOP" | sed 's/\(.\)/\1\n/g' | sort | uniq -c

# 2443 is too high
