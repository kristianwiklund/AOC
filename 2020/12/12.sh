#!/bin/sh

sed 's/^\(.\)/\1 /' < input  | awk -f 12.awk
