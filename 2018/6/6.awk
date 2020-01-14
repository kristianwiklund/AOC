
    function abs(a,b)
    {
	return a<b?b-a:a-b
    }

BEGIN {a=0}
{x[a]=$1;y[a]=$2;a++}
END {


    
    for (i=0;i<a;i++)
    {
	mkm["MaxX"i] = 0
	mkm["MaxY"i] = 0
	mkm["MinX"i] = 0
	mkm["MinY"i] = 0
	p[i] = 0
	
	for (j=0;j<a;j++)
	{
	    mkm["MaxX"i] = mkm["MaxX"i] || (x[i] < x[j])
	    mkm["MinX"i] = mkm["MinX"i] || (x[i] > x[j])
	    mkm["MaxY"i] = mkm["MaxY"i] || (y[i] < y[j])
	    mkm["MinY"i] = mkm["MinY"i] || (y[i] > y[j])

	    
	    
	    # which are the intersection lines between the respective areas?
	    # the areas of each dot becomes
	    # 3/4 of a circle NOT in conflict with the other dot
	    # 1/4 of a circle in conflict with the other dot, from this a triangle remains
	    # the size of this triangle is R*R/2
	    # hence, the area that belong only to one dot in a two dot scenario is
	    # 2*PI*R*R - (2*PI*R*R/4) + R*R/2 = PI*R*R *(8-2)/4 + R*R/2
	    # = PI*R*R*3/2+R*R/2 = R*R*(3*PI/2+1/2) = R*R*(1/2)*(3*PI+1)

	    # each dot is limited by its closest neighbors
	    # as the size goes into infinity, we get a "star" of straight lines that are intersecting
	    # and form the area for the non-infinite dots
	    
	    
	    
	    
	    
	}

	mkm[i] =  mkm["MaxX"i]  &&  mkm["MinX"i]  && mkm["MaxY"i] && mkm["MinY"i]
	
	if  (mkm[i]) {
	    print i":"
	    
	}
	

    }

}

