-module(t).
-export([move/5,t/0]).


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
    maps:put(Key, Col, Hull).


setup() ->
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
	    Result
    end,

    {DX,DY} = case Dir of
		    78 -> {-1,0};
		    69 -> {0,1};
		    87 -> {1,0};
		    83 -> {0,-1}
		end,

    case Result of 
	0 -> % hit wall
	    NewWorld = setcol(World, CurrentX+DX,CurrentY+DY, 1),
	    {Result, {CurrentX, CurrentY},NewWorld};
	1 -> 
	    {Result, {CurrentX+DX, CurrentY+DY},World};
	2 ->
	    NewWorld = setcol(World, CurrentX+DX,CurrentY+DY, 2),
	    {Result, {CurrentX+DX, CurrentY+DY},NewWorld}
    end.
    
runaround(DirNR, X,Y, World, Droid) ->
    AP = "NWSE",
    
    {Res,{NX,NY},NW} = move(lists:nth(DirNR,AP),X,Y,World, Droid),
    
    io:fwrite("(~B,~B)\n",[NX, NY]),

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
	


		     
