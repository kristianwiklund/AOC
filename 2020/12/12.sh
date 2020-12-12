#!/bin/sh

#sed 's/^\(.\)/\1 /' < input  | awk -f 12.awk
sed 's/^\(.\)/\1 /' < input.short  | awk -f 12b.awk
