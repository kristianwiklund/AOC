from pprint import pprint

def checkxl(arr, x, y):

    h = int(arr[y][x])
    
    for xx in range(0,x):
        if int(arr[y][xx])>=h:
            return False
    return True

def checkxh(arr, x, y):

    h = int(arr[y][x])
        
    for xx in range(x+1,len(arr[0])):
        if int(arr[y][xx])>=h:
            return False
    return True

def checkyl(arr, x, y):

    h = int(arr[y][x])
    
    for yy in range(0,y):
        if int(arr[yy][x])>=h:
            return False
    return True

def checkyh(arr, x, y):

    h = int(arr[y][x])
    
    for yy in range(y+1,len(arr)):
        if int(arr[yy][x])>=h:
            return False
    return True

def checkheight(arr, x, y):

    if x==0 or y==0:
        return True

    if x>=len(arr[0])-1:
        return True

    if y>=len(arr)-1:
        return True

    return checkxl(arr, x, y) or checkxh(arr, x, y) or checkyl(arr, x, y) or checkyh(arr, x, y)

    

with open("input.txt","r") as fd:
    arr = [x.strip() for x in fd.readlines()]
    v = list()
    
    ys = len(arr)
    xs = len(arr[0])

    for x in range(xs):
        vl = list()
        for y in range(ys):
            vl.append(checkheight(arr,x,y))
        v.append(vl)

pprint(v)
print(sum([sum(x) for x in v]))
