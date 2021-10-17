#!/usr/bin/python3

with open("input","r") as fd:
    x = fd.read()
    fd.close()

s=0

for i in range(len(x)):
    if x[i] == x[(i+int(len(x)/2))%len(x)]:
        s+=int(x[i])

print(s)
