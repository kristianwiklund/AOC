import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

arr = readarray("input.txt")
row = 2000000
#row=10

beac=list()
sens=list()

for l in arr:
    x=int(l[2].split("=")[1].strip(","))
    y=int(l[3].split("=")[1].strip(":"))
    s=complex(x,y)
#    print(s)
    sens.append(s)
    
    x=int(l[8].split("=")[1].strip(","))
    y=int(l[9].split("=")[1].strip(":"))
    b=complex(x,y)
#    print(b)
    beac.append(b)

print(sens)

# for each beacon
#  identify the lines defining the area of the relevant beacon coverage
#  project those lines on the line we want to look at
#  the length of the line grows with +1 on each side from the center for each row above the furthest row
# the result is a set of lines showing what is covered

def cover(s,b,l):

    d = int(abs(s.imag-b.imag)+abs(s.real-b.real))

    if int(s.imag+d)<l:
        return None

    # d is the max distance where we have guaranteed no other beacons
    # at that place, we have one single blob right below the sensor
    # at position (s.real, s.imag+d)
    # for each distance above this, we get an additional blob on the
    # side
    side = d-abs(s.imag-l)
    if(side<0):
        return None
    
#    print("cover",s,b,"(s)",side,"<<",d,">>",(s.real - abs(side), s.real + abs(side)))
    return (s.real - abs(side), s.real + abs(side))


def lineme(row):
    line=list()

    for i in range(len(sens)):
        c = cover(sens[i],beac[i],row)
        if c:
            line.append(c)

        line=sorted(line,key=lambda x:x[0])
    return line

#print(mi,ma)

def yes(x, line):

    for i in line:
        if x>=i[0] and x<=i[1]:
            return True

    return False

def scoreme(line, maxx=None):
    score=0
    
    ma = max([int(y) for x,y in line])
    if maxx:
        ma = max(maxx,ma)
        
    mi = min([int(x) for x,y in line])

    
    for i in range(mi,ma):
        if yes(i,line):
            score+=1
            if (ma-mi)<80:
                print("#",end="")
            else:
                if (ma-mi)<80:
                    print(".",end="")    
    return score
 
print("")
line = lineme(row)


print("part 1:",scoreme(line))


def overlap(a,b):
    if a==b:
        return True
    
    if a[0]>=b[0] and a[1]<=b[1]:
        return True
    else:
        return False

def cm(a,b):

    if a==b:
        return 0

    if a[0]==b[0]:
        if a[1]==b[1]:
            return 0
        if a[1]<b[1]:
            return -1
        return 1
    if a[0]<b[0]: 
        return -1
    return 1
    

from functools import cmp_to_key

for i in range(0,4000000):
    line = lineme(i)
    line= sorted(list(line),key=cmp_to_key(cm))

    x=0
    for j in line:
        if j[0]<x:
            if j[1]<x:
                continue
        if j[0]-x == 2:
            print ("part 2:", i+(x+1)*4000000,line)
            import sys
            sys.exit()
        
        x=j[1]
        if x>4000000:
            break
        
