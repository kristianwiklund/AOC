-module(ic).
%%-export([two/1]).
-export([readfile/1]).
-export([run/2]).
-export([datan/0]).
-export([datan2/0]).
-export([setnth/3]).
-export([mod/4]).
-export([t/4]).

setnth(1, [_|Rest], New) ->
    [New|Rest];
setnth(I, [E|Rest], New) -> 
    [E|setnth(I-1, Rest, New)].


readfile(FileName) ->
		   {ok, Binary} = file:read_file(FileName),
		   string:tokens(erlang:binary_to_list(Binary), ",\n").


getparams([X|XS],[L|LS],O,PAR,Rel) ->

    if ((X==48) and (XS == [])) ->
	    getparams([],[L|LS],O,PAR,Rel);
       true ->
	    case X of
		48 ->		   

		    V = lists:nth(L+1,O),
		    %io:fwrite("0: O[~B]=~B\n", [L+1,V]),
		    getparams(XS,LS,O,[V|PAR],Rel);
		49 ->
		    %io:fwrite("1: V=~B\n", [L]),
		    getparams(XS,LS,O,[L|PAR],Rel);
		50 ->
		    Addr = Rel+L,
		    V = lists:nth(Addr+1,O),
		    %io:fwrite("2: O[~B] = ~B\n", [Addr+1,V]),
		    getparams(XS,LS,O,[V|PAR],Rel)
	    end
			       end;
getparams(_,L,O,PAR,Rel) ->
    Y = PAR,
    Z = Y,
    TT = lists:reverse(Z),
    {TT,L}.



r2(1,[A,B,C|L],O,Pid,Rel,WM) ->
    X = lists:nth(A+1,O)+lists:nth(B+1,O),
    P = setnth(C+1,O,X),
    L1 = lists:nthtail(length(P)-length(L),P),
    PC = length(P)-length(L),
    %io:fwrite("~B: add ~B ~B -> ~B=~B\n", [PC,A,B,C,X]),
    %%io:write(L1),
    r(L1,P,Pid,Rel);
r2(2,[A,B,C|L],O,Pid,Rel,WM) ->
    %%io:fwrite("*"),
    X = lists:nth(A+1,O)*lists:nth(B+1,O),
    %io:fwrite("mul ~B ~B -> ~B=~B\n", [A,B,C,X]),
    P = setnth(C+1,O,X),
    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel);

r2(3,[A|L],O,Pid,Rel,WM) ->

    %io:fwrite("wait for message"),
    if 
	Pid == undefined ->
	    {ok,B}=io:read('enter>'),
	    P = setnth(A+1,O,B),
	    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel);
       true ->
	    receive
		B ->
						%io:fwrite("got ~B\n",[B]),
		    P = setnth(A+1,O,B),
		    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel)
	    end
    end;
r2(203, [A|L],O,Pid,Rel,WM) ->
%    {ok,B}=io:read('enter>'),
    %io:fwrite("~w ~A",[INPUT,A]),

    if 
	Pid == undefined ->
	    {ok,B}=io:read('enter>'),
	    %io:fwrite("set rel position ~B\n",[A+1+Rel]),
	    P = setnth(A+1+Rel,O,B),
	    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel);
       true ->
	    receive
		B ->
						%io:fwrite("got ~B\n",[B]),
		    P = setnth(A+1+Rel,O,B),
		    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel)
	    end
    end;




r2(4,[A|L],O,Pid,Rel,WM) ->
    X = lists:nth(A+1,O),
    %io:fwrite("~B\n", [X]),
    %io:fwrite("send ~B\n",[X]),
    if Pid == undefined ->
	    io:fwrite("output: ~B\n", [X]);
       true -> 
	    Pid ! X
    end,

    r(lists:nthtail(length(O)-length(L),O),O,Pid,Rel);
r2(5,[A,B|L],O,Pid,Rel,WM) ->
    X = lists:nth(A+1,O),
    Y = lists:nth(B+1,O),
    
    %io:fwrite("jump-if-true(P) ~B->~B\n", [X,Y]),
    
    if 
	X =/= 0 ->
	    L1 = lists:nthtail(Y,O);
	true  ->
	    L1 = lists:nthtail(length(O)-length(L),O)
    end,
    r(L1,O,Pid,Rel);
r2(6,[A,B|L],O,Pid,Rel,WM) ->
    X = lists:nth(A+1,O),
    Y = lists:nth(B+1,O),
    
    %io:fwrite("jump-if-false(P) ~B->~B\n", [X,Y]),
    
    if 
	X == 0 ->
	    L1 = lists:nthtail(Y,O);
	true  ->
	    L1 = lists:nthtail(length(O)-length(L),O)
    end,
    r(L1,O,Pid,Rel);
r2(7,[A,B,C|L],O,Pid,Rel,WM) ->
    X = lists:nth(A+1,O),
    Y = lists:nth(B+1,O),
    
    if
	X < Y ->
	    V = 1;
	true ->
	    V = 0
    end,
    P = setnth(C+1,O,V),    
    L1 = lists:nthtail(length(P)-length(L),P),
    r(L1,P,Pid,Rel);
