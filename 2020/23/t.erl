-module(t).
-export([move/3,chopout/2, findinsertcup/4, newcup/2,tt/0,t/0]).

chopout(L, I) ->
    {L1,L2} = lists:split(I, L),
    L2Len = length(L2),
    {L1P,L2P} = if
	     L2Len < 3 ->
			{LT1,LT2} = lists:split(3-L2Len,L1),
			{LT2,L2++LT1};
		    true -> {LT1, LT2} = lists:split(3,L2),
			    {L1++LT2,LT1}
		end,
    {L1P,L2P}.


findinsertcup(Cup, Min, Max, Circle) when Cup<Min ->
    findinsertcup(Max, Min, Max, Circle);
findinsertcup(Cup, Min, Max, Circle) ->

    X = string:str(Circle, [Cup]),
    
    if
	X==0 ->
	    findinsertcup(Cup-1, Min, Max, Circle);
	true ->
	    Cup
    end.



insert(Circle, Pile, Where) ->
    I = string:str(Circle, [Where]),
    {L1,L2} = lists:split(I, Circle),
    L1++Pile++L2.

newcup(Circle, Cup) ->
    X = string:str(Circle, [Cup]),
    LC = length(Circle),

    I=if
	X==LC ->
	    1;
	true -> X+1
      end,
    lists:nth(I, Circle).

    
move (Circle, Cup, 0) ->
    I = string:str(Circle,[1]),
    {L1,L2} = lists:split(I, Circle),
    L = L2++L1,
    {L, Cup};
move (L, Cup, MaxMoves) ->
    io:fwrite("~p: ~p ~p ~n",[MaxMoves, Cup, L]),
    I = string:str(L, [Cup]),
    {Circle, Pile} = chopout(L, I),
    InsertCup = findinsertcup(Cup-1, lists:min(Circle), lists:max(Circle), Circle),
    T2 = insert(Circle, Pile, InsertCup),
    NewCup = newcup(T2, Cup),
%    T2.
    move(T2, NewCup, MaxMoves-1).


t() ->
    move(i:d(),1,100).

tt() ->
    move(i:s(),3,100).
