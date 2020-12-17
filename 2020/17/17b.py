
def parsinator(x):
    s=dict()
    
    for i in range(0,len(x)):
        for j in range(0,len(x[i])):
            if x[i][j]=='#':
                s[j,i,0,0]=True 

    return (s,0,0,0,0,len(x)-1,len(x[i])-1,0,0)

banana = [(a,b,c,d) for a in [-1,0,1] for b in [-1,0,1] for c in [-1,0,1] for d in [-1,0,1] if (a,b,c,d)!=(0,0,0,0)]
    
def count(s,x,y,z,w):
    
    #nb = [(a+x,b+y,c+z,d+w) for a in [-1,0,1] for b in [-1,0,1] for c in [-1,0,1] for d in [-1,0,1] if (a,b,c,d)!=(0,0,0,0) and (a+x,b+y,c+z,d+w) in s ]
    nb = [(t[0]+x,t[1]+y,t[2]+z,t[3]+w) for t in banana if (t[0]+x,t[1]+y,t[2]+z,t[3]+w) in s ]

    return len(nb)

def check(s,x,y,z,w):

    c = count(s,x,y,z,w)

    if c==3:
        return True

    if c==2 and (x,y,z,w) in s:
        return True

    return False

def sim(space):
    (s,minx,miny,minz,minw,maxx,maxy,maxz,maxw) = space
    
    ns = {(x,y,z,w):True for x in range(minx-1,maxx+2) for y in range(miny-1,maxy+2) for z in range(minz-1,maxz+2) for w in range(minw-1,maxw+2) if (check(s,x,y,z,w))}

    for (x,y,z,w) in ns:
        if x<minx:
            minx=x
        if x>maxx:
            maxx=x
        if y<miny:
            miny=y
        if y>maxy:
            maxy=y
        if z<minz:
            minz=z
        if z>maxz:
            maxz=z
        if w<minw:
            minw=w
        if w>maxw:
            maxw=w
            
    return (ns,minx,miny,minz,minw,maxx,maxy,maxz,maxw)

def draw(space):
    return
    (s,minx,miny,minz,minw,maxx,maxy,maxz,maxw) = space

    for w in range(minw,maxw+1):
        for z in range(minz,maxz+1):
            for y in range(miny,maxy+1):
                for x in range(minx, maxx+1):
                    if (x,y,z) in s:
                        print("#",end='');
                    else:
                        print(".",end='');
                print("")
            print("")
        print("")

inshort=[".#.","..#","###"]
#inshort=["...","###","..."]
inlong = [".##.####",".#.....#",          "#.###.##",          "#####.##",          "#...##.#",          "#######.",          "##.#####",".##...#."]
space=parsinator(inlong)
for i in range(0,6):
    space=sim(space)

    draw(space)

print(len(space[0]))



