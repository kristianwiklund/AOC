
s = { "R":(1,0),
      "L":(-1,0),
      "U":(0,-1),
      "D":(0,1),
    }

k = dict()



def move(hx,hy,tx,ty,w,d):

    for i in range(d):
        if not (tx,ty) in k:
            k[(tx,ty)]=True

        ox=hx
        oy=hy
        
        hx+=s[w][0]
        hy+=s[w][1]

        # figure out how to move the tail
        # straight up or down
        if abs(hx-tx)>1 and abs(hy-ty)==0:
            tx+=s[w][0]
        elif abs(hx-tx)==0 and abs(hy-ty)>1:
            ty+=s[w][1]
        else:
            # a diagonal
            if abs(hx-tx)>1:
                tx+=s[w][0]
                ty+=(hy-ty)
            elif abs(hy-ty)>1:
                ty+=s[w][1]
                tx+=(hx-tx)
            else:
                pass
                #print (w,d,hx,hy,tx,ty)

            
    return (hx,hy,tx,ty)
    

with open("input.txt","r") as fd:

    lines = [x.strip() for x in fd.readlines()]

    hx=0
    hy=0
    tx=0
    ty=0
    
    
    for m in lines:
            
        w,d = m.split()

        (hx, hy, tx, ty) = move(hx,hy,tx,ty,w,int(d))

    print(len(k))
