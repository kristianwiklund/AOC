#!/bin/bash

INPUT=input.txt

mkheader() {

    cat $INPUT | awk -F, 'BEGIN {x=0;y=0} {x=($1>x)?$1:x;y=($1>y)?$1:y} END {print "#define IMAXX "x"\n#define IMAXY "y}' > 6.h

    echo "#define SCALE $1" >> 6.h
    echo "#define MAXX (IMAXX*(2*SCALE+1)) // get some margins...
#define  MAXY (2*IMAXY*(SCALE+1))
char data[MAXY+1][MAXX+1];" >> 6.h
    echo "#define NRCOORD `wc -l $INPUT|cut -d ' ' -f 1`" >> 6.h
    echo "int cx[NRCOORD],cy[NRCOORD];" >> 6.h
    echo "void setup() { " >> 6.h

    cat $INPUT | awk -F, 'BEGIN {a=1} {print "data["$2"+SCALE*IMAXY]["$1"+SCALE*IMAXX] = 48+"a";";a=a+1} ' >> 6.h

    cat $INPUT | awk -F, 'BEGIN {a=0} {print "cx[ "a "]=(" $1 "+SCALE*IMAXX);cy[" a "]=(" $2 "+SCALE*IMAXY);"; a=a+1}' >> 6.h
    echo "}" >> 6.h
}

mkheader 2
rm -f 6
make 6
./6 > out.tmp
awk -vFS="" '{for(i=1;i<=NF;i++)w[$i]++}END{for(i in w) print i,w[i]}' out.tmp > 6a1.tmp

mkheader 10
rm -f 6
make 6
./6 > out.tmp
awk -vFS="" '{for(i=1;i<=NF;i++)w[$i]++}END{for(i in w) print i,w[i]}' out.tmp > 6a2.tmp

fgrep -f 6a1.tmp 6a2.tmp | sort -n -k 2

