#!/bin/bash

IN=pp.txt
#python3 prop.py > $IN

echo "long int bop[] = {" > input.h
head -n -1 $IN | sed 's/$/,/' >> input.h
echo "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};" >> input.h
echo -n "#define INPUT ">>input.h
head -n -1 $IN | wc -l | cut -d ' ' -f 1 >> input.h
echo -n "#define OFFSET ">>input.h
tail -n -1 $IN >> input.h

make 20
./20
