import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

wind = readarray("input.short",split="")[0]
owind = deepcopy(wind)

#The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

shapes = [["####"],[".#.","###",".#."],["..#","..#","###"],["#","#","#","#"],["##","##"]]

#The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).
# If the end of the list is reached, it repeats

#The tall, vertical chamber is exactly seven units wide

minx = 0
maxx = 6

chamber = {(0,0):"#",(1,0):"#",(2,0):"#",(3,0):"#",(4,0):"#",(5,0):"#",(6,0):"#"}

def pp(chamber,alt=False):
    global minx
    global maxx

    print("    +-------+")
    
    maxy = max([y for x,y in chamber])
    
    for y in range(maxy+1,-1,-1):
        l=0
        for x in range(minx-1,maxx+2):
            if x<0:
                if not alt:
                    print("{:3d} |".format(y),end="")
                continue
            
            if x==maxx+1:
                if not alt:
                     print("|".format(y),end="")
                continue
            
            if (x,y) in chamber:
                l+=1
                if not alt:
                    print (chamber[(x,y)],end="")
            else:
                if not alt:
                    print(".",end="")
        if not alt:
            print("")
        else:
            print (l,end=",")
            
    if not alt:
        print("    +-------+")
        print("")

def collide(chamber, shape, nx, ny):

    
    for y in range(len(shape)):
        for x in range(len(shape[y])):
            if shape[y][x]=="#":
                if (nx+x,ny-y) in chamber:
                    return True

    return False

def draw(c, shape, x, y, sym="#"):
    
    for sy in range(len(shapes[shape])):
        for sx in range(len(shapes[shape][sy])):
            if shapes[shape][sy][sx]=="#":
                c[(x+sx,y-sy)]=sym
    return c

def drop(chamber, shape, wind):
    global minx
    global maxx

    #Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

    x=2 
    y = max([y for x,y in chamber])+3+len(shapes[shape])

    #After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by the next symbol in the jet pattern) and then falling one unit down.
    while True:

        # first push...
        d = wind.pop(0)
        wind.append(d)

        #pp(draw(deepcopy(chamber),shape,x,y,sym="@") )

        
        # shape width is...
        width = max([len(x) for x in shapes[shape]])
        #print ("Shape",shape,"is",width,"wide")
        
        if d=="<":
            nx = x-1
            if nx<minx:
                nx=minx
        else:
            nx = x+1
            if nx+width>maxx+1:
#                print(x,"x hit",nx+width,"backing")
#                for i in range(nx,nx+width):
#                    print(i)
                nx-=1

        check = collide(chamber, shapes[shape], nx, y)
        if not check:
            x=nx
            
        #print(d)
        #pp(draw(deepcopy(chamber),shape,x,y,sym="@"))
            
        # ...then fall

        # shape width is...
        height = len(shapes[shape])

        ny = y - 1

        check = collide(chamber, shapes[shape], x, ny)
        if not check:
            y=ny
        else:
            # we hit something on the way down, lock in place
            chamber = draw(chamber, shape, x, y)

            return (chamber,wind)

hmap=dict()

for i in range(300):
    (chamber,wind) = drop(chamber,i%5,wind)
    height = max([y for (x,y) in chamber])
    hmap[i]=height
    
pp(chamber)


# create different representations of the chamber

height = max([y for (x,y) in chamber])


# a string
scham=""
for y in range(2,height):
    for x in range(maxx+1):
        if (x,y) in chamber:
            scham=scham+"#"
        else:
            scham=scham+" "
# number of tjohej per row

x=scham

def bobtonum(x):
    scham=deepcopy(x)
    print("Converting to numbers")
    num=[]
    while len(scham):
        p = scham[:7]
        q = scham[7:]
        t = sum([1 if x=='#' else 0 for x in p])
        scham=q
        num.append(chr(t+ord('1')))
    num="".join(num)
        
    return(num)

def bobtobin(x):
    # binary
    bnum=[]
    scham=deepcopy(x)
    while len(scham):
        p = scham[:7]
        q = scham[7:]
        p = p.replace("#","1").replace(" ","0")
        scham=q
        bnum.append(int(p,2))

    return (bnum)

num = bobtonum(x)
bnum=bobtobin(x)
#print (num)
#print (bnum)

def banana(s):
    # find recurring pattern in banana
    # the hypothesis is that it stabilizes towards the end
    #s = s[::-1] # reverse the string

    for i in range(11,len(s)):
        a = s[:i]
        v = s[i:].index(a)
        
        #print("l =",i,v,a)
        #print("l =",i,v,s[i+v:v+2*i])

        # gotcha
        if v==0:
            #print("Test sequence starts at",i)
            #print("Test sequence is",a)

            return len(a)
s=num

for j in range(len(s)):
    try:
        pheight=banana(s[j:])
        print ("offset",j)
        offset=j
        print ("pheight",pheight)
        break
    except:
        continue

# --

# reset the chamber, drop again

chamber = {(0,0):"#",(1,0):"#",(2,0):"#",(3,0):"#",(4,0):"#",(5,0):"#",(6,0):"#"}
pstartcount=-1
for i in range(300):
    (chamber,wind) = drop(chamber,i%5,wind)
    height = max([y for (x,y) in chamber])
    if height==offset and pstartcount<0:
        print("recording drop at offset",offset,"which required",i,"stones")
        pstartcount=i+1
    if height==offset+pheight:
        print("recording drop at pattern end",height,"which required",i,"stones")
        pendcount=i+1
        break

plen = pendcount-pstartcount
print("pattern height is",pheight,"created by",plen,"stones")

scount=1000000000000
pcount = scount-pstartcount # this is where the recurrence starts
npat = pcount // plen # this is the number of patterns in the recurrence
print("npat",npat)  
spill = pcount % plen
print(spill)

height=npat*pheight+offset+spill

print("Part 2:", height)
print("The example answer is 1514285714288")

#print(npat*pheight+pstart+spill)
#print((1514285714288-spill-pstart)/npat)


