#!/bin/bash

export BC_LINE_LENGTH=10000
sed 's|!.||g' | sed 's|<[^>]*>||g' | sed 's|[^{}]||g' | sed 's/{/c=c+1;/g' | sed 's/}/print " ";print c;c=c-1;/g' | sed 's/^/print "\\n";c=0;/' | tr ';' '\n'| bc -l  | sed 's/^ *//' |  sed 's/$/\n/' |  sed 's| |\n.+|g' | bc -l| tail -1

