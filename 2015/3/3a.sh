#!/bin/bash

echo -n "Part 1: "
(DX[1]=1
DX[2]=-1
DX[3]=0
DX[4]=0
DY[1]=0
DY[2]=0
DY[3]=1
DY[4]=-1
X=0
Y=0
echo $X $Y
sed 's/\(.\)/\1\n/g' < input  | tr '<>^v' '1234' | while read a; do let X=$X+${DX[$a]}; let Y=$Y+${DY[$a]}; echo $X $Y; done) | sort -u | wc -l
