
def readone(f):
    # parse one tile

    h = f.readline()
    h = h.strip('\n\r:')
    myid = int(h.split()[1])

    A = list()
    # then read the 10 lines
    for i in range(0,10):
        A.append(f.readline().strip('\n\r').replace("#","1").replace(".","0"))


    # process a signature for each tile

    ll = "".join([x[9] for x in A])
    lr = "".join([x[0] for x in A]) 
    
    top = int(A[0],2)
    bottom = int(A[9],2)
    left = int(ll,2)
    right = int(lr,2)

    rtop = int(A[0][::-1],2)
    rbottom = int(A[9][::-1],2)
    rleft = int(ll[::-1],2)
    rright = int(lr[::-1],2)
    
    # and discard final empty line
    f.readline()
    
    return (myid, top,bottom,left,right,rtop,rbottom,rleft,rright)

def fliphoriz(tile):

    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (myid, rtop, rbottom, right, left, top, bottom, rright, rleft)

def flipvert(tile):

    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (myid, top, bottom, rleft, rright, rtop, rbottom, left, right)

def rot90(tile):
    (myid, top,bottom,left,right,rtop,rbottom,rleft,rright) = tile

    return (myid, left, right, rtop,rbottom,rleft,rright, top ,bottom)

def rot180(tile):

    return(rot90(rot90(tile)))

def rot270(tile):

    return(rot90(rot180(tile)))

def getpix(fname):
    with open(fname,"r") as fd:
        pics = list()
        try:
            while True:
                pics.append(readone(fd))
        except:
            pass

        return pics


hl = getpix("input.short")

#print(hl[0])
#print(rot90(rot270(hl[0])))









    
