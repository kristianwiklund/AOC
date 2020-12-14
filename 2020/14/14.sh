#!/bin/sh
cat input  | (echo "from mem import Mem";echo "mem=Mem()";awk '/mask/ {print "mem.setmask(\""$3"\")"} /mem/ {print}';echo "print(sum(mem.values()))") > 14.py
python3 14.py

cat input  | (echo "from mem import Mem2";echo "mem=Mem2()";awk '/mask/ {print "mem.setmask(\""$3"\")"} /mem/ {print}';echo "print(sum(mem.values()))") > 14.py
python3 14.py
