-module(t).
-export([t/0,tt/1, foo/0,t2/0]).

t(ITERS) ->
    {Q,_} = lists:mapfoldl(fun(_,X)->
				   A=matcher:match(X),{A,A} end, "##.##.#.#...#......#..#.###..##...##.#####..#..###.########.##.....#...#...##....##.#...#.###...#.##", lists:seq(1,ITERS)),
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
	

t()->    
    t(20).
    
tt(ITERS) ->
    {Q,_} = lists:mapfoldl(fun(_,X)->
				   A=matcher:match(X),{A,A} end, "##.##.#.#...#......#..#.###..##...##.#####..#..###.########.##.....#...#...##....##.#...#.###...#.##", lists:seq(1,ITERS)),
    P = lists:nth(ITERS,Q).

foo(N, Acc) ->	
    X = string:trim(tt(N),both,"."),
    Test = maps:is_key(X, Acc),
    if 
	Test ->
	    io:fwrite("Match at ~B, previous was ~B\n", [N,maps:get(X,Acc)]);
       true ->
	    foo(N+1,maps:put(X, N, Acc))
    end.

foo() ->
    A = lists:seq(185,200),
    B = lists:map(fun(X)->t(X) end, A).

t2()->
    (50000000000-200)*96+t(200).

