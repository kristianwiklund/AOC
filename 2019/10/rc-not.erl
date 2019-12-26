-module(rc).
-export([raycast/3]).
-export([datan1/0]).
-export([t/0]).

datan1() ->
    [".#..#",
     ".....",
     "#####",
     "....#",
     "...##"].

setnth(1, [_|Rest], New) ->
    [New|Rest];
setnth(I, [E|Rest], New) -> 
    [E|setnth(I-1, Rest, New)].

addvisible(Acc, X, Y,D) ->
    Row = lists:nth(Y, Acc),
    RowT = setnth(X, Row, D),
    AccT = setnth(Y, Acc, RowT),
    AccT.

raycast(World, X, Y, DX, DY, Acc) ->


    if (false) ->
	    ok;
       true ->

	    LX = length(lists:nth(1, World)),
	    LY = length(World),
    if 
	((trunc(X)<1) or (trunc(Y)<1) or (trunc(X)>LX) or (trunc(Y)>LY)) -> 
	    Acc;
	true ->									       
	    Pixel = lists:nth(trunc(X), lists:nth(trunc(Y), World)),


	    if 
		Pixel == 35 -> 
		    AccP = addvisible(Acc, trunc(X),trunc(Y),1),
						%io:fwrite("~w\n", [AccP]),
		    AccP;
		true -> 
		    AccP = addvisible(Acc,trunc(X),trunc(Y),2),
		    raycast(World, X+DX, Y+DY, DX, DY, AccP)
	    end

	    
    end
    end.

runrc(World, X, Y, [D|DS], Acc) ->
    Rad = D*math:pi()/180,
    DX = math:cos(Rad),
    DY = math:sin(Rad),
    AccP=raycast(World, X,Y,DX,DY,Acc),
    runrc(World,X,Y,DS,AccP);
runrc(_,_,_,_,Acc) ->
    Acc.

mkblank(World) ->
    LX = length(lists:nth(1, World)),
    LY = length(World),
    Row = lists:duplicate(LX, 0),
    Acc = lists:duplicate(LY, Row),
    Acc.

raycast(World, X, Y) ->

    Acc = mkblank(World),

    RowA = lists:nth(Y, World),
    RowT = setnth(X, RowA, "."),
    WorldP = setnth(Y, World, RowT),

    VisibleW=runrc(WorldP, X, Y, lists:seq(0,360),Acc),
		   VWT = lists:map(fun(L1)->
			    lists:foldl(fun(L2,Sum)->L2+Sum end,0,L1) end, VisibleW),
    lists:foldl(fun(L1,Sum)->
			L1+Sum end,0,VWT)+1.



rcx(World, [X|XS],Y,Acc) ->
    Pixel = lists:nth(X, lists:nth(Y,World)),
    if 
	Pixel == 35 ->
	    AccP = addvisible(Acc, X, Y, raycast(World, X,Y));
	true -> 
	    AccP = Acc
    end,
    rcx(World, XS, Y, AccP);
rcx(_,_,_,Acc) ->
    Acc.

raycast(World, XL,[Y|YS],Acc) ->
    AccP=rcx(World, XL, Y, Acc),
    raycast(World, XL, YS, AccP);
raycast(_,_,_,Acc) ->
    Acc.


    
raycast(World) ->
    Acc = mkblank(World),
    raycast(World, 
	    lists:seq(1,length(lists:nth(1,Acc))),
	    lists:seq(1,length(Acc)), Acc).
	    
t() ->   
    Acc = mkblank(datan1()),
    T=    runrc(addvisible(datan1(),5,1,"."),5,1,lists:seq(0,720),Acc),
    addvisible(T,5,1,8).

