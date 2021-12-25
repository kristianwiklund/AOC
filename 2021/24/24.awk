BEGIN {g=0;print "def f(s):\n   x=0\n   y=0\n   z=0\n   w=0\n"}

/inp / {print "   "$2"=int(s["g"]);";g=g+1;}
/add / {if ($3!=0) {print "   "$2"+="$3";"}}
/mul / {if ($3!=0) {print "   "$2"*="$3";"} else {print "   "$2"=0;"}}
/div / {print "   "$2"//="$3";"}
/mod / {print "   "$2"%="$3";"}
/eql / {print "   "$2"=1 if "$2"=="$3" else 0"}
END {print("   return z;")}



