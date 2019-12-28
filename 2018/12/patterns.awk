BEGIN {
    print "-module(matcher).";
    print "-export([match/1]).";
}
{
    split($1,a,"");
    print("%",$1);
    printf("match([A,B,C,D,E|STR], Acc) when {");
    for (i=1;i<6;i++) {
	if (a[i] != "_")
	    printf("$%s,",a[i]);
       
    }
    printf("$T} == {");

    for (i=1;i<6;i++) {
	if (a[i] != "_")
	    printf("%c,",64+i);       
    }
    print "$T} ->"
    

    print "REM = [B,C,D,E|STR],";
    print "match(REM,\""$2"\"++Acc);";
}
END {print "match([_|STR],Acc) ->";
	print "match(STR,\".\"++Acc);"
	print "match(_,Acc) -> Acc.";
	print "match(S) -> lists:reverse(match(lists:flatten(io_lib:format(\".....~s.....\",[S])),\"..\"))."
}

