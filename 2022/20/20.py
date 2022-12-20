import sys
sys.path.append("../..")
from utilities import *
import networkx as nx
from copy import deepcopy
from pprint import pprint

def toright(seq,nr):
    i = seq.index(nr)
    del seq[i]

    i+=1

    if i>=len(seq):
        i-=len(seq)
#        print("poswrap",i)
        
    seq.insert(i,nr)
        
    return seq

def toleft(seq,nr):
    i = seq.index(nr)
#    print("toleft",seq)
    del seq[i]
#    print("removed i",seq,i)
    if i==0:
        seq=seq[:-1]+[nr]+[seq[-1]]
#        print(seq)
#        print("end")
        #        print("negwrap",i)
        #       print(seq)
        #        print("end")
        return seq
    elif i==1:
        seq.append(nr)
 #       print(seq)
#        print("end")
        return seq
    
 #   print("insert",nr,"at",i-1,"in",seq)
    seq.insert(i-1,nr)
  #  print(seq)
  #  print("end")
    return seq

def  qmix(sss,nr):

    if nr==0:
        return sss
    
    # find nr
    pos = sss.index(nr)
    # remove nr from list
    del sss[pos]
    print("moving item at", pos)
    
    # calculate new position
    np = pos+nr
#    while np<0:
#        np+=(len(sss))
        
    np = np%(len(sss))
    
   # print("inserting item",nr,"at",np)

    # three cases, we are in the middle, at the bottom, or at the top

    if np==0:
        print(">>>")
        return (sss+[nr])
    
    if np==(len(sss)):
        print("<<<")
        return ([nr]+sss)

    #print("insert at",np)
#    print(sss[np-1],sss[np],sss[np+1])
    vvv    = sss[:np]+[nr]+sss[np:]
#    print(vvv[np-1],vvv[np],vvv[np+1])
    #print ("qmix return length",np,len(vvv))
    return vvv
    
def mix(seq,nr):
    print("=================")
   # print("mixing",nr)
    if nr==0:
        return seq
    
    if nr<0:
        for i in range(-nr):
            seq=toleft(seq,nr)
#            print("<",seq)
        return seq
    if nr>0:
        for i in range(nr):
            seq=toright(seq,nr)
#            print(">",seq)
        return seq

assert(toleft([0,1,2],1)==[0,2,1])
assert(toleft([1,0,2],1)==[0,1,2])
print([0,2,1])
print(toleft([0,2,1],1))
assert(toleft([0,2,1],1)==[0,1,2])

    
arr = readarray("input.short",split=" ",convert=lambda x:int(x))
arr=[x[0] for x in arr]
seq=deepcopy(arr)
seq2=deepcopy(arr)

seq=mix(seq,1)
seq2=qmix(seq2,1)
assert(seq==[2,1,-3,3,-2,0,4])
assert(seq==seq2)

seq=mix(seq,2)
seq2=qmix(seq2,2)
assert(seq==[1,-3,2,3,-2,0,4])
assert(seq==seq2)

seq=mix(seq,-3)
seq2=qmix(seq2,-3)
assert(seq==seq2)
assert(seq==[1,2,3,-2,-3,0,4])


seq=mix(seq,3)
seq2=qmix(seq2,3)
assert(seq==[1,2,-2,-3,0,3,4])
assert(seq==seq2)

seq=mix(seq,-2)
seq2=qmix(seq2,-2)
assert(seq==[1,2,-3,0,3,4,-2])
assert(seq==seq2)

seq=mix(seq,0)
seq2=qmix(seq2,0)
assert(seq==[1,2,-3,0,3,4,-2])

try:
    assert(seq==seq2)
except:
    print("seq!=seq2")
    print("should be",[1,2,-3,0,3,4,-2])
    print(seq)
    print(seq2)
    import sys
    sys.exit()

print(seq,seq2)
seq=mix(seq,4)
seq2=mix(seq2,4)
assert(seq==[1,2,-3,4,0,3,-2])
try:
    assert(seq==seq2)