r2(8,[A,B,C|L],O,Pid,Rel,WM) ->
    X = lists:nth(A+1,O),
    Y = lists:nth(B+1,O),
    
    if
	X == Y ->
	    V = 1;
	true ->
	    V = 0
    end,
    P = setnth(C+1,O,V),    
    L1 = lists:nthtail(length(P)-length(L),P),
    r(L1,P,Pid,Rel);

r2(9,[A|L],O,Pid,Rel,WM) ->
    X = lists:nth(A+1,O),
    %io:fwrite("set rel =  ~B\n",[X]),
    r(L,O,Pid,A); 

r2(109,[A|L],O,Pid,Rel,WM) ->
    %io:fwrite("set rel =  ~B\n",[A]),
    r(L,O,Pid,A); 

r2(104,[A|L],O,Pid,Rel,WM) ->
    %io:fwrite("send ~B\n",[A]),
    
    if Pid == undefined ->
	    io:fwrite("output: ~B\n", [A]);
       true -> 
	    Pid ! A
    end,
    r(lists:nthtail(length(O)-length(L),O),O,Pid,Rel);
r2(204,[A|L],O,Pid,Rel,WM) ->
    %io:fwrite("send rel from position ~B memlen=~B\n",[A+1+Rel,length(O)]),
    X = lists:nth(A+1+Rel,O),
    if Pid == undefined ->
	    io:fwrite("output: ~B\n", [X]);
       true -> 
	    Pid ! X
    end,
    r(lists:nthtail(length(O)-length(L),O),O,Pid,Rel);
r2(99,_,O,Pid,Rel,WM) ->
    %io:fwrite("byebye"),
    if 
	Pid == undefined ->
	    ok;
	true ->
	    exit(normal)
	end;
r2(I,L,O,Pid,Rel,WM) ->
    {I,L,O}.

r2(1,INPUT,[A,B,C|L],O,Pid,Rel,WM) ->
    %{1,INPUT,[C|L],O};
    %%io:fwrite("+"),
    X = lists:nth(1,INPUT)+lists:nth(2,INPUT),
    if 
	WM == false ->
	    P = setnth(C+1,O,X);
	true ->
	    Offset = C+Rel,
	    P = setnth(Offset+1,O,X)
    end,

    %io:fwrite("add ~B ~B -> ~B=~B\n", [lists:nth(1,INPUT),lists:nth(2,INPUT),C,X]),
    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel);
r2(2,INPUT,[A,B,C|L],O,Pid,Rel,WM) ->
    %%io:fwrite("*"),
    %io:fwrite("~w\n",[INPUT]),
    X = lists:nth(1,INPUT)*lists:nth(2,INPUT),
    %P = setnth(C+1,O,X),
    if 
	WM == false ->
	    P = setnth(C+1,O,X);
	true ->
	    Offset = C+Rel,
	    P = setnth(Offset+1,O,X)
    end,
    %io:fwrite("mul ~B ~B -> ~B=~B\n", [A,B,C,X]),
    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel);

r2(3,INPUT, [A|L],O,Pid,Rel,WM) ->
%    {ok,B}=io:read('enter>'),
    %io:fwrite("~w ~A",[INPUT,A]),

    if 
	Pid == undefined ->
	    {ok,B}=io:read('enter>'),
	    P = setnth(A+1,O,B),
	    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel);
       true ->
	    receive
		B ->
						%io:fwrite("got ~B\n",[B]),
		    P = setnth(A+1,O,B),
		    r(lists:nthtail(length(P)-length(L),P),P,Pid,Rel)
	    end
    end;

    
r2(5,INPUT,[A,B|L],O,Pid,Rel,WM) ->
    X = lists:nth(1, INPUT),
    Y = lists:nth(2, INPUT),
    
    if 
	X =/= 0 ->
	    %io:fwrite("jump-if-true ~B->~B, O=~B\n", [X,Y,length(O)]),
	    L1 = lists:nthtail(Y,O);
	true  ->
	    %io:fwrite("jump-if-true (stay) check: ~B, untranslated: ~B, rel: ~B, O[~B]=~B\n",[X,A,Rel,
            %										     Rel+A,
	%										      lists:nth(Rel+A+1,O)]),
										   
	    L1 = L
    end,
    %{L1,O};
    r(L1,O,Pid,Rel);
r2(6,INPUT,[A,B|L],O,Pid,Rel,WM) ->
    X = lists:nth(1, INPUT),
    Y = lists:nth(2, INPUT),
    
    if 
	X == 0 ->
	    %io:fwrite("jump-if-false ~B->~B\n", [X,Y]),
	    L1 = lists:nthtail(Y,O);
	true  ->
	    %io:fwrite("jump-if-false ~B (stay)\n",[X]),
	    L1 = L
    end,
    r(L1,O,Pid,Rel);
