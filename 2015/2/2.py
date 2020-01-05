import hashlib
import sys
banana=0
pre = "ckczppom"

while True:
    m = hashlib.md5()
    m.update(pre+str(banana))

    if(m.hexdigest().startswith("00000")):
        print (banana)
        sys.exit()
    
    banana = banana + 1
    if (banana % 10000) == 0:
        print (banana)
