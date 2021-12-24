BEGIN {g=13;print "#include \"24.h\"\nint f(){int w=0,x=0,y=0,z=0;"}
/inp / {print $2"=s["g"];";g=g-1;}
/add / {if ($3>0) {print $2"+="$3";"}}
/mul / {if ($3!=0) {print $2"*="$3";"} else {print $2"=0;"}}
/div / {print $2"/="$3";"}
/mod / {print $2"%="$3";"}
/eql / {print $2"=(("$2"=="$3")?1:0);"}
END {print("return (z);}")}



