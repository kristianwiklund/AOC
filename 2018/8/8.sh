#!/bin/bash

echo "This will dump core, obviously not the right choice :-)"

tr " " "\n" < input.txt > input.tmp

IFS=$'\n'

readnode () {

    local childnodes
    local metadata
    local metadatacount
    local md
    
    # read header
    read childnodes
    read metadatacount
    metadata=0

    if [ 0 -ne $childnodes ]; then
	#	echo "level $1 reading $childnodes nodes"
		    
	for i in {1.. $childnodes}; do
	 #   echo "$i"
	    readnode $(($1+1))
	    metadata=$(($metadata + $?)) 
	    	    
	done
	
    fi

    for i in {1..$metadatacount}; do
	read md
	metadata=$(($metadata + $md)) 
    done
    
    return $metadata

}

readnode 1 < input.tmp
echo $?



