-module(kw).
-export([getxy/3,setxy/4,setnth/3,mkblank/1,file2lines/1,tilecount/4,tilematch/4]).


dirvector(Dir) ->
    case Dir of % {X,Y}
	"N" -> {0,-1}; %N
	"E" -> {1,0}; %E
	"W" -> {-1,0}; %W
	"S" -> {0,1}; %S
	
	78 -> {0,-1}; %N
	69 -> {1,0}; %E
	87 -> {-1,0}; %W
	83 -> {0,1}; %S

	1 -> {0,-1}; %N
	2 -> {1,0}; %E
	4 -> {-1,0}; %W
	3 -> {0,1} %S
    end.

tilematch(X,Y, World, What) ->
    
    MaxY = length(World),
    MaxX = length(lists:nth(1,World)),

    L = lists:map(fun(P)->
			  dirvector(P) end, "NESW"),
    D1 = lists:map(fun({DX, DY}) ->
			  {DX+X,DY+Y} end, L),
    D = lists:filter(fun({DX,DY}) ->
			     (DX =< MaxX) and (DY =< MaxY) and (DX =/=0) and (DY =/= 0) end, D1),

    T = lists:map(fun({DX, DY}) ->
			  Check = getxy(World, DX,DY), [Check] == What end, D),
    T.
    

tilecount(X,Y,World, What) ->
    T = tilematch(X,Y,World, What),
    lists:foldl(fun(P, Acc) ->
			if P -> Acc+1; true->Acc end end, 0, T).


getxy(Hull, X, Y) when is_map(Hull)->
    Key = [X,Y],
    Iskey = maps:is_key(Key, Hull),

    if 
	Iskey ->
%	    cecho:mvaddstr(3,0,"Found real key"),
	    maps:get(Key, Hull);
	true->	    
	    0
    end;

getxy(World,X,Y) when is_list(World)->

    Char = ((lists:nth(X,lists:nth(Y,World)))),
    Char.				

setxy(Hull, X, Y, Col) when is_map(Hull) ->
    Key = [X,Y],
    NHull=maps:put(Key, Col, Hull),
    
    %io:fwrite("Map: ~p\n", [Hull]),
    if Col>-1 ->
	    %Tile = lists:nth(Col+1," #*...."),
	%    cecho:mvaddch(Y,X,Tile),
	 %   cecho:refresh(),
						%    io:fwrite("***~p***\n", [NHull]),
	    NHull;
       true ->
	    NHull
    end;
setxy(Acc, X, Y,D) when is_list(Acc) ->
    Row = lists:nth(Y, Acc),
    RowT = setnth(X, Row, D),
    AccT = setnth(Y, Acc, RowT),
    AccT.


setnth(1, [_|Rest], New) ->
    [New|Rest];
setnth(I, [E|Rest], New) -> 
    [E|setnth(I-1, Rest, New)].



mkblank(World) when is_list(World) ->
    LX = length(lists:nth(1, World)),
    LY = length(World),
    Row = lists:duplicate(LX, 0),
    Acc = lists:duplicate(LY, Row),
    Acc;
mkblank(World) when is_map(World) ->
    #{}.





file2lines(File) ->
   {ok, Bin} = file:read_file(File),
   string2lines(binary_to_list(Bin), []).


string2lines("\n" ++ Str, Acc) -> [lists:reverse([$\n|Acc]) | string2lines(Str,[])];
string2lines([H|T], Acc)       -> string2lines(T, [H|Acc]);
string2lines([], Acc)          -> [lists:reverse(Acc)].
