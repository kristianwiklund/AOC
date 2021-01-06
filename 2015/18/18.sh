#!/bin/sh

echo "char *input[] = {" > input.h
cat $1 | sed -e's/^/"/' -e 's/$/",/' >> input.h
echo "};" >> input.h

S=`wc -l < $1`
echo "#define XMAX $S" >> input.h
echo "#define YMAX $S" >> input.h

make
./life
