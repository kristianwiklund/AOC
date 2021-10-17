#!/bin/bash

IFS=$'\n'

(
    for i in `cat input`;do
	#echo $i
	(
	    (
		(
		    echo $i|tr '\t' '\n'|sort -n|tail -1
		);
		(
		    echo $i|tr '\t' '\n'|sort -nr|tail -1
		)
	    ) |paste -s -d- -
	) | bc
    done
)|paste -s -d+ -|bc
