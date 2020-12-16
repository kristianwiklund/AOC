function s(spec) {
    split(spec,a,"-");
    printf("(x >=%s and x <=%s) ",a[1],a[2])
}

	{
	    printf("    l.append(((")
	    for (i=2;i<=NF;i++) {
		s($i);
		printf(" or ");
	    }
	    printf(" False ),\"%s\"))\n",$1);	   
	}

