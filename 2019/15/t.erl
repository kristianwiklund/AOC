-module(t).
-export([move/5,t/0,tt/0,fsu/2,fsm/1]).
-export([emptyspaces/3]).
-export([nremptyspaces/3]).
-export([findstart/2]).
-include_lib("../../cecho/_build/default/lib/cecho/include/cecho.hrl").



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

move(Dir, CurrentX, CurrentY, World, Droid) ->
    

    DD = case Dir of 
	     78 -> 1; %N
	     69 -> 4; %E
	     87 -> 3; %W
	     83 -> 2 %S
	 end,

    Droid ! DD,
    
    receive
	Result ->
	    %io:fwrite("~p\n"", [Result]),
	    Result

    end,

    {DX,DY} = dirvector(Dir),

    case Result of 
	0 -> % hit wall
	    NewWorld = setcol(World, CurrentX+DX,CurrentY+DY, 1),
	    {Result, {CurrentX, CurrentY},NewWorld};
	1 ->  % moved one step
	    NewWorld = setcol(World, CurrentX+DX,CurrentY+DY, 0),
	    {Result, {CurrentX+DX, CurrentY+DY}, NewWorld};
	2 -> % found the oxygen system
	    NewWorld = setcol(World, CurrentX+DX,CurrentY+DY, 2),
	    {Result, {CurrentX+DX, CurrentY+DY},NewWorld}
    end.

fixnewdir(DirNR, Prob, X, Y, World) ->
    R = rand:uniform(100),
    Empty = emptyspaces(X,Y,World),
    NrEmpty = nremptyspaces(X,Y,World),
    Reverse = lists:nth(DirNR,[3,4,1,2]),
    TL = ic:setnth(Reverse, Empty, false),
    {TL2,_} = lists:mapfoldl(fun(X, Acc) -> {if X->Acc; true->0 end,Acc+1} end,1,TL),
    TL3 = lists:filter(fun(X)->
			       X=/=0 end, TL2),
    cecho:mvaddstr(2, 0, io_lib:format("Exits    : ~p       ",[TL3])),	    
    LTL3 = length(TL3),
    if LTL3 == 0 ->
	    Reverse;
       true->
	    lists:nth(rand:uniform(length(TL3)),TL3)
    end.
    
	    

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
	       	    


	
probinator(DirNR, X,Y, World, Droid) ->	   
    AP = "NESW",
    Reverse = [3,4,1,2],
    cecho:mvaddch(0,1,48+DirNR),
    {Res,{NX,NY},TNW} = move(lists:nth(DirNR,AP),X,Y,World, Droid),
    if 
	Res =/= 0 ->
	    {_,{NNX, NNY},NW} = move(lists:nth(
				       lists:nth(DirNR, Reverse),
				       AP),NX,NY,World, Droid),
	    if 
		{NNX, NNY} =/= {X,Y} ->
		    exit(failerror);
		true ->
		    ok
	    end;
	true -> NW = TNW
    end,
    NW.
	       

    
runaround(DirNR, X,Y, World, Droid) ->
    AP = "NESW",
    Bot = "^>v<",
    Here = getcol(World, X,Y),
    if Here == 0 ->
	    if {30,30}=={X,Y} ->
		    cecho:mvaddstr(Y,X,"@"); % erase cursor
	       true ->
		    cecho:mvaddstr(Y,X," ") % erase cursor
	    end;
       Here == 2 ->
	    cecho:mvaddstr(Y,X,"*");
       true ->
	    ok
    end,
    		       
    {Res,{NX,NY},TNW} = move(lists:nth(DirNR,AP),X,Y,World, Droid),    

    % if the move was successful, try moving in the other directions, after which, we return
    % to the current position
    % this maps the map

    if
	Res == 1 ->
	    TryDirs = lists:delete(DirNR, [1,2,3,4]),
    	    NW = lists:foldl(fun(DNR,Acc) -> probinator(DNR, NX, NY, Acc, Droid) end, TNW, TryDirs);
	true ->
	    NW = TNW
    end,
    
    cecho:mvaddstr(1, 0, io_lib:format("Position: (~B,~B)       ",[NX,NY])),	    
    cecho:mvaddch(NY,NX,lists:nth(DirNR,Bot)),
    cecho:refresh(),

%    timer:sleep(300), % to see what happens

    if 
	Res==0 ->
	    NewDir = fixnewdir(DirNR,100, NX, NY, NW);
	true ->
	    Check = nremptyspaces(NX, NY, NW),
	    if Check > 2 ->
		    NewDir = fixnewdir(DirNR,50, NX, NY, NW);
	       true ->
		    NewDir = DirNR
	    end
    end,

    case Res of
	1 ->
	    runaround(NewDir, NX,NY, NW, Droid);
	2 -> 
	    cecho:mvaddstr(NY,NX,"*"),
	    cecho:mvaddstr(30,30,"@"),
	    runaround(NewDir, NX, NY, NW, Droid);
	0 ->
	    runaround(NewDir, NX, NY, NW, Droid)
    end.

% 182 - too low
% 226 - incorrect
% 234 
% 281 - too high

t() ->
    Droid = setup(),
    runaround(1, 30,30,#{},Droid).

file2lines(File) ->
   {ok, Bin} = file:read_file(File),
   string2lines(binary_to_list(Bin), []).


string2lines("\n" ++ Str, Acc) -> [lists:reverse([$\n|Acc]) | string2lines(Str,[])];
string2lines([H|T], Acc)       -> string2lines(T, [H|Acc]);
string2lines([], Acc)          -> [lists:reverse(Acc)].

setmatrix(Acc, X, Y,D) ->
    Row = lists:nth(Y, Acc),
    RowT = ic:setnth(X, Row, D),
    AccT = ic:setnth(Y, Acc, RowT),
    AccT.

findpath(Maze,X,Y, Steps) ->
    Data = lists:nth(X, lists:nth(Y, Maze)),
    timer:sleep(50),
    case Data of
	42 ->
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
			


tt()->
    Maze = file2lines("map5"),
    {MX,MY} = findstart(Maze, 64),
    code:add_patha("../../cecho/_build/default/lib/cecho/ebin"),
    application:start(cecho),
    % Set attributes
    cecho:cbreak(),
    cecho:noecho(),
    cecho:curs_set(?ceCURS_INVISIBLE),
    cecho:refresh(),
    cecho:erase(),
    cecho:refresh(),
    lists:foldl(fun(S,Y)->cecho:mvaddstr(Y, 1, S),Y+1 end, 1,Maze),
    cecho:refresh(),
    findpath(Maze, MX, MY, 0).
    
	     
    


		     
