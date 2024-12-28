import math

def steps(x):

    if x==1:
        return 0
    
    # find which dimension the outer rim is
    a = math.sqrt(x)
    b = math.floor(a)
    c = b+1
    
    # we are always at least math.floor(c/2) steps out
    # then we can find the location by checking with div and mod
    
    toedge = math.floor(c/2)

    # idiot version

    arr = list(range(x-(c*(x//c)), x-(c*(x//c))+c))
    print(arr)
    return 1

print ("x,c,toedge,div,mod")

# middle
assert(steps(1)==0)

# middles
assert(steps(2)==1)
assert(steps(4)==1)
assert(steps(6)==1)
assert(steps(8)==1)

# corners

assert(steps(9)==2)
assert(steps(3)==2)
assert(steps(7)==2)
assert(steps(5)==2)


assert(steps(1024)==31)

assert(steps(23)==2)
assert(steps(12)==3)



