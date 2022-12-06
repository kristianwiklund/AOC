
def checkseq(line):
    cnt=0
    while len(line)>=4:
        seq = line[:4]
        
        if len(set(seq))==4:
            return cnt+4
        line = line[1:]
        cnt=cnt+1

    return -1

def checkseq2(line):
    cnt=0
    while len(line)>=4:
        seq = line[:14]
        
        if len(set(seq))==14:
            return cnt+14
        line = line[1:]
        cnt=cnt+1

    return -1
    
with open("input.txt","r") as fd:

    lines = fd.readlines()
    for line in lines:
        print("part 1:", checkseq(line), line)
        print("part 2:", checkseq2(line), line)
        

    
            
        
        
