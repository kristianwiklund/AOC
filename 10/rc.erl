-module(rc).
-export([datan1/0]).
-export([datan2/0]).
-export([datan3/0]).
-export([datan4/0]).
-export([datan/0]).
-export([astrodetect/5]).
-export([online/6]).
-export([starcheck/3]).
-export([finder/4]).
-export([testzor/1]).
-export([polarize/3]).
-export([foff/3]).
-export([foffenator/4]).

datan() ->
    ["....#.....#.#...##..........#.......#......",
".....#...####..##...#......#.........#.....",
".#.#...#..........#.....#.##.......#...#..#",
".#..#...........#..#..#.#.......####.....#.",
"##..#.................#...#..........##.##.",
"#..##.#...#.....##.#..#...#..#..#....#....#",
"##...#.............#.#..........#...#.....#",
"#.#..##.#.#..#.#...#.....#.#.............#.",
"...#..##....#........#.....................",
"##....###..#.#.......#...#..........#..#..#",
"....#.#....##...###......#......#...#......",
".........#.#.....#..#........#..#..##..#...",
"....##...#..##...#.....##.#..#....#........",
"............#....######......##......#...#.",
"#...........##...#.#......#....#....#......",
"......#.....#.#....#...##.###.....#...#.#..",
"..#.....##..........#..........#...........",
"..#.#..#......#......#.....#...##.......##.",
".#..#....##......#.............#...........",
"..##.#.....#.........#....###.........#..#.",
"...#....#...#.#.......#...#.#.....#........",
"...####........#...#....#....#........##..#",
".#...........#.................#...#...#..#",
"#................#......#..#...........#..#",
"..#.#.......#...........#.#......#.........",
"....#............#.............#.####.#.#..",
".....##....#..#...........###........#...#.",
".#.....#...#.#...#..#..........#..#.#......",
".#.##...#........#..#...##...#...#...#.#.#.",
"#.......#...#...###..#....#..#...#.........",
".....#...##...#.###.#...##..........##.###.",
"..#.....#.##..#.....#..#.....#....#....#..#",
".....#.....#..............####.#.........#.",
"..#..#.#..#.....#..........#..#....#....#..",
"#.....#.#......##.....#...#...#.......#.#..",
"..##.##...........#..........#.............",
"...#..##....#...##..##......#........#....#",
".....#..........##.#.##..#....##..#........",
".#...#...#......#..#.##.....#...#.....##...",
"...##.#....#...........####.#....#.#....#..",
"...#....#.#..#.........#.......#..#...##...",
"...##..............#......#................",
"........................#....##..#........#"].


datan1() ->
    [".#..#",
     ".....",
     "#####",
     "....#",
     "...##"].

datan2() ->
    ["......#.#.",
     "#..#.#....",
     "..#######.",
     ".#.#.###..",
     ".#..#.....",
     "..#....#.#",
     "#..#....#.",
     ".##.#..###",
     "##...#..#.",
     ".#....####"].

datan3() ->
    [".#..##.###...#######",
     "##.############..##.",
     ".#.######.########.#",
     ".###.#######.####.#.",
     "#####.##.#.##.###.##",
     "..#####..#.#########",
     "####################",
     "#.####....###.#.#.##",
     "##.#################",
     "#####.##.###..####..",
     "..######..##.#######",
     "####.##.####...##..#",
     ".#####..#.######.###",
     "##...#.##########...",
     "#.##########.#######",
     ".####.#.###.###.#.##",
     "....##.##.###..#####",
     ".#.#.###########.###",
     "#.#.#.#####.####.###",
     "###.##.####.##.#..##"].
	
datan4() ->
[".#....#####...#..",
"##...##.#####..##",
"##...#...#.#####.",
"..#.....#...###..",
"..#.#.....#....##"].

setnth(1, [_|Rest], New) ->
    [New|Rest];
setnth(I, [E|Rest], New) -> 
    [E|setnth(I-1, Rest, New)].

setmatrix(Acc, X, Y,D) ->
    Row = lists:nth(Y, Acc),
    RowT = setnth(X, Row, D),
    AccT = setnth(Y, Acc, RowT),
    AccT.

