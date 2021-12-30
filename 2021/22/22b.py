#!/usr/bin/python3

import sys
import cut
from box import Box
from reactor import Reactor
from termcolor import colored

# run the tests

import test

# - finally, read input from stdin and solve the problem

R = Reactor()

def readinaTOR():

    RR = Reactor()
    
    for l in sys.stdin:
        l = l.strip()

        b = Box(l)
        RR = RR + b
        
    return RR
