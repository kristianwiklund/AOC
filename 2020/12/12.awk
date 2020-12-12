function abs(v) {return v < 0 ? -v : v}
BEGIN {a=90;x=0;y=0;PI=atan2(0,-1)}
/N/ {y=y-$2;print $1,a,x,y;}
/E/ {x=x+$2;print $1,a,x,y;}
/W/ {x=x-$2;print $1,a,x,y;}
/S/ {y=y+$2;print $1,a,x,y;}
/R/ {a=a+$2;print $1,a,x,y}
/L/ {a=a-$2;print $1,a,x,y}
/F/ {dx=$2*sin(a * PI / 180.0);dy=-$2*cos(a * PI / 180.0);x=x+dx;y=y+dy;print $1,a,x,y,dx,dy}
END {print x,y,abs(x)+abs(y)}
