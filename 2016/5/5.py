#!/usr/bin/python3

from hashlib import md5

def findit(pw):
    c = 0
    mpw = ""
    spw = [0,0,0,0,0,0,0,0]
    sc=0
    
    while True:
        slc = md5((pw+str(c)).encode("ascii"))
        slc = slc.hexdigest()

        if slc[:5]=="00000":
            # handle password 1
            if len(mpw)<8:
                mpw=mpw+slc[5]

            # handle password 2
                
            if int(slc[5],16)<8:
                if spw[int(slc[5])]==0:
                    spw[int(slc[5])]=ord(slc[6])
#                    print(slc, spw)
                    sc+=1
            if len(mpw)==8 and sc==8:
#                print(spw)
                return(mpw,"".join([chr(x) for x in spw]))
        c+=1

assert(findit("abc")==("18f47a30","05ace8e3"))
found = findit("ojvtpuvg")
print("The first password is:",found[0])
print("The second password is:",found[1])
