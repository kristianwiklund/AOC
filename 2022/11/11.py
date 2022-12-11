from pprint import pprint

def ap(fd):

    who = fd.readline().strip().split(" ")[1][:-1]
    items = [int(x) for x in fd.readline().strip().split(":")[1].split(",")]
    op = fd.readline().strip().split("=")[1]
    test = int(fd.readline().strip().split(" ")[-1])
    iftrue = int(fd.readline().strip().split(" ")[-1])
    iffalse = int(fd.readline().strip().split(" ")[-1])
    fd.readline()
    
    return({"m":who,"i":items,"o":op,"t":test,"it":iftrue,"if":iffalse,"cnt":0})


def inspect(apes):
    
    for m in range(len(apes)):
        #print("Monkey",m)

        for i in apes[m]["i"]:
            #print (" Monkey inspects an item with worry level of",i)
            apes[m]["cnt"]+=1
            
            old = i
            new = eval(apes[m]["o"])
            #print (" Worry level op",apes[m]["o"],"goes to",new)
            new = new // 3
            #print (" Monkey gets bored with item. Worry level is divided by 3 to",new)
            #print (" Current worry level is ",end="")
            
            if new % apes[m]["t"]:
                #print ("not diviseble by",apes[m]["t"])
                #print (" Item with worry level",new,"is thrown to monkey",apes[m]["if"])
                apes[apes[m]["if"]]["i"].append(new)
            else:
                #print ("diviseble by",apes[m]["t"])
                #print (" Item with worry level",new,"is thrown to monkey",apes[m]["it"])
                apes[apes[m]["it"]]["i"].append(new)
        apes[m]["i"] = list()

        #print("")
        #for m in range(len(apes)):
        #    print ("Monkey",m,"-",apes[m]["i"],"inspected items",apes[m]["cnt"],"times")

    return (apes)

    
with open("input.txt","r") as fd:

    apes = list()
    while True:
        try:
            apes.append(ap(fd))
        except:
            break
    for i in range(20):
        apes = inspect(apes)

    apes = sorted(apes,key=lambda x:-x["cnt"])
    print("Part 1:", apes[0]["cnt"]*apes[1]["cnt"])
        
