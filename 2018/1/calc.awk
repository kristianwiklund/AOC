BEGIN {f=0}

{
    f=f+$1
    apa[f]=apa[f]+1
    if(apa[f]==2) {
	print f
	exit
    }

}

