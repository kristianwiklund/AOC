import sys

L=[]
for l in sys.stdin:
    s=""
    for x in l.strip():
        s+=str(bin(int(x,16))[2:]).zfill(4)

    L.append(s)

print(L)
print(len(L[0]))
assert(L[0]=="00111000000000000110111101000101001010010001001000000000")
