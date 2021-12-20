#!/usr/bin/python3

import re



level="\[[^\[\]]*"
number="[0-9]"
comma=","

def explode(s):
    match = re.search(level+level+level+level+number+comma+number,s)

    if match:
        #print(match)
        (start, end)=match.span()
        where = end-3
        (l,r)=s[where:where+3].split(",")
        #print(l,r)
        l = int(l)
        r = int(r)
        
        # find the first number to the right of the hit

        match = re.search(number,s[end:])
        if match:
            #print(s[end:])
            #print (match)
            (startr,endr)=match.span()
            #print (s[end+startr:])
            value=int(s[end+startr:][0])
            #print(value+r)
            #print(s)
            s = s[:end+startr]+str(value+r)+s[end+startr+1:]
            #print(s)

        # explode the hit

        s = s[:where-1]+"0"+s[where+4:]
        #print(s)
        # find the first number to the left of the hit

        w = s[:where-1][::-1]
        #print(w)
        match = re.search(number,w)
        if match:
            #print (match)
            #print("nosplice",w)

            (startr,endr)=match.span()
            value=int(w[startr:][0])
            w = w[:startr]+str(value+l)+w[startr+1:]
            #print ("splice",w)
            w=w[::-1]
            #print(w)
            #print ("spre",s)
            s = w + s[where-1:]
            #print("spost",s)
        return s
        
s1="[[[[[9,8],1],2],3],4]"
assert (explode(s1) == "[[[[0,9],2],3],4]")

s2="[7,[6,[5,[4,[3,2]]]]]"
assert(explode(s2) == "[7,[6,[5,[7,0]]]]")

s3="[[6,[5,[4,[3,2]]]],1]"
assert (explode(s3) == "[[6,[5,[7,0]]],3]")

s4="[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"
try:
    assert (explode(s4) == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
except:
    print(explode(s4))
    print ("[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
