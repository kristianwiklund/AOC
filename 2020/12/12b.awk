function abs(v) {return v < 0 ? -v : v}
BEGIN {sx=0;sy=0;x=10;y=-1;PI=atan2(0,-1)}
/N/ {y=y-$2;print $1,x,y;}
/E/ {x=x+$2;print $1,x,y;}
/W/ {x=x-$2;print $1,x,y;}
/S/ {y=y+$2;print $1,x,y;}
/R 90/ {t = y;y=x;x=-t}
/L 270/ {t = y;y=x;x=-t}
/R 180/ {y=-y;x=-x}
/L 180/ {y=-y;x=-x}
/R 270/ {t = y;y=-x;x=t}
/L 90/ {t = y;y=-x;x=t;print $1,x,y;}


/F/ {sx=sx+$2*x;sy=sy+$2*y;print $1,$2,"wp=("x,y")","s=("sx,sy")"}
END {print sx,sy,abs(sx)+abs(sy)}
