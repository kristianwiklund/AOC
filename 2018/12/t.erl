-module(t).
-export([t/0]).

t() ->
    ITERS=20,
    {Q,_} = lists:mapfoldl(fun(_,X)->
				   A=matcher:match(X),{A,A} end, "#..#.#..##......###...###", lists:seq(1,ITERS)),
    P = lists:nth(ITERS,Q),
    {U,_}=lists:mapfoldl(fun(X,Acc)->
			if X==$# ->
				{Acc,Acc+1};
			   true ->
				{0,Acc+1} 
			end
		   end,
			 -ITERS*5, P),
    lists:foldl(fun(X,A)->X+A end,0,U).
				
    

