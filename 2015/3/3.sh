#!/bin/bash

echo -n "Part 1: "
./3a.sh input | sort -u | wc -l

echo -n "Part 2: "
./3b.sh input | sort -u | wc -l


