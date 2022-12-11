from pprint import pprint
import sys
sys.path.append("../..")
from utilities import *

def ap(fd):

    who = fd.readline().strip().split(" ")[1][:-1]
    l = fd.readline().strip().split(":")
    try:
        items = [int(x) for x in l[1].split(",")]
    except:
        items = []
    op = fd.readline().strip().split("=")[1]
    test = int(fd.readline().strip().split(" ")[-1])
    iftrue = int(fd.readline().strip().split(" ")[-1])
    iffalse = int(fd.readline().strip().split(" ")[-1])
    fd.readline()

    return({"m":who,"i":items,"o":op,"t":test,"it":iftrue,"if":iffalse,"cnt":0,"tc":0,"fc":0})


def inspect(apes):
    
    for m in range(len(apes)):
        for i in apes[m]["i"]:
            apes[m]["cnt"]+=1

            old = items[i]["v"]
            items[i]["ap"][m]+=1
            new = eval(apes[m]["o"])%(19*23*13*17)
            #new = new // 3
            items[i]["v"]=new
            #items[i]["f"]=("("+apes[m]["o"].replace("old",items[i]["f"])+")").replace(" ","")
            if new % apes[m]["t"]:
                #print("A",i,"->",apes[m]["if"])
                items[i]["ss"]+=str(apes[m]["if"])
                apes[m]["fc"]+=1
                apes[apes[m]["if"]]["i"].append(i)
            else:
                #print("A", i,"->",apes[m]["it"])
                items[i]["ss"]+=str(apes[m]["it"])
                apes[m]["tc"]+=1
                apes[apes[m]["it"]]["i"].append(i)
        apes[m]["i"] = list()


    return (apes)

def pap(i,apes):
    
    return [(x["cnt"],x["tc"],x["fc"]) for x in apes]





with open("input.short","r") as fd:

    apes = list()
    while True:
        try:
            apes.append(ap(fd))
        except:
            break
    items = dict()
    
    for i in range(len(apes)):
        ni = list()
        for j in apes[i]["i"]:
            nin = (i,j)
            items[nin]=dict()
            items[nin]["ap"]={x:0 for x in range(len(apes))}
            items[nin]["v"]=j
            items[nin]["f"]=str(j)
            items[nin]["ss"]=""
            items[nin]["first"]=str(i)
            ni.append(nin)
        apes[i]["i"]=ni

    for i in range(10000):
        inspect(apes)
        if not i%100:
            print(i)
        if i==9999:
            print ("APES 1", [x["cnt"] for x in apes])
            
    #for x in range(1):
    #    for i in sorted(items,key=lambda x:x[1]):
    #        print(i,"=",items[i]["ap"])
            
    #apes = sorted(apes,key=lambda x:-x["cnt"])
    #print("Part 2:", apes[0]["cnt"],apes[1]["cnt"],apes[0]["cnt"]*apes[1]["cnt"])

    
    for i in items:
        #print ("---",i,"---")
        #print (i,items[i]["ss"])
        items[i]["lrs"]=lrs(items[i]["ss"])
        where = items[i]["ss"].index(items[i]["lrs"])
        prefix = items[i]["ss"][:where]
        items[i]["prefix"]=list(items[i]["first"]+prefix)
        print(i,prefix,items[i]["lrs"])
        items[i]["pos"]=0
        print("item",i,"prefix",len(prefix),"suffix",len(items[i]["lrs"]))

    def nis(i):
        pos = items[i]["pos"]
        lp = len(items[i]["prefix"])
        llrs = len(items[i]["lrs"])
                 
        if lp:
            x = items[i]["prefix"].pop(0)
            #print("pref", items[i]["prefix"])
            return x
        else:
            #print("lrs", items[i]["lrs"], "pos", items[i]["pos"],"X",items[i]["lrs"][pos])
            x = items[i]["lrs"][pos]
            pos+=1
            items[i]["pos"] = pos % llrs

            return x

    def cnti(z,n,ac):
        cnt=0
        a = nis(z)
        b = ""
        while cnt<n:
            cnt+=1
            while True:
                #print("a",a,"b",b)
                #print("B",z,"->",a)
                ac[int(a)]+=1
                #print("B",ac)
                b = nis(z)

                # we do the monkeys in order. Hence, if we end up moving an item to a monkey lower than the monkey
                # the item is located in, we have a new cycle
                if int(b) < int(a):
                    #print("B -tick")
                    a=b
                    break
                a=b
        return ac
        
    # we know the sequences of the items. Now we only have to make the apes toss them in the right order
    # we only have 1 item in the test code
    ac = {x:0 for x in range(len(apes))}

    for i in items:
        #print(i)
        ac = cnti(i,1000,ac)
        #print(ac)

    

#print ("B -end")
#print("B",z,"->",a)
#ac[int(a)]+=1

print("APES 2",list(ac.values()))
        
