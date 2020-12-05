-module(fem).
-export([one/1]).
-export([two/1]).
-export([rc/3]).
-export([calc/1]).

rc([R|RS], Len, Row) ->
    {L,U} = lists:split(Len div 2,Row),

    case R of 
	70->
	    rc(RS,Len div 2,L);
	66->
	    rc(RS,Len div 2,U);
	76->
	    rc(RS,Len div 2,L);
	82->
	    rc(RS,Len div 2,U)
    end;
rc(_,_,[R|_]) ->
    R.



calc([A,B,C,D,E,F,G,H,I,J]) ->
    R=rc([A,B,C,D,E,F,G],128,lists:seq(0,127)),
    S=rc([H,I,J],8,lists:seq(0,7)),
    {R,S,R*8+S};
calc(_) ->
    false.

one([X|XS],Acc) ->
    one(XS, [calc(X)|Acc]);
one(_,Acc) ->
    Acc.
one(X) ->
    [{_,_,Id}|_] = lists:reverse(lists:keysort(3,one(X,[]))),
    Id.

two(X) ->
    L1=lists:keysort(3,one(X,[])),
    L2=lists:map(fun({_,_,Id}) ->
			 Id
		 end, L1),
    {Min,Max}={lists:min(L2),lists:max(L2)},
    R2=sets:from_list(lists:seq(Min,Max)),
    R1=sets:from_list(L2),
    sets:to_list(sets:subtract(R2,R1)).
    


    

    
