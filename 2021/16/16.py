import sys

L=[]
for l in sys.stdin:
    s=""
    for x in l.strip():
        s+=str(bin(int(x,16))[2:]).zfill(4)

    L.append(s)
#assert(L[0]=="110100101111111000101000")
#assert(L[1]=="00111000000000000110111101000101001010010001001000000000")

def decodeliteral(s):

    v=0
    last = s[0]=='0'
    while True:
        v=v<<4|int(s[1:5],2)
        s=s[5:]
        if last:
            break
        last = s[0]=='0'
    return(s,v)

def decode(s):

    version=int(s[0:3],2)
    typeid=int(s[3:6],2)

    # chomp
    s = s[6:]

    if typeid==4: # literal value
        (s,l)=decodeliteral(s)
        return ((version,l),s)
    else:
        lengthtype=int(s[0])
        s=s[1:]
        if not lengthtype:
            length=int(s[0:15],2)
            s=s[15:]
            ss=s[:length]
            s=s[length:]
            L=[]
            while ss:
                (LT,ss)=decode(ss)
                L.append(LT)
            return((version,L),s)
        else:
            numpack=int(s[0:11],2)
            s=s[11:]
            L=[]
            for i in range(numpack):
                (LT,s)=decode(s)
                L.append(LT)
            return((version, L),s)

def versum(L):
    s=0
    if type(L)==tuple:
        s+=L[0]
        if type(L[1])==list:
            s+=versum(L[1])
    else:
        for i in L:
            s+=versum(i)
    return s
            
#assert(versum(decode(L[3])[0])==16)
#assert(versum(decode(L[4])[0])==12)
#assert(versum(decode(L[5])[0])==23)
#assert(versum(decode(L[6])[0])==31)

print("Answer 1: ",versum(decode(L[0])[0]))