r2(7,INPUT, [A,B,C|L],O,Pid,Rel,WM) ->
    X = lists:nth(1, INPUT),
    Y = lists:nth(2, INPUT),    
    if
	X < Y ->
	    V = 1;
	true ->
	    V = 0
    end,

	    
    if 
	WM == false ->
	    P = setnth(C+1,O,V);
	true ->
	    Offset = C+Rel,
	    P = setnth(Offset+1,O,V)
    end,

    L1 = lists:nthtail(length(P)-length(L),P),

    %if WM ->
	    %io:fwrite("check_if_lessthan ~B,~B->~B, rel=~w,O[~B]=~B,P[~B]=~B\n", 
	%	      [X,Y,V,WM,Rel+C,lists:nth(Rel+C+1,O),Rel+C,lists:nth(Rel+C+1,P)]);
       %true -> 
%	    XYZ=false
		
 %   end,

    r(L1,P,Pid,Rel);


r2(8,INPUT,[A,B,C|L],O,Pid,Rel,WM) ->
    Y = lists:nth(1, INPUT),
    X = lists:nth(2, INPUT),    
    
    if
	X == Y ->
	    V = 1;
	true ->
	    V = 0
    end,

    %io:fwrite("check_if_equal ~B,~B->~B\n", [X,Y,V]),
    if 
	WM == false ->
	    P = setnth(C+1,O,V);
	true ->
	    Offset = C+Rel,
	    P = setnth(Offset+1,O,V)
    end,
    %P = setnth(C+1,O,V),    
    L1 = lists:nthtail(length(P)-length(L),P),
    r(L1,P,Pid,Rel);

r2(9,INPUT,[A|L],O,Pid,Rel,WM) ->
    Y = lists:nth(1, INPUT),
    r(L,O,Pid,Rel+Y);


r2(99,_,_,O,Pid,Rel,WM) ->
    %io:fwrite("byebye"),
    if 
	Pid == undefined ->
	    ok;
	true->
	    exit(normal)
end.

r([I|L],O,Pid,Rel) ->
    S = lists:reverse(integer_to_list(I)),
    SL = length(S),
    %%io:write(S),
    %%io:write(","),
    if
	((SL>2) and (I =/= 104) and (I =/= 204) and (I =/= 203)) ->
	    [A,B|XXX] = S,
	
	    if 
		length(XXX) == 1 ->
		    X = string:concat(XXX,"0");
		true -> 
		    X = XXX
	    end,
	    %io:fwrite("opc ~B: ~p->~p (rel=~B) Mode=~p\n",[I,lists:reverse(S),X,Rel,XXX]),
	    {INPUT,L2} = getparams(X,L,O,[],Rel),
	    II = list_to_integer([B,A]),
	    %{II,X,L,O};
	    %%io:write({II,INPUT,L,O}),
	    WM = ((lists:nth(1,lists:reverse(X))==50) and (length(X)==3)),
	    %io:fwrite("--- end opc ~B WM=~w, l(X)=~B---\n", [I,WM,length(X)]),
	    r2(II,INPUT,L,O,Pid,Rel,WM);
	true ->
	    %%io:write({I,L,O}),
	    r2(I,L,O,Pid,Rel,false)
    end.

	
%%Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).

run(OP,Pid) ->
    O1 = array:from_list(OP,0), 
    O = array:to_list(array:set(1100,0,O1)),
    r(O,O,Pid,0),
    ok.

mod(X,Y,O,Pid) ->
    OP = setnth(2,O,X),
    OR = setnth(3,OP,Y),
    run(OR,Pid).

%----------------------------------------------------------------------------------------

datan() ->
    [3,8,1001,8,10,8,105,1,0,0,21,42,51,76,93,110,191,272,353,434,99999,3,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,3,9,1001,9,4,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,5,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99].


datan2() ->
    [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0].

t(P,X,Y,Pid) ->
    R = lists:nth(1,mod(X,Y,P,Pid)).
    
datan5() ->
    [3,225,1,225,6,6,1100,1,238,225,104,0,
     1101,78,5,225,1,166,139,224,101,-74,224,224,4,224,
     1002,223,8,223,1001,224,6,224,1,223,224,223,1002,136,18,224,101,-918,224,224,4,224,
     1002,223,8,223,101,2,224,224,1,224,223,223,1001,83,84,224,1001,224,-139,224,4,224,
     102,8,223,223,101,3,224,224,1,224,223,223,1102,55,20,225,1101,53,94,225,2,217,87,224,1001,224,-2120,224,4,224,
     1002,223,8,223,1001,224,1,224,1,224,223,223,102,37,14,224,101,-185,224,224,4,224,
     1002,223,8,223,1001,224,1,224,1,224,223,223,1101,8,51,225,1102,46,15,225,1102,88,87,224,1001,224,-7656,224,4,224,
     102,8,223,223,101,7,224,224,1,223,224,223,1101,29,28,225,1101,58,43,224,1001,224,-101,224,4,224,
     1002,223,8,223,1001,224,6,224,1,224,223,223,1101,93,54,225,101,40,191,224,1001,224,-133,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,40,79,225,4,223,
     99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,434,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,494,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,539,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,7,677,677,224,1002,223,2,223,1005,224,599,101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,644,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226].
