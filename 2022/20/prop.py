with open("input.short","r") as fd:
    lines = fd.readlines()
    lines = [int(x.strip())*811589153 for x in lines]
#    lines = [int(x.strip()) for x in lines]
    bop = set()
#    print("max",max(lines))
#    print("min",min(lines))
    x = len(str(max(lines)))
    v= "10"+"0"*x
    v=int(v)
    
#    print("offset",v)
    for i in lines:
        while i in bop:
            i+=v if i>0 else -v
            
        bop.add(i)
        print(i)

    print(v)

    

