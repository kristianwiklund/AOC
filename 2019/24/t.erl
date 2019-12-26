-module(t).
-import(kw,[getxy/3,setxy/4,setnth/3,mkblank/1,file2lines/1,tilecount/4]).

-export([t1/0,t/0,evolve/3, mutate/1,datan/0, datan2/0,datan3/0,bdr/1,runmut/2,colsum/2,rowsum/2]).
-export([countneighbors/5,revolve/5]).

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
% ---------------------------- solution for part 1 ------------------------------------------%

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
    

t1()->
    runmut(t:datan(), #{}).

% ---------------------------- solution for part 2 ------------------------------------------%
% changes needed:
% world need to become a map of worlds with number
% looking at tile ? will recurse into the next world
% looking at the edges will look one level upwards
% if those worlds do not exist, they need to be created

emptyworld() ->
    T=lists:map(fun(_)->"....." end, lists:seq(1,5)),
    setxy(T,3,3,"?").

% -- mutate all worlds in RWorld. If no bugs are created in a world, and it is above or below the current max, remove it

colsum(World, Col) ->
    
    L = lists:map(fun(Y)->
			  T = getxy(World, Col, Y),
			  if [T]=="#" ->
				  1;
			     true ->
				  0
			  end end, lists:seq(1,5)),
    lists:foldl(fun(T, Acc)->
			T+Acc end,0,L).

rowsum(World, Row) ->
    
    L = lists:map(fun(X)->
			  T = getxy(World, X, Row),
			  if [T]=="#" ->
				  1;
			     true ->
				  0
			  end end, lists:seq(1,5)),
    lists:foldl(fun(T, Acc)->
			T+Acc end,0,L).


checkneighbor(World, X, Y, RWorld, Level, Direction) ->			  
    {DX, DY} = kw:dirvector(Direction),
    NX = X+ DX,
    NY = Y + DY,
    if 
	{NX, NY} == {3,3} ->% go down one level
	    Check = maps:is_key(Level-1, RWorld),	    
	    if
		not Check ->
%		    io:fwrite("No world below ~B\n",[Level]),
		    0; % no level below -> no bacteria there
		true ->
		    G = maps:get(Level-1, RWorld),
		    
		    case Direction of 
			"N" -> 
			    rowsum(G,5);
			"E" ->
			    colsum(G,1);
			"W" ->
			    colsum(G,5);
			"S" ->
			    rowsum(G,1)
		    end
	    end;

	((NX > 0) and (NX < 6) and (NY>0) and (NY<6)) ->
	    T = getxy(World, NX, NY),
	    if T==$# ->
		    1;
	       true ->
		    0
	    end;
		
	true -> % one level up, we are outside this thingy
	    Check = maps:is_key(Level+1, RWorld),	    
	    if
		not Check ->
%		    io:fwrite("No world above ~B\n",[Level]),
		    0; % no level above -> no bacteria there
		true ->
		    G = maps:get(Level+1, RWorld),
		    
		    case Direction of 
			"N" -> 
			    T = getxy(G,3,2);
			"E" ->
			    T = getxy(G,4,3);
			"W" ->
			    T = getxy(G,2,3);
			"S" ->
			    T = getxy(G,3,4)
		    end,
		    if T==$# ->
			    1;
		       true ->
			    0
		    end
	    end
    end.


countneighbors(World, X, Y, RWorld, Level) ->
    
    % we need to check three different cases
    % "in world" -> the number of # that are on this level
    % "out of bounds" -> the number of # that are immediately outside
    % that is, to the left, right, up, down of the ? in the above level
    % "collapse" -> the number of # that are on the edge of the below thing

    % refering to the things we probe, not the current item:
    % in world: (X,Y) != 3,3 and X>0 and X<5 and Y>0 and Y<6
    % out of bounds: X<0 or X>5 or Y<0 or Y> 5
    % collapse: {X,Y} == {3,3}

    % need more food error
    
    % look to the north

    N = checkneighbor(World, X,Y,RWorld, Level,"N"),
    E = checkneighbor(World, X,Y,RWorld, Level,"E"),
    W = checkneighbor(World, X,Y,RWorld, Level,"W"),
    S = checkneighbor(World, X,Y,RWorld, Level,"S"),
    N+E+W+S.
	    
    
revolve(World, X, Y, RWorld, Level) ->
    
    % basically the same as the "evolve" above, but it need to descend through the ?:s and ascend through its sides
    
    Char = getxy(World, X,Y),
    if 
	Char == $? ->
	    Char;
	{X,Y} == {3,3} ->
	    $?;
	true ->
	    NB = countneighbors(World, X, Y, RWorld, Level),
	    ME = (Char == $#),
	    % the usual rule

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
	    end
    end.


rmutate(RWorld, NW, [Level|Levels]) ->
    
    Check = maps:is_key(Level, RWorld),
    World = 
	if Check ->
		maps:get(Level, RWorld);
	   true ->
		emptyworld()
	end,
    
    TNW = lists:map(
	    fun(Y) ->
		    lists:map(
		      fun(X) ->
			      revolve(World,X,Y, RWorld, Level ) end,
		      lists:seq(1,5)) end,
	    lists:seq(1,5)),
    
    if 
	TNW =/= World ->
	    FNW = maps:put(Level, TNW, NW);
	true ->
	    FNW = NW
    end,
    rmutate(RWorld, FNW, Levels);
rmutate(_,NW,_) ->
    NW.

    
    



rmutate(RWorld) ->
    
    % S are the worlds we already have
    S = lists:seq(maps:get("min", RWorld), maps:get("max", RWorld)),
    
    TNW = rmutate(RWorld, #{}, S),
    Keys = maps:keys(TNW),
    TNW1 = maps:put("min", lists:min(Keys)-1, TNW),
    TNW2 = maps:put("max", lists:max(Keys)+1, TNW1),
    TNW2.
   
    
    

% -- helpers below --

runrmut(RWorld, 0) ->
    RWorld;

runrmut(RWorld, Steps) ->  
    NRW1 = rmutate(RWorld),
    runrmut(NRW1, Steps - 1).

t() ->
    W = setxy(t:datan(), 3,3,"?"),
    RW = #{0=>W,"max"=>1, "min"=>-1},
    M=runrmut(RW,200),
    AW = lists:flatten(maps:values(M)),
    C= lists:foldl(fun(X,Acc)->
			if X==$# ->
				Acc+1;
			   true ->
				Acc
			end 
		   end, 0 , AW),
    C.
    
