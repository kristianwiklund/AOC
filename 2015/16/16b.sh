#!/bin/sh

cat input | grep -v "children: [0-2,4-9]" | grep -v "cats: [2-7]" | grep -v "cats: 1[^0]" | grep -v "samoyeds: [0-1,3-9]" | grep -v "pomeranians: [4-9]" | grep -v "pomeranians: 10" | grep -v "akitas: [1-9]" | grep -v "vizslas: [1-9]"  | grep -v "goldfish: [6-9]" | grep -v "goldfish: 10" | grep -v "trees: [0,2]" | grep -v "trees: 1[^0]" | grep -v "cars: [0-1,3-9]" | grep -v "perfumes: [0,2-9]"
