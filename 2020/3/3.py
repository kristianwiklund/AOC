#!/usr/bin/python3

def check(dx,dy):
    f=open("input","r")
    l=f.readlines()
    l=[l.strip('\n\r') for l in l]


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

print("1: "+str( check(3,1)))
print("2: "+str(check(1,1)*check(3,1)*check(5,1)*check(7,1)*check(1,2)))

