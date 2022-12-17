import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

wind = readarray("input.short",split="")[0]
#print(wind)
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

    print("+-------+")
    
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
        print("+-------+")
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
            

cnt=0

th = dict()
ph =0
rh=dict()
ip=-1
for i in range(5000):
#    print(i,wind)
    #Pattern:     ###    ###    ###    ####     #     ###     #
    (chamber,wind) = drop(chamber,i%5,wind)
    height = max([y for (x,y) in chamber])
    th[i]=height
    
    if ph<=height:
        rh[ph]=i
        ph=height

    #if not (i+1)%1000:
    #    print(i+1,height,height*1000/(i+1),height/17)

    if i==2021:
        print("Part 1:",height)

    # the recurring pattern in the test thingy starts at 175
    # and is 35 stones long
    #if height==175:
    #    print("ps:",height, i)
        
    #if not (height-175)%53:
    #    ho=height-175
    #    if ho:
#            print (ip,i,i-ip,(i+175)/(ho))
    #        ip=i


#pp(chamber)
    
print("Finding pattern")
# find recurring pattern
s=""
for y in range(1,height):
    for x in range(maxx+1):
        if (x,y) in chamber:
            s=s+"#"
        else:
            s=s+" "
#print(s)
#print("Converting to numbers")
#u=[]
#while len(s):
#    p = s[:7]
#    q = s[7:]
#    t = sum([1 if x=='#' else 0 for x in p])
#    s=q
#    u.append(chr(t+ord('1')))

#u="".join(u)
#print (u)
#import sys
#sys.exit()

#print(u)
#sq=lrs(s)
#print(sq)
#print(u)

def computeLPSArray(string, M, lps):
    length = 0        # length of the previous longest prefix suffix
    i = 1
  
    lps[0] = 0    # lps[0] is always 0
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:            
                # This is tricky. Consider the example AAACAAAA 
                # and i = 7.
                length = lps[length-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
  
# Returns true if string is repetition of one of its substrings
# else return false.
def isRepeat(string):
    # Find length of string and create an array to
    # store lps values used in KMP
    n = len(string)
    lps = [0] * n
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(string, n, lps)
  
    # Find length of longest suffix which is also
    # prefix of str.
    length = lps[n-1]
  
    # If there exist a suffix which is also prefix AND
    # Length of the remaining substring divides total
    # length, then str[0..n-len-1] is the substring that
    # repeats n/(n-len) times (Readers can print substring
    # and value of n/(n-len) for more clarity.
    if length > 0 and n%(n-length) == 0:
        return True
    else:
        False
  
def banana(s):
    # find recurring pattern in banana
    # the hypothesis is that it stabilizes towards the end
    #s = s[::-1] # reverse the string

    for i in range(100,len(s)):
        a = s[:i]
        v = s[i:].index(a)
        
        print("l =",i,v,a)
        print("l =",i,v,s[i+v:v+2*i])

        # gotcha
        if v==0:
            print("Test sequence starts at",i)
            print("Test sequence is",a)

            return len(a)

for j in range(len(s)):
    try:
        pheight=banana(s[j:])
        print ("offset",j)
        break
    except:
        continue
    


#print("Pattern:",sq)
print("Height:",height)
vq=""

pstart=j

print("pstart",pstart,"ulen",len(s))
#pstart=175
#print(rh)
pstartcount = rh[pstart]

# calculate this in a smart way later
pheight=pheight/7
print("got pheight",pheight)
pendcount = rh[pstart+pheight]
#plen=35 ## 54 - number of stones are 35
plen=(pendcount-pstartcount)
print("plen",plen)
scount=1000000000000
pcount = scount-pstartcount
npat = pcount // plen
print("npat",npat)
spill = pcount % plen
print(spill)

height=npat*pheight+pstart+spill+1

print("Part 2:", height)
print("The example answer is 1514285714288")

print(npat*pheight+pstart+spill)
print((1514285714288-spill-pstart)/npat)

# 1799999999916 too high
# 1400000000005 too low
