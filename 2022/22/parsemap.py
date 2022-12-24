
def splitrealmap(mymap):
    global altworld
    altworld=True
    
    newmap = dict()
    dim = len(mymap[0])//3

    # chomp map 1 and 2
    newmap[1]=list()
    newmap[2]=list()

    for i in range(dim):
        l = mymap[i].strip()
        newmap[1].append(mymap[i][dim:dim*2])
        newmap[2].append(mymap[i][dim*2:dim*3])
        
    newmap[3]=list()
    
    for i in range(dim):
        l = mymap[i+dim].strip()

        three = l[0:dim]
        newmap[3].append(three)

    newmap[4]=list()
    newmap[5]=list()

    for i in range(dim):
        l = mymap[i+dim*2].strip()

        four = l[0:dim]              
        five = l[dim:dim*2]
        newmap[4].append(four)
        newmap[5].append(five)

    newmap[6]=list()
    for i in range(dim):
        newmap[6].append(mymap[i+dim*3].strip())

    for i in range(1,7):
        print("map",i)
        for j in range(len(newmap[i])):
            print(newmap[i][j])
        
    return newmap
    
def splitmap(mymap):
    global altworld
    altworld=False
    
    v = mymap[0].strip()
    dim = len(v)
    
    if len(v)>50:
        return splitrealmap(mymap)

    if v=="........":
        return splitrealmap(mymap)
    
    newmap = dict()
    
    # chomp map 1
    newmap[1]=list()

    for i in range(dim):
        newmap[1].append(mymap[i].strip())

    print("Map 1 is")
    for i in newmap[1]:
        print(i)
    print(len(newmap[1]),len(newmap[1][0]))
    # chomp maps 2,3,4
    newmap[2]=list()
    newmap[3]=list()
    newmap[4]=list()
    
    for i in range(dim):
        l = mymap[i+dim].strip()
        two = l[0:dim]
        three = l[dim:dim*2]
        four = l[dim*2:dim*3]
        newmap[2].append(two)
        newmap[3].append(three)
        newmap[4].append(four)

    print("Map 2 is")
    for i in newmap[2]:
        print(i)

    print("Map 3 is")
    for i in newmap[3]:
        print(i)

    print("Map 4 is")
    for i in newmap[4]:
        print(i)

    newmap[5]=list()
    newmap[6]=list()

    for i in range(dim):
        l = mymap[i+dim*2].strip()

        five = l[0:dim]              
        six = l[dim:dim*2]
        newmap[5].append(five)
        newmap[6].append(six)

    print("Map 5 is")
    for i in newmap[5]:
        print(i)

    print("Map 6 is")
    for i in newmap[6]:
        print(i)
        
    return newmap

def transmogrif(mypath, fullmap):
    global altworld

    if altworld:
        print("Using alternative rendering")
    np=[]

    if not altworld:
        for i in mypath:
            x,y,d,world=i
            #print(i)
        
            #print((x,y),world,end="")
            if world==1:
                x+=len(fullmap[1])*2
            elif world<=4:
                y+=len(fullmap[1])
                x+=len(fullmap[1])*(world-2)
            else:
                y+=len(fullmap[1])*2
                x+=len(fullmap[1])*(world-3)
                #print("->",(x,y),world)
            np.append((x,y,world,d))

        return(np)
    else:
        for i in mypath:
            x,y,d,world=i
            #print(i)
        
            #print((x,y),world,end="")
            if world<=2:
                x+=len(fullmap[1])*world
            elif world==3:
                y+=len(fullmap[1])
                x+=len(fullmap[1])
            elif world<=5:
                y+=len(fullmap[1])*2
                x+=len(fullmap[1])*(world-4)
                #print("->",(x,y),world)
            else:
                y+=len(fullmap[1])*3
                
            np.append((x,y,world,d))
            
        return(np)
