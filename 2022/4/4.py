
with open("input.txt","r") as fd:
    lines = fd.readlines()

    cnt=0
    cnt2=0
    for line in lines:
        ep = line.strip().split(",")
        a1,a2=[int (x) for x in ep[0].split("-")]
        b1,b2=[int (x) for x in ep[1].split("-")]

        sa = set(range(a1,a2+1))
        sb = set(range(b1,b2+1))

        cnt += sa.issubset(sb) or sb.issubset(sa)
        cnt2 += not sa.isdisjoint(sb)

    print("Part 1:",cnt)
    print("Part 2:",cnt2)

    
