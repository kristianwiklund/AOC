
class Ranges:

    def __init__(self, value=[]):
        if isinstance(value,range):
            value = [value]
            
        self.values = value

        # check if two ranges overlap
    def overlap(self, x, y):
        if x.start == x.stop or y.start == y.stop:
            return False
        return x.start <= y.stop and y.start <= x.stop

    # intersection between two ranges
    # https://stackoverflow.com/questions/6821156/how-to-find-range-overlap-in-python
    def range_intersect(self,range_x,range_y):
        if len(range_x) == 0 or len(range_y) == 0:
            return []
        # find the endpoints
        x = (range_x.start, range_x.stop) # from the first element to the last, inclusive
        y = (range_y.start, range_y.stop)
        # ensure min is before max
        # this can be excluded if the ranges must always be increasing

        # the range of the intersection is guaranteed to be from the maximum of the min values to the minimum of the max values, inclusive
        z = (max(x[0],y[0]),min(x[1],y[1]))
        if z[0] <= z[1]:
            return range(z[0], z[1] ) # to make this an inclusive range
        else:
            return [] # no intersection

    def __and__(self, r2):

        a = []
        
        # this is a list of non-overlapping ranges
        for x in self.values:
            # this is also a list of non-overlapping ranges
            for y in r2.values:
                #print(x,y)
                i = self.range_intersect(x,y)
                #print("i",i)
                if i!=[]:
                    a.append(i)
                    
        a = self.merge(a)
        return Ranges(a)
                    
    def _range(self):
        return self.values
        
    def merge(self, m):

        if len(m)<=1:
            return m

        m = sorted(m, key=lambda x:x.start)
#        print("---",m)
        
        l=m
        m=[]
        # starting point
        a = l.pop(0)
        
        while True:
            if len(l)==0:
                m.append(a)
                break
            
            b = l.pop(0)
            if a.stop < b.start:
                print("a ",a,", and b ",b,", are disjunct, add a to m, set a to b, loop")
                m.append(a) # disjunct, no merge
                a = b
                continue
            elif a.stop>b.stop:
                print("a,",a,", is a superset to b,",b," drop b and continue looking at a")
                # a is a superset to b, remove b, use only a
                continue
            elif a.stop>=b.start:
                # a and b overlaps, merge
                a = range(a.start,b.stop)
                continue
            else:
                print("wtf",a.start,a.stop,b.start,b.stop)
                    
                #        print("m=",m)
        return m
    
    def __add__(self, value):

        if isinstance(value, range):
            p = self.values
            p.append(value)
            p = self.merge(p)
            return Ranges(p)
        else:
            raise ValueError

        
        

    def __str__(self):
        return str(self.values)
        

ap = Ranges(range(1,3))
ap = ap + range(3,4)
assert(ap._range()==[range(1,4)])
ap = ap + range(1,4)
assert(ap._range()==[range(1,4)])
ap = ap + range(5,6)
assert(ap._range()==[range(1,4),range(5,6)])

print("ap1",ap)
ap = ap & Ranges(range(4,5))
print("ap1&(4,5)=",ap)
    

