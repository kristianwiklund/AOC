def f(s):
   x=0
   y=0
   z=0
   w=0

   return (w,x,y,z)

def i0(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=1;
   x+=14;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=7;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i1(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=1;
   x+=12;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=4;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i2(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=1;
   x+=11;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=8;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i3(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=26;
   x+=-4;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=1;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i4(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=1;
   x+=10;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=5;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i5(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=1;
   x+=10;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=14;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i6(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=1;
   x+=15;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=12;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i7(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=26;
   x+=-9;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=10;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i8(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=26;
   x+=-9;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=5;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i9(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=1;
   x+=12;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=7;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i10(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=26;
   x+=-15;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=6;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i11(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=26;
   x+=-7;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=8;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i12(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=26;
   x+=-10;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=4;
   y*=x;
   z+=y;
   return (w,x,y,z)

def i13(s, w,x,y,z):
   w=s
   x=0;
   x+=z;
   x%=26;
   z//=26;
   x=1 if x==w else 0
   x=1 if x==0 else 0
   y=0;
   y+=25;
   y*=x;
   y+=1;
   z*=y;
   y=0;
   y+=w;
   y+=6;
   y*=x;
   z+=y;
   return (w,x,y,z)
