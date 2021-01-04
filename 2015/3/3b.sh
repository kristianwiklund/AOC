#!/bin/bash

sed 's/\(.\)./\1/g' < $1 >input.santa
sed 's/.\(.\)/\1/g' < $1 >input.robosanta

./3a.sh input.santa
./3a.sh input.robosanta
