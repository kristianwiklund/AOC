a=a+1
/cut / {print "D"a+1"=t:mcut(D"a","$2"),"}
/deal with increment / {print "D"a+1"=t:mdwi(D"a","$4"),"}
/deal into new stack/ {print "D"a+1"=t:mrdealinto(D"a"),"}
END {print "D"a+1"."}
