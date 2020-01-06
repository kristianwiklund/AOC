#!/bin/bash

cat input.txt | grep "[aeiou].*[aeiou].*[aeiou]" | grep "\(.\)\1" | egrep -v "ab|cd|pq|xy" | wc -l
