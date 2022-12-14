import sys
sys.path.append("../..")
from utilities import *

p = readarray("input.txt",split="->",convert=lambda y:[int(x) for x in y.split(",")])


x=[i[0] for x in p for i in x ]
y=[i[1] for x in p for i in x ]
minx=min(x)
miny=min(y)
maxx=max(x)
maxy=max(y)


plan = dict()

def draw(plan,c1,c2):
    x1,y1=c1
    x2,y2=c2

    print("Draw",c1,"->",c2)
    
    dx = 0 if x2-x1==0 else int((x2-x1)/abs(x2-x1))
    dy = 0 if y2-y1==0 else int((y2-y1)/abs(y2-y1))

    if dx:
        for i in range(abs(x2-x1)+1):
            plan[(x1+i*dx,y1)]="#"
    else:
        for i in range(abs(y2-y1)+1):
            plan[(x1,y1+i*dy)]="#"

    return plan
            
for line in p:

    for c in range(1,len(line)):
        plan = draw(plan,line[c-1],line[c])

def sand(plan,x,y,maxy):

    print("sand",x,y)
    
    if (x,y) in plan:
        print("full cave")
        return False

    
    while True:

        if y>=maxy:
            print("Dropped off",x,y,x,maxy)
            return False
        
        if not (x,y+1) in plan:
            y+=1
            continue

        if not (x-1,y+1) in plan:
            x-=1
            y+=1
            continue

        if not (x+1,y+1) in plan:
            x+=1
            y+=1
            continue

        # stopped
        plan[(x,y)]="o"
        return True

def pp(plan,minx,miny,maxx,maxy):

    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            if (x,y) in plan:
                print(plan[(x,y)],end="")
            else:
                if y==0 and x==500:
                    print("+",end="")
                else:
                    print(".",end="")
        print("")
                
from pprint import pprint        
pp(plan,minx,miny,maxx,maxy)

cnt=0
while sand(plan,500,0,maxy):
    cnt+=1
    pp(plan,minx,0,maxx,maxy)

print(cnt)
