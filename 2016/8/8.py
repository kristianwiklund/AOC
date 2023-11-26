import sys
sys.path.append("../..")
from utilities import *
#import networkx as nx
from copy import deepcopy
from pprint import pprint
import numpy as np

#lines = readlines("input.short")


def rect(b, x, y):
    for j in range(x):
        for i in range(y):
            b[i][j] = 1

def rotcol1(board, x):
    (ys,xs) = board.shape

    v = board[ys-1][x]
    for i in range(ys-1,0,-1):
        board[i][x]=board[i-1][x]

    board[0][x] = v

def rotcolby(board, x, n):
    for i in range(n):
        rotcol1(board, x)

def rotrow1(board, y):
    (ys,xs) = board.shape

    v = board[y][xs-1]
    for i in range(xs-1,0,-1):
        board[y][i]=board[y][i-1]

    board[y][0] = v

def rotrowby(board, y, n):
    for i in range(n):
        rotrow1(board, y)

board = np.zeros((6,50))

arr = readarray("input.long",split=" ",convert=lambda x:x)

for i in arr:
    if i[0] == "rect":
        (x,y)=i[1].split("x")
        rect(board,int(x),int(y))
    else:
        if i[1] == "row":
            y = int(i[2].split("=")[1])
            n = int(i[4])
            rotrowby(board,y,n)
        else:
            x = int(i[2].split("=")[1])
            n = int(i[4])
            rotcolby(board,x,n)            

print("Part 1:",int(sum(sum(board))))

for y in range(6):
    print("")
    for x in range(50):
        if board[y][x]:
            print("#",end="")
        else:
            print(" ",end="")
    
