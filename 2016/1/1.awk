BEGIN {dx=0;dy=-1;x=0;y=0}
/R/ {t=dx;dx=-dy;dy=t;for(i=0;i<$2;i++){x=x+dx;y=y+dy;print "P", x,y}}
/L/ {t=dx;dx=dy;dy=-t;for(i=0;i<$2;i++){x=x+dx;y=y+dy;print "P", x,y}}
END {print sqrt(x*x)+sqrt(y*y)}
