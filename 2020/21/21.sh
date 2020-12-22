#!/bin/bash

#cat $1 | sed 's/contains //g' | python3 21.py

cat $1 | cut -d"(" -f 1 | tr ' ' '\n' | sort -u | grep -v '^$' > tmp
ITC=`wc -l tmp|cut -d ' ' -f1`
IT=`cat tmp | tr '\n' ' '`

cat $1 | cut -d "(" -f2 | tr -d ")," | sed 's/contains //' |  tr ' ' '\n' | sort -u | grep -v '^$' > tmp2

OTC=`wc -l tmp2|cut -d ' ' -f1`
OT=`cat tmp2 | tr '\n' ' '`

function l() {
    line=$1
    
    for i in $IT; do
	if [[ $line == *$i* ]] ; then
	    echo -n "1"
	else
	    echo -n "0"
	fi
    done

    echo -n " "
    for i in $OT; do
	if [[ $line == *$i* ]] ; then
	    echo -n "1"
	else
	    echo -n "-"
	fi
    done
    echo ""
	
}

# consume the file line by line

(
    echo ".i $ITC"
    echo ".ilb $IT"

    echo ".o $OTC"
    echo ".ob $OT"

    echo ".type fd"

    while IFS=$'\n' read -r line; do
	l "$line"
    done < $1
#l "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)"
#l "trh fvjkl sbzzf mxmxvkd (contains dairy)"
#l "sqjhc fvjkl (contains soy)"
#l "sqjhc mxmxvkd sbzzf (contains fish)"

    echo ".e"
) > tmp.esp

espresso tmp.esp > esp.result

# from https://stackoverflow.com/questions/12633522/prevent-bc-from-auto-truncating-leading-zeros-when-converting-from-hex-to-binary
paddy()
{
    how_many_bits=$1
    read number
    zeros=$(( $how_many_bits - ${#number} ))
    for ((i=0;i<$zeros;i++)); do
    echo -en 0
    done && echo $number
}

G="1"
echo $IT
rm -f tmp5
for i in $OT; do
    #echo $G
    grep "^[01]* $G" esp.result | grep -v "^[.] " > tmp4
    (echo "obase=2";echo $((`cat tmp4  | cut -d ' ' -f 1 | sed 's/^/2#/' | tr '\n' '&'|sed 's/&$//'`)))| bc | paddy $ITC >> tmp5
    G="."$G
done

# bitwise or on all lines in tmp5

(echo "obase=2";echo $((`cat tmp5 | sed 's/^/2#/' | tr '\n' '|'|sed 's/|$//'`))) | bc | paddy $ITC | sed 's/\(.\)/\1 /g' > tmp6
read -a A < tmp6
#echo ${A[@]}

c=0
(for i in $IT; do
    if [[ ${A[$c]} == "0" ]]; then
	echo $i
    fi
    let c++
 done) | sed 's/^/^/' | sed 's/$/$/' > tmp7

cat $1 | tr ' ' '\n'  > tmp8

grep -f tmp7 tmp8 | wc -l

# 2425 is not correct
