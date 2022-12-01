
elves = dict()
en=0

def readelf(fd):
    elf = list()
    x = fd.readline().strip()
    
    while x:
        if x=="":
            return elf
        elf.append(int(x))
        
        x = fd.readline().strip()

    return elf

fd = open("input.txt","r")

while fd:
    elf = readelf(fd)
    if len(elf):
        elves[en] = sum(elf)
        en=en+1
    else:
        break

# elves is a dict of elves and their inventory sum
    
print ("-",elves,"-")
maxelf = sorted(elves,key=lambda x:elves[x]).pop()
print ("Part 1:",maxelf, elves[maxelf])


