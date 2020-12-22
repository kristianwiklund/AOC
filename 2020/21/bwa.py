#!/usr/bin/python3
import sys

with open(sys.argv[1],"r") as fd:

    a = fd.readline().strip("\n\r").split(" ")[0]
    l = len(a)
    a=int(a,2)

    while True:
        b = fd.readline()
        b = b.rstrip()

        if not b:
            break

        b = int(b.strip("\n\r").split(" ")[0],2)
        a=a&b

    print (format(a,"0"+str(l)+"b"))

