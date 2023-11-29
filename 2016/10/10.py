import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
from sortedcontainers import SortedList
from sortedcontainers import SortedDict
from sortedcontainers import SortedSet
#import numpy as np

lines = readarray("input.txt",split=" ",convert=lambda x:x)
#lines = readlines("input.short")

targets = dict()

class Output:
    def __init__(self, what):
        self.container=[what]

    def get(self, what):
        self.container.append(what)
        
    def __repr__(self):
        return "Output("+self.__str__()+")"
    
    def __str__(self):
        return str(self.container)

    def __getitem__(self,idx):
        return self.container[idx]
    
class Bot:
    def __init__(self, name, lowto, highto):
        self.container=SortedSet()
        self.highto=highto
        self.lowto=lowto
        self.name=name

    def get(self, x):
        self.container.add(x)
        if len(self.container)==2:
            if list(self.container)==[17,61]:
                print("answer 1:",self.name,self.container)
            try:
                targets[self.lowto].get(self.container[0])
            except:
                targets[self.lowto] = Output(self.container[0])

            try:
                targets[self.highto].get(self.container[1])
            except:
                targets[self.highto] = Output(self.container[1])
                
            self.container = SortedList()

    def __repr__(self):
        return "Bot("+self.__str__()+")"
    
    def __str__(self):
        return self.lowto+","+self.highto

for line in lines:
    if line[0]=="bot":
        targets[line[0]+line[1]] = Bot(line[0]+line[1],line[5]+line[6],line[10]+line[11])

for line in lines:
    if line[0]=="value":
        targets[line[4]+line[5]].get(int(line[1]))

print("Answer 2:",targets["output0"][0]*targets["output1"][0]*targets["output2"][0])
