import hashlib
import sys
banana=0
pre = "ckczppom"

#part 1
while True:
    m = hashlib.md5()
    m.update((pre+str(banana)).encode('utf-8'))

    x = m.hexdigest()
    if(x.startswith("00000")):
        print (str(banana)+" "+x)
        break
    
    banana = banana + 1


#part 2
while True:
    m = hashlib.md5()

    m.update((pre+str(banana)).encode('utf-8'))
    
    x = m.hexdigest()
    if(x.startswith("000000")):
        print (str(banana)+" "+x)
        break
    
    banana = banana + 1
