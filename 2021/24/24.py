import f
import time

start = time.time()

z14=None
for a in range(1,10):
    (w1,x1,y1,z1) = f.i0(a,0,0,0,0)
    for b in range(1,10):
        (w2,x2,y2,z2) = f.i1(b,w1,x1,y1,z1)
        for c in range(1,10):
            (w3,x3,y3,z3) = f.i2(c,w2,x2,y2,z2)
            for d in range(1,10):
                (w4,x4,y4,z4) = f.i3(d,w3,x3,y3,z3)
                
                for e in range(1,10):
                    (w5,x5,y5,z5) = f.i4(e,w4,x4,y4,z4)
                    
                    if z5 > 7000:
                        continue

                    for ff in range(1,10):
                        (w6,x6,y6,z6) = f.i5(ff,w5,x5,y5,z5)

                        if z6 > 172000:
                            continue
                        for g in range(1,10):
                            (w7,x7,y7,z7) = f.i6(g,w6,x6,y6,z6)

                            for h in range(1,10):
                                (w8,x8,y8,z8) = f.i7(h,w7,x7,y7,z7)

                                if z8 > 171600:
                                    continue
                                
                                for i in range(1,10):
                                    (w9,x9,y9,z9) = f.i8(i,w8,x8,y8,z8)
#                                    print(a,b,c,d,e,ff, g, "time =",time.time()-start,z14)                    
                                    if z9 > 6600:
                                        continue
                                    
                                    for j in range(1,10):
                                        (w10,x10,y10,z10) = f.i9(j,w9,x9,y9,z9)

                                        if z10 > 171600:
                                            continue
                                        
                                        for k in range(1,10):
                                            (w11,x11,y11,z11) = f.i10(k,w10,x10,y10,z10)

                                            if z11 > 6600:
                                                continue
                                            
                                            for l in range(1,10):
                                                (w12,x12,y12,z12) = f.i11(l,w11,x11,y11,z11)

                                                if z12>254:
                                                    continue
                                                
                                                for m in range(1,10):
                                                    (w13,x13,y13,z13) = f.i12(m,w12,x12,y12,z12)
                                                    
                                                    if z13>9:
                                                        continue
                                                    
                                                    for nnn in range(1,10):
                                                        (w14,x14,y14,z14) = f.i13(nnn,w13,x13,y13,z13)
                                                        if z14==0:
                                                            print(a,b,c,d,e,ff,g,h,i,j,k,l,m,nnn)
                                                            
