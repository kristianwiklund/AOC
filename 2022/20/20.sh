#!/bin/bash

IN=$1

echo "int bop[] = {" > input.h
cat $IN | sed 's/$/,/' >> input.h
echo "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};" >> input.h
echo -n "#define INPUT ">>input.h
wc -l $IN | cut -d ' ' -f 1 >> input.h
make 20
./20
