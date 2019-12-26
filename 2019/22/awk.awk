a=a+1
/cut / {print "D"a+1"=t:cut(D"a","$2"),"}
/deal with increment / {print "D"a+1"=t:dealwithincrement(D"a","$4"),"}
/deal into new stack/ {print "D"a+1"=t:dealinto(D"a"),"}
END {print "D"a+1"."}
