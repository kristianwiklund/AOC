import networkx as nx

G=nx.DiGraph()
with open("input.txt") as fd:

    lines = [x.strip() for x in fd.readlines()]

    dirs=dict()
    dirs["/"]=set()
    G.add_node("/")
    
    cwd=""
    for l in lines:
        if l[0]=='$':
            if l[2]=='c':
                if l[5]=="/":
                    cwd = "/"  
                elif l[5]=='.':
                    cwd="/".join(cwd.split("/")[:-1])
                    if cwd=="":
                        cwd="/"
                else:
                    if ("dir "+l[5:]) in dirs[cwd]:
                        ocd=cwd
                        if cwd=="/":
                            cwd=""
                        
                        cwd=cwd+"/"+l[5:]
                        if not cwd in dirs:
                            dirs[cwd] = set()
                            G.add_edge(ocd,cwd)
            if l[2]=='l':
                pass

        else:
            dirs[cwd].add(l)
            if l[0]!='d':
                G.add_edge(cwd,l.split(" ")[1],weight=int(l.split(" ")[0]))
            else:
                G.add_edge(cwd,l.split(" ")[1],weight=-1)

score=0

for i in dirs:
    s = nx.descendants(G,i)
    s.add(i)
    w=int(G.subgraph(s).size(weight="weight"))

    if w<=100000:
#        print(w)
        score+=w
#    for j in dirs[i]:
#        if j[0]!='d':
#            p=i
#            p="" if i =="/" else i
#            print (p+"/"+j.split(" ")[1],j.split(" ")[0])


print("part 1:",score)

def findbigone(G,m):

    sd = ""
    ss = None
    for i in dirs:
        
        s = nx.descendants(G,i)
        s.add(i)
        w=int(G.subgraph(s).size(weight="weight"))
        if w>=m:
            # seek the smallest one
            if not ss or m<ss:
                ss = w
                sd = i
    return (ss,sd)

m=-1

s = nx.descendants(G,"/")
s.add("/")
fss=int(G.subgraph(s).size(weight="weight"))
m = -((70000000-30000000)-fss)

l = list()
for i in dirs:
    s = nx.descendants(G,i)
    s.add(i)
    w=int(G.subgraph(s).size(weight="weight"))

    if w>=m:
        l.append(w)

print("part 2:",sorted(l)[0])
