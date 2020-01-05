import hashlib
import sys
banana=0
pre = "ckczppom"

while True:
    m = hashlib.md5()
    m.update(pre+str(banana))

    x = m.hexdigest()
    if(x.startswith("000000")):
        print (str(banana)+" "+x)
        sys.exit()
    
    banana = banana + 1
    if (banana % 10000) == 0:
        print (banana)
