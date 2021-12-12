BEGIN {dx=0;dy=-1;x=0;y=0}
/R/ {t=dx;dx=-dy;dy=t;x=x+$2*dx;y=y+$2*dy}
/L/ {t=dx;dx=dy;dy=-t;x=x+$2*dx;y=y+$2*dy}
END {print x+y}
