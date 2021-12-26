#!/usr/bin/python3
import f


# test av i13 - resultat: z in måste vara mindre än 10
# test av i12 - resultat: z in måste vara mindre än 254
# test av i11 - resultat: z in måste vara mindre än 6600
# test av i10 - resultat: z in måste vara mindre än 171600
# i9 - z in måste vara mindre än 6600
# i8 - z in måste vara mindre än 171600
# i7 - z in måste vara mindre än 171600
# i6 6600
# i5 253
vom = set()
for i in range(1,10):
    for j in range (0,1000000):
        (w,x,y,z) = f.i5(i,-1,-1,-1,j)
        if z < 6600:
            vom.add(j)
            print(i,j, max(vom))