mkblank(World) ->
    LX = length(lists:nth(1, World)),
    LY = length(World),
    Row = lists:duplicate(LX, 0),
    Acc = lists:duplicate(LY, Row),
    Acc.

getchar(World,X,Y)->
    Char = ((lists:nth(X,lists:nth(Y,World)))),
    Char.

%--------------------------------

% iterate over the matrix and figure out which combinations of
% asteroids cross what other things

% check if tx,ty is on the line from x1y1 to x2y2
%online(AX,AY,BX,BY,CX,CY) ->
%    if AX == CX ->
%	    BX == CX;
%       AY == CY ->
%	    BY == CY;
%       true ->
%	    ((AX-CX)*(AY-CY))==((CX-BX)*(CY-BY))
%end.
 
online(AX,AY,BX,BY,CX,CY) ->

    if 
	AX == BX ->
	    T2 = (CY-AY)/(BY-AY),
	    ((AX == CX) and ((T2>=0) and (T2=<1)));
	AY == BY ->
	    T1 =  (CX-AX)/(BX-AX),

	    ((AY == CY) and ((T1>=0) and (T1=<1)));
	true ->

	    T1 =  (CX-AX)/(BX-AX),
	    T2 = (CY-AY)/(BY-AY),
						%{T1,T2}.
	    ((T1==T2) and ((T1>=0) and (T1=<1)))
    end.
   
aditer1(World, [X|XS], Y, Acc,AX,AY,BX,BY) ->
    Char = getchar(World,X,Y),
    Coll = online(AX,AY,BX,BY,X,Y),
    
    AccP=setmatrix(Acc,X,Y,Coll and (Char==35)),
%    AccP=setmatrix(Acc, X, Y, X*Y), 
    aditer1(World, XS, Y, AccP,AX,AY,BX,BY);
aditer1(_,_,_,Acc,_,_,_,_) ->
    Acc.

aditer(World, [X|XS], [Y|YS], Acc,AX,AY,BX,BY) ->
    AccP = aditer1(World, [X|XS], Y, Acc,AX,AY,BX,BY),
    aditer(World, [X|XS], YS, AccP,AX,AY,BX,BY);
aditer(_,_,_,Acc,_,_,_,_)->
    Acc.

% this function lets us know if we can detect BXBY from AXAY
astrodetect(World,AX,AY,BX,BY) ->
    Acc = mkblank(World),
    CMatrix = aditer(World, 
	    lists:seq(1,length(lists:nth(1,Acc))),
	    lists:seq(1,length(Acc)), Acc,
		     AX,AY,BX,BY),
    T1 = lists:map(fun(Y)->lists:foldr(fun(X,Acc)->
					       if X -> Acc+1; true-> Acc end end,0,Y) end,CMatrix),
    T2 = lists:foldr(fun(X,Acc)->
			     X + Acc end,0,T1),
    T2<3.
    %CMatrix.
% --------------------------------------------
% interate over the matrix, check the ones with blob in them

sciter1(World, [X|XS], Y, Acc,AX,AY) ->
    
    Check = (not((X==AX) and (Y==AY))),
    %io:fwrite("~B,~B ~B,~B -> ~w\n",[X,Y,AX,AY,Check]),

    if (Check) ->
	    Char = getchar(World,X,Y),
	    if 
		Char == 35 ->
		    AD = astrodetect(World,AX,AY,X,Y);
		    %io:fwrite("~B,~B = ~w\n",[X,Y,AD]);

		true ->
		    AD = false
	    end,
	    if 
		AD -> 
		    AccP = Acc+1;
		true ->
		    AccP= Acc
	    end;
       true -> 
	    AccP=Acc
    end,
    
%    AccP=setmatrix(Acc, X, Y, X*Y), 
    sciter1(World, XS, Y, AccP,AX,AY);
sciter1(_,_,_,Acc,_,_) ->
    Acc.

sciter(World, [X|XS], [Y|YS], Acc,AX,AY) ->
    AccP = sciter1(World, [X|XS], Y, Acc,AX,AY),
    sciter(World, [X|XS], YS, AccP,AX,AY);
sciter(_,_,_,Acc,_,_)->
    Acc.

% given a specific blob, how many can we see?

starcheck(World,AX,AY) ->
    sciter(World,
	   lists:seq(1,length(lists:nth(1,World))),
	   lists:seq(1,length(World)),
	  0,AX,AY).

