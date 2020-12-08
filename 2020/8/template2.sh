
	*)
	    echo "Terminated"
	    exit
	    ;;
	esac;
    MemMap[$PC]=1
    let PC++
    printf "| %8s | %8d | %8d |\n" "$I" "$OPC" "$ACC"
    

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
