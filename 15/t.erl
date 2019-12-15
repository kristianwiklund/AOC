-module(t).
-export([move/5,t/0]).
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
    Tile = lists:nth(Col,"#*"),
    cecho:mvaddch(Y,X,Tile),
    cecho:refresh(),
    maps:put(Key, Col, Hull).



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
    
    cecho:mvaddch(CurrentY,CurrentX,32),

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

    {DX,DY} = case Dir of
		    78 -> C="^", {-1,0};
		    69 -> C="<", {0,1};
		    87 -> C=">", {1,0};
		    83 -> C="v", {0,-1}
		end,

    case Result of 
	0 -> % hit wall
	    NewWorld = setcol(World, CurrentX+DX,CurrentY+DY, 1),
	    cecho:mvaddstr(CurrentY,CurrentX,C),
	    cecho:refresh(),
	    {Result, {CurrentX, CurrentY},NewWorld};
	1 ->  % moved one step
	    cecho:mvaddstr(CurrentY+DX,CurrentX+DY,C),
	    cecho:refresh(),
	    {Result, {CurrentX+DX, CurrentY+DY}, World};
	2 -> % found the oxygen system
	    NewWorld = setcol(World, CurrentX+DX,CurrentY+DY, 2),
	    {Result, {CurrentX+DX, CurrentY+DY},NewWorld}
    end.
    
runaround(DirNR, X,Y, World, Droid) ->
    AP = "NWSE",
    
    {Res,{NX,NY},NW} = move(lists:nth(DirNR,AP),X,Y,World, Droid),
    
    %io:fwrite("(~B,~B) ~p\n",[NX, NY, NW]),

    case Res of
	1 ->
	    runaround(DirNR, NX,NY, NW, Droid);
	2 -> 
	    {Res,{NX,NY},NW};
	0 ->
	    NewDir = if DirNR == 4  ->
			     1;
			true -> DirNR + 1
		     end,
	    runaround(NewDir, NX, NY, NW, Droid)
    end.


t() ->
    Droid = setup(),
    runaround(1, 0,0,#{},Droid).
	


		     
