#!/usr/bin/python3

def check(dx,dy):
    f=open("input","r")
    l=f.readlines()
    l=[l.strip('\n\r') for l in l]
    #print(l)
    dx=3
    dy=1
    x=0
    y=0

    c=0
    while(y<len(l)):
    
        if l[y][x]=='#':
            c+=1
        x+=dx
            
        if x>=len(l[0]):
            x-=len(l[0])
        y+=dy

    return (c)
        
c=check(3,1)
print(c)
