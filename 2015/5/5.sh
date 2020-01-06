#!/bin/bash

echo "Part 1:"
cat input.txt | grep "[aeiou].*[aeiou].*[aeiou]" | grep "\(.\)\1" | egrep -v "ab|cd|pq|xy" | wc -l

echo "Part 2:"
cat input.txt | grep "\(..\).*\1" | grep "\(.\).\1" | wc -l
