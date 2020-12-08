
	*)
	    echo "Segmentation fault"
	    exit
	    ;;
	esac;
    MemMap[$PC]=1
    let PC++
}

function run() {

    # need a check here to terminate
    PC=0
    ACC=0
    
    while [ -z ${MemMap[$PC]}  ]; do

	cpu

	
	
    done
    
}

run
