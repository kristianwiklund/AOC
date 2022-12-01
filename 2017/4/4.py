
def checkpass(line):
    t = dict()
    for x in line.split(" "):
        if x in t:
            return False
        t[x]=x
        
    return True


def checkpass2(line):
    t = dict()
    for x in line.split(" "):
        x = "".join(sorted(x))
        if x in t:
            return False
        t[x]=x
        
    return True

with open("input.txt") as fd:
    lines = fd.readlines()
    valid = 0
    valid2 = 0
    for line in lines:
        line=line.strip()
        if checkpass(line):
            valid = valid + 1
        if checkpass2(line):
            valid2 = valid2 + 1
            
print("Part 1:",valid)
print("Part 2:",valid2)



            
        
