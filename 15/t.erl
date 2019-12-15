-module(t).
-export([move/5,t/0]).
-export([emptyspaces/3]).
-export([nremptyspaces/3]).
-include_lib("../../cecho/_build/default/lib/cecho/include/cecho.hrl").



getcol(Hull, X, Y) ->
    Key = [X,Y],
    Iskey = maps:is_key(Key, Hull),
    if 
	Iskey ->
	    maps:get(Key, Hull);
	true->
	    0
    end.
				
setcol(Hull, X, Y, Col) ->
    Key = [X,Y],
    %io:fwrite("Map: ~p\n", [Hull]),
    T = getcol(Hull, X,Y),
    if T =/= Col ->
	    Tile = lists:nth(Col,"#*"),
	    cecho:mvaddch(Y,X,Tile),
	    cecho:refresh(),
	    maps:put(Key, Col, Hull);
       true -> Hull
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
	    {Result, {CurrentX+DX, CurrentY+DY}, World};
	2 -> % found the oxygen system
	    NewWorld = setcol(World, CurrentX+DX,CurrentY+DY, 2),
	    {Result, {CurrentX+DX, CurrentY+DY},NewWorld}
    end.

fixnewdir(DirNR, Prob, X, Y, World) ->
    R = rand:uniform(100),
    Empty = emptyspaces(X,Y,World),
    NrEmpty = nremptyspaces(X,Y,World),
    if 
	NrEmpty == 1 -> % dead end, reverse
	    lists:nth(DirNR,[3,4,1,2]);
	true ->
	    if NrEmpty > 2 -> % more than two exits, eliminate the one we come from
		    TL = ic:setnth(lists:nth(DirNR,[3,4,1,2]), Empty, false),
		    {TL2,_} = lists:mapfoldl(fun(X, Acc) -> {if X->Acc; true->0 end,Acc+1} end,1,TL),
		    TL3 = lists:filter(fun(X)->
					       X=/=0 end, TL2),
		    lists:nth(rand:uniform(length(TL3)),TL3);
	       true ->
		    if R < Prob+1 ->
			    rand:uniform(4);
		       true ->
			    DirNR
		    end
	    end
    end.
	    

dirvector(Dir) ->
    case Dir of % {X,Y}
	78 -> {0,-1}; %N
	69 -> {1,0}; %E
	87 -> {-1,0}; %W
	83 -> {0,1} %S
    end.

emptyspaces(X,Y, World) ->
    L = lists:map(fun(P)->
			  dirvector(P) end, "NESW"),
    D = lists:map(fun({DX, DY}) ->
			  {DX+X,DY+Y} end, L),
    T = lists:map(fun({DX, DY}) ->
			  getcol(World, X,Y)==0 end, D).

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
% 281 - too high

t() ->
    Droid = setup(),
    runaround(1, 30,30,#{},Droid).
	


		     
