#!/usr/bin/awk -f 
BEGIN {p=100000} $1>p {c++} {p=$1} END {print c}
