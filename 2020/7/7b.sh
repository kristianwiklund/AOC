#!/bin/bash



function l() {
    
    cat $1 | grep -v contain | sed 's/bags/bag/' | grep -v "shiny gold" | sed "s/^\([ a-z]*\) \(.*\)/s#\1s*#*\2#/"

    # | cut -d ' ' -f 1-3 | sed 's/bags/bag/' | sed 's#\(.*\)#s/\1/shiny gold bag/#'  > tmp
}

function b() {

    until diff "in" "out" > /dev/null; do
	echo "bopp"
	cp in result
	mv "out" "in"
	cat in | tr -d '.' |sed 's/contain no other bags/1/' | grep -v "[0-9] shiny gold" | tr ',' '+' > tmp3

	l tmp3 > pattern
	mv tmp3 tmp4
	touch tmp3
	
	until diff tmp3 tmp4 > /dev/null; do
	    mv tmp4 tmp3
	    sed -f pattern < tmp3  | grep -v "^*"  > tmp4
	done
	
	grep -v "[0-9]$" < tmp4 | grep -v ")$"  > out
	
#	egrep "[0-9]$" < tmp4  | sed 's/^\(.*\) contains*/\1 (1+/' | sed 's/$/)/' >> out
	egrep "[0-9])*$" < tmp4  | sed 's/^\(.*\) contains*/\1 (1+/' | sed 's/$/)/' >> out


	Y=`grep "^shiny gold" result`
	X=`grep "^shiny gold" result | sed 's/bags//' | grep -v bag`
	echo $Y	
	if [ "a$X" != "a" ]; then
	    echo $X
	    exit
	fi
    done
}
rm -f "in"
touch "in"

 cp input "out"
 b
 grep "shiny gold" result

