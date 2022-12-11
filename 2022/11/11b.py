from pprint import pprint
import sys
sys.path.append("../..")
from utilities import *

def ap(fd):

    who = fd.readline().strip().split(" ")[1][:-1]
    try:
        items = [int(x) for x in fd.readline().strip().split(":")[1].split(",")]
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
            new = eval(apes[m]["o"])
            #new = new // 3
            items[i]["v"]=new
            #items[i]["f"]=("("+apes[m]["o"].replace("old",items[i]["f"])+")").replace(" ","")
            if new % apes[m]["t"]:
                #print(i,"->",apes[m]["if"])
                items[i]["ss"]+=str(apes[m]["if"])
                apes[m]["fc"]+=1
                apes[apes[m]["if"]]["i"].append(i)
            else:
                #print(i,"->",apes[m]["it"])
                items[i]["ss"]+=str(apes[m]["it"])
                apes[m]["tc"]+=1
                apes[apes[m]["it"]]["i"].append(i)
        apes[m]["i"] = list()


    return (apes)

def pap(i,apes):
    
    return [(x["cnt"],x["tc"],x["fc"]) for x in apes]



# Returns the longest repeating non-overlapping
# substring in str
def lrs(str):
 
    n = len(str)
    LCSRe = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    res = "" # To store result
    res_length = 0 # To store length of result
 
    # building table in bottom-up manner
    index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
             
            # (j-i) > LCSRe[i-1][j-1] to remove
            # overlapping
            if (str[i - 1] == str[j - 1] and
                LCSRe[i - 1][j - 1] < (j - i)):
                LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1
 
                # updating maximum length of the
                # substring and updating the finishing
                # index of the suffix
                if (LCSRe[i][j] > res_length):
                    res_length = LCSRe[i][j]
                    index = max(i, index)
                 
            else:
                LCSRe[i][j] = 0
 
    # If we have non-empty result, then insert
    # all characters from first character to
    # last character of string
    if (res_length > 0):
        for i in range(index - res_length + 1,
                                    index + 1):
            res = res + str[i - 1]
 
    return res
 


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
            ni.append(nin)
        apes[i]["i"]=ni


    for i in range(200):
        if not i%100:
            print(i)
        inspect(apes)

    #for x in range(1):
    #    for i in sorted(items,key=lambda x:x[1]):
    #        print(i,"=",items[i]["ap"])
            
    #apes = sorted(apes,key=lambda x:-x["cnt"])
    #print("Part 2:", apes[0]["cnt"],apes[1]["cnt"],apes[0]["cnt"]*apes[1]["cnt"])

    for i in items:
        print ("---",i,"---")
        print (i,items[i]["ss"])
        print(i,lrs(items[i]["ss"]))
        
