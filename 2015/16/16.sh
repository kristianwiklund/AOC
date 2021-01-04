#!/bin/sh

cat input | grep -v "children: [0-2,4-9]" | grep -v "cats: [0-6,8-9]" | grep -v "samoyeds: [0-1,3-9]" | grep -v "pomeranians: [0-2,4-9]" | grep -v "akitas: [1-9]" | grep -v "vizslas: [1-9]"  | grep -v "goldfish: [0-4,6-9]" | grep -v "trees: [0-2,4-9]" | grep -v "cars: [0-1,3-9]" | grep -v "perfumes: [0,2-9]"
