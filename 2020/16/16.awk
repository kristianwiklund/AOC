function s(spec) {
    split(spec,a,"-");
    printf("(x >=%s and x <=%s) ",a[1],a[2])
}

	{
	    printf("(");
	    for (i=1;i<=NF;i++) {
		s($i);
		printf(" or ");
	    }
	    printf(" False) or ");	   
	}