except:
    print("seq!=seq2")
    print("should be",[1,2,-3,4,0,3,-2])
    print(seq)
    print(seq2)
    import sys
    sys.exit()

seq.append(-4711)
seq2.append(-4711)
seq=mix(seq,-4711)
seq2=mix(seq2,-4711)

try:
    assert(seq==seq2)
except:
    print("seq!=seq2")
    print(seq)
    print(seq2)
    import sys
    sys.exit()


seq.append(4711)
seq2=deepcopy(seq)
seq=mix(seq,4711)
seq2=mix(seq2,4711)
seq=mix(seq,-4711)
seq2=mix(seq2,-4711)
seq=mix(seq,4)
seq2=mix(seq2,4)
seq=mix(seq,-4711)
seq2=mix(seq2,-4711)
seq=mix(seq,4711)
seq2=mix(seq2,4711)

try:
    assert(seq==seq2)
except:
    print("seq!=seq2")
    print(seq)
    print(seq2)
    import sys
    sys.exit()


print("Tests passed")


       
#import sys
#sys.exit()

## -

arr = readarray("input.txt",split=" ",convert=lambda x:int(x))
arr=[x[0] for x in arr]
seq=deepcopy(arr)
seq2=deepcopy(arr)

print("seq len",len(seq))
print("seq2 len",len(seq2))


print("---")

oseq=deepcopy(seq)
for i in arr:
    print(i,"is in ",seq.index(i),"in seq, at",seq2.index(i),"in seq2, and in",oseq.index(i),"in oseq")
    print(2*len(seq)+i)
    
    assert(len(seq)==len(seq2))
    seq=mix(seq,i)    
    seq2=qmix(seq2,i)
    
    print("seq2 length",len(seq2))

#    try:
#        assert(seq==seq2)
#    except:
#        print("s,s2 len:",len(seq),len(seq2))
#        for i in range(max(len(seq),len(seq2))):
#            if seq[i]!=seq2[i]:
#                print ("differs at",i)
#                print ("break was done at",(len(seq)+i)%len(seq))
#                print((oseq[i-1],seq[i-1],seq2[i-1]),(oseq[i],seq[i],seq2[i]),(oseq[i+1],seq[i+1],seq2[i+1]),(oseq[i+2],seq[i+2],seq2[i+2]))
#                print("Found",seq[i],"at",i,"in seq")
#                print("Found",seq2[i],"at",i,"in seq2")
               
#                try:
#                    print(seq[i],"is at ",seq2.index(seq[i]),"in seq2")
#                except:
#                    print(seq[i],"is gone from seq2")
#                    import sys
#                    sys.exit()
#                break
                   
#        print("assert exception, exiting")
#        import sys
#        sys.exit()
   
print("---")
p=seq2.index(0)

#v = seq2[(1000+p)%len(seq2)]+seq2[(2000+p)%len(seq2)]+seq2[(3000+p)%len(seq2)]
#assert(v!=1306)
#assert(v!=10022)
#assert(v!=15540)
#assert(v!=2655)
#assert(v!=-7031)
#assert(v!=2655)
#assert(v!=8011)

#seq=seq2

print (seq[(1000+p)%len(seq)])
print (seq[(2000+p)%len(seq)])
print (seq[(3000+p)%len(seq)])

print("<<<",seq[(1000+p)%len(seq)]+seq[(2000+p)%len(seq)]+seq[(3000+p)%len(seq)])

from itertools import cycle

cnt=0
pp=0
found=False
for i in cycle(seq):

    if i==0 and not found:
        found=True
        print("pp",pp,"p",p)
        continue

    p+=1

    if found:
        cnt+=1
        if cnt==1000:
            print (cnt,len(seq),i)
            a=i

        if cnt==2000:
            print (cnt,len(seq),i)
            b=i

        if cnt==3000:
            print (cnt,len(seq),i)
            print(">>>",a+b+i)
            break

    if p>len(seq)*5:
        print("ebreak")
        break

print("trest",p,len(seq),seq.index(8767))
