#!/bin/bash

cat smallinput.txt | awk -F, 'BEGIN {x=0;y=0} {x=($1>x)?$1:x;y=($1>y)?$1:y} END {print "#define IMAXX "x"\n#define IMAXY "y}' > 6.h

echo "#define MAXX (IMAXX*5) // get some margins...
#define MAXY (IMAXY*5)
char data[MAXY+1][MAXX+1];
char newdata[MAXY][MAXX+1];" >> 6.h

echo "void setup() { " >> 6.h


cat smallinput.txt | awk -F, 'BEGIN {a=1} {print "data["$2"+2*IMAXY]["$1"+2*IMAXX] = 48+"a";";a=a+1}' >> 6.h

echo "}" >> 6.h
