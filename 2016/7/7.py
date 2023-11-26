import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
#import numpy as np
import re

#arr = readarray("input.short",split="",convert=lambda x:x)
lines = readlines("input.long")

#117 is too high

def splitme(x):
    a = re.sub("\[[^]]*\]"," ",x)
    b = re.sub("[^[]*\[([^]]*)\][^[]*","\g<1> ",x)

    return (a.strip(),b.strip())
    
assert(splitme("ioxxoj[asdfgh]zxcvbn")== ('ioxxoj zxcvbn', 'asdfgh'))
assert(splitme("aaaa[xxxx]bbb[yyy]ccccccc")==("aaaa bbb ccccccc","xxxx yyy"))

def isabba(s):
    for x in range(len(s)):
        ss = s[x:x+4]
        if len(ss)==4:
#            print(ss)
#            print(ss[0:2],"".join(reversed(ss[2:4])))
            if ss[0]!=ss[1]:
                if ss[0:2] == "".join(reversed(ss[2:4])):
                    return True
    return False
                    
assert(isabba("ioxxoj")==True)
assert(isabba("aaaa")==False)

def supportstls(x):
    l = splitme(x)
    return isabba(l[0]) and not isabba(l[1])
            
assert(supportstls("abba[mnop]qrst")==True)
assert(supportstls("aaaa[qwer]tyui")==False)

print("TLS IPs:",sum([supportstls(x) for x in lines]))

def supportssl(s):
    (s1,s2)=splitme(s)
    for x in range(len(s1)):
        ss = s1[x:x+3]
        if len(ss)==3:
            if ss[0]==ss[2] and ss[0]!=ss[1]:
                # ABA
                bab = ss[1]+ss[0]+ss[1]
                if bab in s2:
                    return True
    return False

# there were working unit tests here but I changed the API

print("SSL IPs:",sum([supportssl(x) for x in lines]))
    
