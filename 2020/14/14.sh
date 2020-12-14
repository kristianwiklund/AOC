#!/bin/sh
#cat $1  | (echo "from mem import Mem";echo "mem=Mem()";awk '/mask/ {print "mem.setmask(\""$3"\")"} /mem/ {print}';echo "print(sum(mem.values()))") > 14.py
#python3 14.py

cat $1  | (echo "from mem import Mem2,sumzor";echo "mem=Mem2()";awk '/mask/ {print "mem.setmask(\""$3"\")"} /mem/ {print}';echo "#print (mem)";echo "print(sumzor(mem))") > 14.py
#cat $1  | (echo "from mem import Mem2,sumzor";echo "mem=Mem2()";awk '/mask/ {print "mem.setmask(\""$3"\")"} /mem/ {print}';echo "print(sumzor(mem))") > 14.py
python3 14.py

# 4124741710594 - too low
# 4124741710594

