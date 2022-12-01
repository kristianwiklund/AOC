import sys
sys.path.append("..")

from utilities import *

elves = dict()
en=0

fd = open("input.txt","r")

while fd:
    elf = readblock(fd)
    if len(elf):
        elves[en] = sum(elf)
        en=en+1
    else:
        break

# elves is a dict of elves and their inventory sum
    
#print ("-",elves,"-")
maxelf = sorted(elves,key=lambda x:elves[x]).pop() # this takes the last elf in the list (the one with the highest content)
print ("Part 1:", elves[maxelf])

topthree = sorted(elves,key=lambda x:elves[x],reverse=True)[:3]
p = 0
for i in topthree:
    p=p+elves[i]

print ("Part 2:", p)



