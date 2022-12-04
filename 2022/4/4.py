
with open("input.txt","r") as fd:
    lines = fd.readlines()

    cnt=0
    cnt2=0
    for line in lines:
        ep = line.strip().split(",")
        a=[int (x) for x in ep[0].split("-")]
        b=[int (x) for x in ep[1].split("-")]

        sa = set(range(a[0],a[1]+1))
        sb = set(range(b[0],b[1]+1))

        if sa.issubset(sb) or sb.issubset(sa):
            cnt=cnt+1

        if not sa.isdisjoint(sb):
            cnt2=cnt2+1
        
        
    print("Part 1:",cnt)
    print("Part 2:",cnt2)

    
