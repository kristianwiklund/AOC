#!/bin/bash

IN=pp2.txt
python3 prop.py > $IN

echo "long int bop[] = {" > input2.h
head -n -1 $IN | sed 's/$/,/' >> input2.h
echo "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};" >> input2.h
echo -n "#define INPUT ">>input2.h
head -n -1 $IN | wc -l | cut -d ' ' -f 1 >> input2.h
echo -n "#define OFFSET ">>input2.h
tail -n -1 $IN >> input2.h

make 20b
./20b
