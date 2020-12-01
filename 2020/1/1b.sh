for i in `cat input`; do
    for j in `grep -v $i input`; do
	T=`expr 2020 - $j - $i`
	if grep -- "^$T\$" input > /dev/null; then
	    echo $i $j $T | tr ' ' '*'|bc
	fi
    done
done


#grep "^`expr 2020 - $i`\$" input; done;echo -n 1)|echo `tr '\n' '*'`|bc
