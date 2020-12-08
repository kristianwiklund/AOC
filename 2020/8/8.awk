# first part of case statement
function pre() {
    print (IC")");
    IC=IC+1;
}
function post() {
    print (";;");
}

BEGIN {IC=0}
/nop/ {pre();post();}
/jmp/ {pre();
    print("let PC=PC+"$2"-1");
    post();}
/acc/ {pre();
    print("let ACC=ACC+"$2"");
    post();}
