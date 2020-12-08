
	*)
	    echo "Terminated"
	    exit 0
	    ;;
	  esac;
 
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
    echo "Crash"
    echo "PC: $PC - ${MemMap[$PC]} "
    exit 1
    
}

run
