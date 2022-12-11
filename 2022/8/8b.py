from pprint import pprint
#1440

def checkxl(arr, x, y):

    h = int(arr[y][x])
    s = 0

    if x==0:
        return 0
    
    for xx in range(x-1,-1,-1):
        if int(arr[y][xx])<h:
            s+=1
        else:
            return s+1
    return s

def checkxh(arr, x, y):

    s = 0
    h = int(arr[y][x])
        
    for xx in range(x+1,len(arr[0])):
        if int(arr[y][xx])<h:
             s+=1
        else:
            return s+1
        
    return s


def checkyl(arr, x, y):

    h = int(arr[y][x])
    s = 0

    if y==0:
        return 0
    
    for yy in range(y-1,-1,-1):
        if int(arr[yy][x])<h:
            s+=1
        else:
            return s+1
    return s

def checkyh(arr, x, y):

    s = 0
    h = int(arr[y][x])
        
    for yy in range(y+1,len(arr)):
        if int(arr[yy][x])<h:
            s+=1
        else:
            return s+1
        
    return s




def checkheight(arr, x, y):

    return checkyl(arr, x, y)*checkxl(arr, x, y)*checkxh(arr, x, y)*checkyh(arr, x, y)

    

with open("input.short","r") as fd:
    arr = [x.strip() for x in fd.readlines()]
    v = list()
    
    ys = len(arr)
    xs = len(arr[0])

    for x in range(xs):
        vl = list()
        for y in range(ys):
            vl.append(checkheight(arr,x,y))
        v.append(vl)

print(max([max(x) for x in v]))

