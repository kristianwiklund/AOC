#!/usr/bin/python3

def isreal(room):
    s = room.split("[")

    if len(s)<2:
        return (False, -1)

    cksum = s[1][:-1]
    
#    print(s[0],":",cksum)

    s = s[0].split("-")
    r = s[:-1]
    try:        
        i = s[-1:]
        roomid = int(i[0])
    except:
        return (False, roomid)

#    print(r,i)


    d = dict()
    s = "".join(r)

#    print(s)

    for x in s:
        try:
            d[x]+=1
        except:
            d[x]=1

#    print(d)

    r = reversed(sorted(list(set(d.values()))))
    
#    print(r)

    tvitt = list()
    for x in r:
        v = [k for k,v in d.items() if v==x]
        tvitt.append(set(v))
#        print(x,v)
    
#    print(tvitt)

    cnt=0
    for i in cksum:
        if len(tvitt[cnt])>1:
            p = cksum.find(i)
            slc = cksum[p:p+len(tvitt[cnt])]
#            print(i,p,slc)
            if len(slc)>1:
                if all(slc[i] >= slc[i+1] for i in range(len(slc) - 1)):
#                    print("not alphabetic")
                    return (False, roomid)
            
        if not i in tvitt[cnt]:
#            print (i,tvitt[cnt])
            return (False, roomid)

        tvitt[cnt].discard(i)
        if len(tvitt[cnt])==0:
            cnt+=1
    
    return (True, roomid)

assert(isreal("aaaaa-bbb-z-y-x-123[abxyz]")==(True,123))
assert(isreal("a-b-c-d-e-f-g-h-987[abcde]")==(True,987))
assert(isreal("not-a-real-room-404[oarel]")==(True,404))
assert(isreal("totally-real-room-200[decoy]")==(False,200))

def decrypt(room, roomid):
    room = " ".join(room.split("-")[:-1])
#    print (room)

    room = "".join([chr((ord(x)+roomid-ord('a'))%26+ord('a')) if x!=" " else ' '  for x in room])
    return (room)

assert (decrypt("qzmt-zixmtkozy-ivhz-343", 343)=="very encrypted name")

with open("input.long") as fd:
    lines = [x.strip() for x in fd.readlines()]
    
    sum=0
    for x in lines:
        (t,s) = isreal(x)
        if t:
            sum+=s
            if decrypt(x,s)=="northpole object storage":
                print("Northpole Object Storage:",s)
                
    print("Sum of all real rooms:",sum)


