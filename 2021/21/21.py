#!/usr/bin/python3

p1=9
p2=3
dd=0
s1=0
s2=0
nr=0

def d(dd):

    dd+=1

    dd = dd if dd<=100 else dd-100
    return dd

def p(pp, i):
    
    pp+=i

    while pp>10:
        pp=pp-10
    return pp
    
while True:

    dd=d(dd)
    r1=dd
    nr+=1
    p1=p(p1,dd)
    dd=d(dd)
    r2=dd
    nr+=1
    p1=p(p1,dd)
    dd=d(dd)
    r3=dd
    nr+=1
    p1=p(p1,dd)
    s1+=p1

    if s1>=1000:
        break

    dd=d(dd)
    r1=dd
    nr+=1
    p2=p(p2,dd)
    dd=d(dd)
    r2=dd
    nr+=1
    p2=p(p2,dd)
    dd=d(dd)
    r3=dd
    nr+=1
    p2=p(p2,dd)
    s2+=p2
    
    if s2>=1000:
        break
    

print("Answer 1: ",min(s1,s2)*nr,min(s1,s2),nr)


