-module(t).
-import(kw,[getxy/3,setxy/4,setnth/3,mkblank/1,file2lines/1,tilecount/4]).

-export([t/0,evolve/3, mutate/1,datan/0, datan2/0,datan3/0,bdr/1,runmut/2]).


datan() ->
    [".###.",
     "..#.#",
     "...##",
     "#.###",
     "..#.."].

datan2() ->
    ["....#",
     "#..#.",
     "#..##",
     "..#..",
     "#...."].

datan3() ->
    [".....",
     ".....",
     ".....",
     "#....",
     ".#..."].

evolve(World, X,Y) ->
    
    NB = tilecount(X,Y,World,"#"),
    ME = [getxy(World, X,Y)] ==  "#",


    if
	(ME and (NB == 1)) ->
						%	    io:fwrite("Stay: (~B,~B) NB:~B ME:~p\n",[X,Y,NB,ME]),
	    35;
	((not ME) and ((NB == 1) or (NB == 2))) ->
						%	    io:fwrite("Grow: (~B,~B) NB:~B ME:~p\n",[X,Y,NB,ME]),
	    35;
	true ->
						%	        io:fwrite(" Die: (~B,~B) NB:~B ME:~p\n",[X,Y,NB,ME]),
	    46
    end.

bdr(World) ->
    L = lists:flatten(World),
    {T,_} = lists:mapfoldl(fun(A,Acc)->
			       {if [A]=="#" -> math:pow(2,Acc); true->0 end,Acc+1} end,0,L),
    S= trunc(lists:foldl(fun(X, Sum) -> X + Sum end, 0, T)),
    S.

mutate(World) ->
    
    NW = lists:map(
	   fun(Y) ->
		   lists:map(
		     fun(X) ->
			     evolve(World,X,Y) end,
		     lists:seq(1,5)) end,
	   lists:seq(1,5)),
    NW.

printworld([W|WS]) ->
    io:fwrite("~s\n",[W]),
    printworld(WS);
printworld(_) ->
    io:fwrite("--------").


runmut(World, Cache) ->

    NW = mutate(World),

    Check = maps:is_key( lists:flatten(NW), Cache),

    if Check ->
	    io:fwrite("--------\nBDR: ~p\n", [bdr(NW)]),
	    printworld(NW);
       true ->
	    NC = maps:put(lists:flatten(World), 1, Cache),
	    runmut(NW,NC)
    end.
    

t()->
    runmut(t:datan(), #{}).

% 23014595 too low

