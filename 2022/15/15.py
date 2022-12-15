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
    print("cover",s,b,"(s)",side,"<<",d,">>",(s.real - abs(side), s.real + abs(side)))
    return (s.real - abs(side), s.real + abs(side))


line=list()
for i in range(len(sens)):
    c = cover(sens[i],beac[i],row)
    if c:
        line.append(c)


def overlap(a,b):
    if a==b:
        return True
    
    if a[0]>=b[0] and a[1]<=b[1]:
        return True
    else:
        return False

def merge(line):
    
    pre = len(line)
    post=0

    while pre!=post:

        line=set(line)
        line=list(line)

        if len(line)==1:
            break
    
        pre = post
        line= sorted(line,key=lambda x:x[0])

        print("Merging",line)
    
        ll=set()
        line.reverse()
    
        # remove true duplicates


        
        for i in range(len(line)-1):
            for j in range(i+1,len(line)):
                # find out if the current item is completely overlapped by the next item
                if overlap(line[i],line[i+1]):
                    ll.add(line[i])
            
        line=set(line)
        line=line-ll

        
        line= sorted(list(line),key=lambda x:x[0])

        if len(line)==1:
            print("down to 1, break")
            break
        
        ll = set()

        # merge things
        for i in range(len(line)-1):
            for j in range(i+1,len(line)):
                if line[i][0]<=line[i+1][0]:
                    if line[i][1]>=line[i+1][0] and line[i][1]<=line[i+1][1]:
                        print(line[i],"merge with",line[i+1])
                        ll.add((line[i][0],line[i+1][1]))
                    else:
                        ll.add(line[i])
                        ll.add(line[i+1])
                else:
                    ll.add(line[i])
                    ll.add(line[i+1])

        line = list(ll)
        post = len(line)
        print("merged:",line)

    return line

line=sorted(line,key=lambda x:x[0])
ma = max([int(y) for x,y in line])
mi = min([int(x) for x,y in line])

print(mi,ma)
score=0

def yes(x, line):

    for i in line:
        if x>=i[0] and x<=i[1]:
            return True

    return False

for i in range(mi,ma):
    if yes(i,line):
        score+=1

print(score)

