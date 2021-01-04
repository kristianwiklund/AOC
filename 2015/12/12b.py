#!/usr/bin/python3
import sys
import json
from pprint import pprint

with open(sys.argv[1],"r") as fd:
    d=json.load(fd)

def prune(obj):

    try:
        i = iter(obj)
    except:
        return obj

    if type(obj) is str:
        return obj
    
    if type(obj) is dict:
        
        if "red" in obj.values():
            return None
        else:
            for i in obj:
                obj[i] = prune(obj[i])
            return {x:obj[x] for x in obj if obj[x]}
            
    else:
        # list
        t = list()
        for i in obj:
            i = prune(i)
            if i:
                t.append(i)
        return t


pprint(prune (d))

