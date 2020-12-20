
def read(f):
    # parse one tile

    h = f.readline()
    h = h.strip('\n\r:')
    myid = int(h.split()[1])

    A = list()
    # then read the 10 lines
    for i in range(0,10):
        A.append(f.readline().strip('\n\r').replace("#","1").replace(".","0"))

    # process a signature for each tile
    top = int(A[0],2)
    bottom = int(A[9],2)
    left = int("".join([x[9] for x in A]),2)
    right = int("".join([x[0] for x in A]),2)

    # and discard final empty line
    f.readline()
    
    return (myid, top,bottom,left,right)

with open("input.short","r") as fd:
    pics = list()
    try:
        while True:
            pics.append(read(fd))
    except:
        pass

    print(pics)





    
