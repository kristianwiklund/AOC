-module(t).
-export([las/4,las/1,t/0,t2/0]).

las([X|XS],Prev, Cnt, Acc) when X == Prev -> 
    las(XS, Prev, Cnt+1, Acc);
las([X|XS], Prev, Cnt, Acc) when X =/= Prev -> 
    AccP = [[Cnt, Prev]|Acc],
    las(XS, X, 1, AccP);
las(_,Prev,Cnt,Acc) -> 
    [[Cnt, Prev]|Acc].
	 

las([X|XS]) ->
    lists:flatten(lists:reverse(las([X|XS],X,0,[]))).

tx(R) ->
    INPUT = [1,1,1,3,2,2,2,1,1,3],
    
    T = lists:foldl(fun(X, Acc) ->
			    T= las(Acc),
			    io:fwrite("~B: ~B\n",[X,length(T)]),
			    T
			    
		    end,
		    INPUT,
		    lists:seq(1,R)),
    io:fwrite("\nFinal length: ~B",[length(T)]).
    
t() ->
    tx(40).

t2() ->
    tx(50).
