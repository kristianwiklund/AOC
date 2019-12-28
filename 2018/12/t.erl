-module(t).
-export([t/0]).

t() ->
    ITERS=20,
    {P,_} = lists:mapfoldl(fun(_,X)->
				   A=matcher:match(X),{A,A} end, "..#..", lists:seq(1,ITERS)),
    P.
    

