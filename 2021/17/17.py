#!/usr/bin/python3

import math

# game data
# target area: x=111..161, y=-154..-101

# test data
# target area: x=20..30, y=-10..-5

test = True

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

# max x velocity is determined by halting to a stop within the box
# x2=vx*(vx-1)/2
hmax=0
vxmax=abs(int(0.5*(1-math.sqrt(8*x2+1))))
print(vxmax,vymax)
d=0
h=0
for i in range(vxmax):
   d=d+vxmax
   vxmax=vxmax-1
   print("x",d,vxmax,h,vymax)
   h=h+vymax
   hmax=max(hmax,h)
   vymax=vymax-1

while True:
   print("x",d,vxmax,h,vymax)
   h=h+vymax
   hmax=max(h,hmax)
   vymax=vymax-1
   if h<y2:
       print("exit: hmax=",hmax,h)
       break
print("Answer 1: ",hmax)
   

