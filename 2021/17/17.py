#!/usr/bin/python3

import math

# game data
# target area: x=111..161, y=-154..-101

# test data
# target area: x=20..30, y=-10..-5

test = False

if test:
    x1=20
    x2=30
    y1=-10
    y2=-5
else:
    x1=111
    x2=161
    y1=-154
    y2=-101

# max y velocity is determined by the blob hitting the lowest edge of the box with its first step below zero
# since the trajectory above the zero line is symmetrical, it will hit the x axis with a step

vymax = abs(y1)-1

# min x velocity is determined by halting to a stop within the box
# x2=vx*(vx-1)/2
hmax=0
vxmin=abs(int(0.5*(1-math.sqrt(8*x2+1))))-1
vxm=vxmin
print(vxmin,vymax)
d=0
h=0
t=0
for i in range(vxmin):
    t=t+1
    d=d+vxmin
    vxmin=vxmin-1

    h=h+vymax
    hmax=max(hmax,h)
    vymax=vymax-1

while True:

    h=h+vymax
    t=t+1
    hmax=max(h,hmax)
    vymax=vymax-1
    if h<y2:
        print("exit: hmax=",hmax,h)
        break
if test:
    print("**** running with test data ****")
print("Answer 1: ",hmax, " ",t," (seconds)")

def bfopp(vx,vy):
    x=0
    y=0
    for i in range(0,t+1):
       if y<y1:
           return False
       if vx==0 and x<x1:
           return False
       if x>x2:
           return False
       if x<=x2 and x>=x1 and y<=y2 and y>=y1:
           return True
       x=x+vx
       y=y+vy
       vy=vy-1
       vx=max(0,vx-1)
       
    return False

c=0
for x in range(x2+1):
    for y in range(y1,-y1):
        if bfopp(x,y):
            #print(x,y)
            c=c+1

print("Answer 2:",c)
