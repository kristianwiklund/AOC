import sys
sys.path.append("../..")
from utilities import *
import networkx as nx

cm = "SabcdefghijklmnopqrstuvwxyzE"

arr = readarray("input.txt",split="",convert=lambda x:cm.index(x))
bg = readarray("input.txt",split="")

def pos(arr, what):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x]==what:
                return (x,y)

    return None

G=nx.DiGraph()

def peek(arr,x,y):
    if x<0 or y<0:
        return None
    if y>=len(arr):
        return None
    if x>=len(arr[0]):
        return None

    return arr[y][x]

ck=[(0,1),(1,0),(-1,0),(0,-1)]

me=pos(arr,0)
you=pos(arr,27)
sls = list()
for y in range(len(arr)+1):
    for x in range(len(arr[0])+1):
        c = peek(arr,x,y)
        if c==1:
            sls.append((x,y))
        
        if c:
            for dx,dy in ck:
                v = peek(arr,x+dx,y+dy)
                if v!=None and c-v<=1:
                    if not G.has_edge((x,y),(x+dx,y+dy)):
                        G.add_edge((x,y),(x+dx,y+dy))
                        #print("edge",(x,y),"->",(x+dx,y+dy),"weight = ",abs(v-c))


printpath ((nx.shortest_path(G, source=you, target=me)),background=bg)
lpa = len(nx.shortest_path(G, source=you, target=me))-1
print("Part 1:",lpa)
lme=me
arr[me[1]][me[0]]=1

for me in sls:
    try:
        lpc = len(nx.shortest_path(G, source=you, target=me))-1
        if lpc<lpa:
            lme=me
            lpa=lpc
            print(me,lpa)
            printpath ((nx.shortest_path(G, source=you, target=me)),background=bg)
    except:
        pass

print ("part 2:",lpa,lme)



        
    


