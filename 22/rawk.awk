a=a+1
/cut / {print "D"a+1"=t:rcut(D"a","$2",t:bignum()),"}
/deal with increment / {print "D"a+1"=t:rdwi(D"a",t:bignum(),"$4"),"}
/deal into new stack/ {print "D"a+1"=t:rdealinto(D"a",t:bignum()),"}
END {print "D"a+1"."}