% which to look at?

finder1(World, [X|XS], Y, Acc) ->
    Char = getchar(World,X,Y),
    if 
	Char == 35 ->
	    AccP=[{X,Y}|Acc];
	true->
	    AccP=Acc
       end,
    finder1(World, XS, Y, AccP);
finder1(_,_,_,Acc) ->
    Acc.

finder(World, [X|XS], [Y|YS], Acc) ->
    AccP = finder1(World, [X|XS], Y, Acc),
    finder(World, [X|XS], YS, AccP);
finder(_,_,_,Acc)->
    Acc.

testzor1(World, [{AX,AY}|Alist], Acc)->
    
    N = starcheck(World,AX,AY),
    testzor1(World,Alist,[{AX,AY,N}|Acc]);
testzor1(_,_,Acc) ->
    Acc.

    
testzor(World) ->
    Asteroids = finder(World, 
		       lists:seq(1,length(lists:nth(1,World))), 
		       lists:seq(1,length(World)),
		       []),
    D=testzor1(World,Asteroids,[]),
    {X,Y,N} = lists:nth(1,lists:reverse(lists:sort(fun({_,_,X},{_,_,Y})->
							   Y>X end, D))),
    {X-1,Y-1,N}.

% {30,34,344}
% datan4 -> 9,4

polarize1([{XT,YT}|LS],Acc,HomeX,HomeY) ->

    X = XT-HomeX,
    Y = YT-HomeY,
    if 
	((XT==HomeX) and (YT==HomeY)) ->
	    polarize1(LS,Acc,HomeX,HomeY);
	true ->
	    Atan = math:atan2(Y,X)+math:pi()/2,
	    PI2 = math:pi()*2,
	    if 
		Atan < 0 ->
		    Btan = math:pi()*2-Atan;
		Atan >= PI2 ->
		    Btan = Atan-math:pi()*2;
		true ->
		    Btan=Atan
	    end,
	    T = {{XT,YT},{math:sqrt(X*X+Y*Y),
			  Btan}},
	    
	    polarize1(LS,[T|Acc],HomeX,HomeY)
    end;
polarize1(_,Acc,_,_) ->
    Acc.

% rc:polarize(rc:datan2(),10,12).

polarize(World,HomeX,HomeY) ->    
    A1 = finder(World, 
		       lists:seq(1,length(lists:nth(1,World))), 
		       lists:seq(1,length(World)),
		       []),
    A3=polarize1(A1,[],HomeX,HomeY),
    A4 = lists:sort(fun({{X1,Y1},{R1,A1}},{{X2,Y2},{R2,A2}}) ->
			    R2<R1 end, A3),
    A5  =lists:sort(fun({{X1,Y1},{R1,A1}},{{X2,Y2},{R2,A2}}) ->
			    A2>A1 end, A4),

    A5.

foff([Ast|AstS], Acc, OA, Remains, World,Cnt) ->
    {XY,{D,A}} = Ast,
    if 
	A=<OA ->
	    foff(AstS,Acc,OA, [Ast|Remains],World, Cnt);
	true ->
	    {X,Y}=XY,
	    NW = setmatrix(World,X,Y, Cnt),
	    foff(AstS,[{XY,Cnt}|Acc],A, Remains, NW, Cnt+1)
    end;
foff(_, Acc, _, Remains, World,Cnt) ->
    {lists:reverse(Acc),     lists:reverse(Remains), Cnt+1, World}.

foff([Ast|AstS],Cnt,World) ->
    {XY,{D,A}} = Ast,
    Acc = [{XY,Cnt}],
    OA = A,
    foff(AstS, Acc, OA, [],  World,Cnt).


foffenator(A,Acc,Cnt, World) ->
    if 
	A =/= [] ->
	    io:fwrite("Foff! ~B\n", [Cnt]),
	    {Result,Remains,C,NW} = foff(A,Cnt,World),


%	    Rem = lists:sort(fun({{X1,Y1},{R1,A1}},{{X2,Y2}
	    %,{R2,A2}}) ->
%				     A2>A1 end, Remains),
	    foffenator(Remains, lists:append(Acc,Result),C,NW);
	true ->
	    {Acc, World}
    end.

