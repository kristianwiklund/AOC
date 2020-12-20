
def read(f):
    # parse one tile

    h = readline(f)
    f.strip('\n\r:')
    myid = int(line.split[1])

    A = list()
    # then read the 10 lines
    for i in range(0.10):
        A.append.readline(f).strip('\n\r').replace("#","1").replace(".","0")

    # process a signature for each tile
    top = int(A[0],2)
    bottom = int(A[9],2)
    left = int([x[9] for x in A],2)
    right = int([x[0] for x in A],2)

    return (id, top,bottom,left,right)

fd = open("input.short","r")
print(read(fd))
    
    
