from math import *
import numpy as np

class snafu():
    def __init__(self,i):
        if isinstance(i,int):
            self.value = self.i2s(i)
        elif isinstance(i,str):
            self.value = i
        else:
            raise ValueError("Cannot convert to snafu from"+str(type(i)))

    # convert to int
    def __int__(self):
        return self.s2i()

    # comparison operator for the asserts
    def __eq__(self, other):
        if isinstance(other,snafu):
            return self.value == other.value
        elif isinstance(other,str):
            return self.value == other
        elif isinstance(other,int):
            p = snafu(other)
            return self==p

    # convert integer to snafu, this is the tricky one
    # from the input, it looks like there are no negative numbers as such
    def i2s(self,i):

        ii=i

        v = {
            2:"2",
            1:"1",
            0:"0",
            -1:"-",
            -2:"="
        }

        # trivial case
        if i in v:
            return v[i]

        # find the longest snafu needed to represent i
        m = ceil(log(i,5))
        if i<=2*(5**(m-1)):
            m-=1
            
        l = [5**x for x in range(m+1)]
        l.reverse()
        brum=""

        for x in l:
            p = i//x
#            print(i,"//",x,"=",p,"i+x//2",i+x//2,"2*x",2*x)

            if (i+x//2)>=2*x:
                brum+="2"
                i-=2*x
                continue
            
            if (i+x//2)>=x:
                brum+="1"
                i-=x
                continue

            if (i-x//2)<=-2*x:
                brum+="="
                i+=2*x
                continue

            if (i-x//2)<=-x:
                brum+="-"
                i+=x
                continue

            brum+="0"
            #            print("_,i,p",i,p)
                
        brum=brum.lstrip("0")
        # self test
        #print(brum)
        #print("snafu(",ii,")=",brum,"reverse =",int(snafu(brum)))
                
        assert(ii==int(snafu(brum)))
        return(brum)
            
    # convert snafu to integer, simple table lookup
    def s2i(self):
        
        v = {
            "2":2,
            "1":1,
            "0":0,
            "-":-1,
            "=":-2
            }
        
        # convert
        k = [v[x] for x in self.value[::-1]]
        l = [5**x for x in range(len(k))]
        z = zip(k,l)
        s = [x*y for x,y in z]
        return sum(s)

    def __str__(self):
        return self.value

