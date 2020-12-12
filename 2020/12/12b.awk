function abs(v) {return v < 0 ? -v : v}
BEGIN {a=90;sx=0;sy=0;x=10;y=-1;PI=atan2(0,-1)}
/N/ {y=y-$2;print $1,a,x,y;}
/E/ {x=x+$2;print $1,a,x,y;}
/W/ {x=x-$2;print $1,a,x,y;}
/S/ {y=y+$2;print $1,a,x,y;}
/R/ {a=$2*PI/180.0; x=x*sin(a * PI / 180.0);y=-y*cos(a * PI / 180.0);print $1,"a="a,"wp=("x,y")","sh=("sx,sy")"}
/L/ {a=-$2*PI/180.0; x=x*sin(a * PI / 180.0);y=-y*cos(a * PI / 180.0);print $1,"a="a,"wp=("x,y")","sh=("sx,sy")"}
/F/ {sx=sx+$2*x;sy=sy+2*y;print $1,a,x,y,sx,sy}
END {print x,y,abs(x)+abs(y)}
