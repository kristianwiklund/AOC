-module(maze).
-export([fsu/2,fsm/1]).
-export([emptyspaces/3]).
-export([nremptyspaces/3]).
-export([findpath/4]).
-export([findstart/2,file2lines/1]).
-include_lib("../../cecho/_build/default/lib/cecho/include/cecho.hrl").

setnth(1, [_|Rest], New) ->
    [New|Rest];
setnth(I, [E|Rest], New) -> 
    [E|setnth(I-1, Rest, New)].



getcol(Hull, X, Y) ->
    Key = [X,Y],
    Iskey = maps:is_key(Key, Hull),
    if 
	Iskey ->
%	    cecho:mvaddstr(3,0,"Found real key"),
	    maps:get(Key, Hull);
	true->
	    
	    0
    end.
				
setcol(Hull, X, Y, Col) ->
    Key = [X,Y],
    NHull=maps:put(Key, Col, Hull),
    
    %io:fwrite("Map: ~p\n", [Hull]),
    if Col>-1 ->
	    Tile = lists:nth(Col+1," #*...."),
	    cecho:mvaddch(Y,X,Tile),
	    cecho:refresh(),
						%    io:fwrite("***~p***\n", [NHull]),
	    NHull;
       true ->
	    NHull
    end.


setup() ->
    code:add_patha("../../cecho/_build/default/lib/cecho/ebin"),
    application:start(cecho),
    % Set attributes
    cecho:cbreak(),
    cecho:noecho(),
    cecho:curs_set(?ceCURS_INVISIBLE),
    cecho:refresh(),
    cecho:erase(),
    cecho:refresh(),
    C = spawn(ic, run, [datan:datan(), self()]),
    C.

dirvector(Dir) ->
    case Dir of % {X,Y}
	78 -> {0,-1}; %N
	69 -> {1,0}; %E
	87 -> {-1,0}; %W
	83 -> {0,1}; %S
	1 -> {0,-1}; %N
	2 -> {1,0}; %E
	4 -> {-1,0}; %W
	3 -> {0,1} %S
    end.

emptyspaces(X,Y, World) ->
    L = lists:map(fun(P)->
			  dirvector(P) end, "NESW"),
    D = lists:map(fun({DX, DY}) ->
			  {DX+X,DY+Y} end, L),

    T = lists:map(fun({DX, DY}) ->
			  getcol(World, DX,DY) end, D),
    lists:map(fun(TT)->
		      TT==0 end, T).
    
    

nremptyspaces(X,Y,World) ->
    T = emptyspaces(X,Y,World),
    lists:foldl(fun(P, Acc) ->
			if P -> Acc+1; true->Acc end end, 0, T).
	       	    

file2lines(File) ->
   {ok, Bin} = file:read_file(File),
   string2lines(binary_to_list(Bin), []).


string2lines("\n" ++ Str, Acc) -> [lists:reverse([$\n|Acc]) | string2lines(Str,[])];
string2lines([H|T], Acc)       -> string2lines(T, [H|Acc]);
string2lines([], Acc)          -> [lists:reverse(Acc)].

setmatrix(Acc, X, Y,D) ->
    Row = lists:nth(Y, Acc),
    RowT = setnth(X, Row, D),
    AccT = setnth(Y, Acc, RowT),
    AccT.

findpath(Maze,X,Y, Steps) ->
    Data = lists:nth(X, lists:nth(Y, Maze)),
%    timer:sleep(50),
    case Data of
	65 -> % a, for testing
	    cecho:mvaddstr(0, 0, io_lib:format("Found at ~B steps",[Steps])),	    
	    Maze;
	35 -> % # 
	    Maze;	
	43 -> % +
	    Maze;
	_ ->
	    NewMaze = setmatrix(Maze, X,Y,43),
	    cecho:mvaddstr(Y,X,"+"),
	    cecho:refresh(),
	    TA=findpath(NewMaze, X,Y-1, Steps+1),
	    if  TA ->
		    NewMaze;
	       true ->
		    TB = findpath(NewMaze, X-1,Y, Steps+1),
		    if TB  ->
			    NewMaze;
		       true ->
			    TC = findpath(NewMaze, X,Y+1, Steps+1),
		    	    if TC ->
				    NewMaze;
			       true ->
				    TD = findpath(NewMaze, X+1,Y, Steps+1),
				    if TD ->
					    NewMaze;
				       true ->
					    cecho:mvaddstr(Y,X,"."),
					    cecho:refresh(),
					    Maze
				    end
			    end
		    end
	    end

    end.    
    
		       

fsm(X) ->    
    lists:foldl(fun(S, Acc) ->
			Acc+S end, 0, X).
fsu(X, What) ->
    {Res,_}= lists:mapfoldl(fun(S,Acc)->
				    {if S==What->Acc;true->0 end,Acc+1} end, 1,X),
    Res.

findstart(M,What) ->
    F = lists:map(fun(A) ->
			  fsu(A, What) end, M),
    FF = lists:map(fun(T) ->
			   fsm(T) end,F),
    X = lists:max(FF),
    {TT,_} = lists:mapfoldl(fun(S,Acc)->{if S=/=0->Acc;true->0 end,Acc+1} end, 1,FF),
    Y = lists:max(TT),
    {X,Y}.
			


    
	     
    


		     
