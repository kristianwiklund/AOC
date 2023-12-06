
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
    def range_intersect(range_x,range_y):
        if len(range_x) == 0 or len(range_y) == 0:
            return []
        # find the endpoints
        x = (range_x[0], range_x[-1]) # from the first element to the last, inclusive
        y = (range_y[0], range_y[-1])
        # ensure min is before max
        # this can be excluded if the ranges must always be increasing
        x = tuple(sorted(x))
        y = tuple(sorted(y))
        # the range of the intersection is guaranteed to be from the maximum of the min values to the minimum of the max values, inclusive
        z = (max(x[0],y[0]),min(x[1],y[1]))
        if z[0] < z[1]:
            return range(z[0], z[1] + 1) # to make this an inclusive range
        else:
            return [] # no intersection


    def merge(self, m):

        if len(m)<=1:
            return m

        m = sorted(m, key=lambda x:x.start)

        loop=True
        while loop:
            l = m
            m = []
            loop=False
            if len(l)<=1:
                return l
        
            for i in range(len(l)-1):
                if l[i].stop<l[i+1].start:
                    m.append(l[i])
                else:
                    m.append(range(l[i].start, l[i+1].stop))
                    loop=True

            m = sorted(m, key=lambda x:x.start)

        return m
                                           

    def __and__(self, value):

        if isinstance(value, range):
            self.values.append(value)
            self.values = self.merge(self.values)
            return self
        else:
            raise ValueError

        

    def __str__(self):
        return str(self.values)
        

ap = Ranges(range(1,3))
ap = ap & range(3,4)
print(ap)


            
    

