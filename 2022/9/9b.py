
s = { "R":(1,0),
      "L":(-1,0),
      "U":(0,-1),
      "D":(0,1),
    }

k = dict()

def follow(hx,hy,tx,ty):

    # figure out how to move the tail
    # straight up or down
    if abs(hx-tx)>1 and abs(hy-ty)==0:
        tx+=1 if hx-tx>0 else -1
    elif abs(hx-tx)==0 and abs(hy-ty)>1:
        ty+=1 if hy-ty>0 else -1
    else:
        # a diagonal
        if abs(hx-tx)>1 and abs(hy-ty)>1:
            tx+=1 if hx-tx>0 else -1
            ty+=1 if hy-ty>0 else -1
        elif abs(hx-tx)>1:
            tx+=1 if hx-tx>0 else -1
            ty+=(hy-ty)
        elif abs(hy-ty)>1:
            ty+=1 if hy-ty>0 else -1
            tx+=(hx-tx)
        else:
            pass
        #print (w,d,hx,hy,tx,ty)

    return (tx,ty)
    
def move(rope,w,d):

    for i in range(d):
        
        hx=rope[0][0]+s[w][0]
        hy=rope[0][1]+s[w][1]

        nr = [(hx,hy)]
        rope.pop(0)
        for (x,y) in rope:
            (xp,yp) = follow(hx,hy,x,y)
            nr.append((xp,yp))
            hx=xp
            hy=yp

        rope = nr

        if not rope[9] in k:
            k[rope[9]]=True

        
    return nr
    

rope = [(0,0) for x in range(10)]
  
def p(rope, f=None):

    if not (0,0) in rope:
        s=True
    else:
        s=False

    ax = [x[0] for x in rope]
    ay = [x[1] for x in rope]

    lx=min(0,min(ax))
    hx=max(0,max(ax))
    ly=min(0,min(ay))
    hy=max(0,max(ay))

    print(lx,ly)
        
    for y in range(ly,hy+1):
        for x in range(lx,hx+1):
            if s and (x,y)==(0,0):
                print("s",end="")
                continue
            if (x,y) in rope:
                if f:
                    if (x,y)==(0,0):
                        print("s",end="")
                    else:
                        print (f,end="")
                else:
                    if rope.index((x,y))==0:
                        print ("H",end="")
                    else:
                        print (rope.index((x,y)),end="")
            else:
                print(".",end="")
        print("")
    print("-----------")
                

with open("input.txt","r") as fd:

    lines = [x.strip() for x in fd.readlines()]

    hx=0
    hy=0
    tx=0
    ty=0
    k[(0,0)]=True
    
    for m in lines:

        w,d = m.split()
        rope = move(rope,w,int(d))

    print(len(k))


