-module(t).
-export([move/5,chopout/4, findinsertcup/3, newcup/3,tt/0,t/0,t2/1]).

% original: 53350253
% putting pile first: 20429870 (see comment below)
% removing unnecessary calls to length: 18754332
% removing max/min:10493432

chopout(L, I, Len, CSize) ->
%    io:fwrite("~p: ~p ~n",[I, CSize]),
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

findinsertcup(Cup, Pile, Circle) when Cup<0 ->
    findinsertcup(lists:max(Circle), Pile, Circle);


findinsertcup(Cup, Pile, Circle) ->

    X = string:str(Circle, [Cup]),
    if
	X==0 ->
	    findinsertcup(Cup-1, Pile, Circle);
	true ->
	    Cup
    end.

insert(Circle, Pile, Where) ->
    I = string:str(Circle, [Where]),
    {L1,L2} = lists:split(I, Circle),
    
    Pile++(L2++L1). % putting the pile in the front and not in the back is a 50% speedup

newcup(Circle, Cup, LC) ->
    X = string:str(Circle, [Cup]),
    I=if
	X==LC ->
	    1;
	true -> X+1
      end,
    lists:nth(I, Circle).

%% change to not cut paste insert, do cut insert in the same move(?)

    
move (Circle, Cup, 0, _, _) ->
    I = string:str(Circle,[1]),
    {L1,L2} = lists:split(I, Circle),
    L = L2++L1,
    {Cup, L};
move (L, Cup, MaxMoves, Len, CSize) ->
    I = string:str(L, [Cup]),
% these three can 
    {Circle, Pile} = chopout(L, I, Len, CSize),
    InsertCup = findinsertcup(Cup-1, Pile, Circle),
    T2 = insert(Circle, Pile, InsertCup),
% be combined for speedup
    NewCup = newcup(T2, Cup, Len),
    move(T2, NewCup, MaxMoves-1, Len, CSize).


t() ->
    move(i:d(),1,100,length(i:d()),length(i:d())).

tt() ->
    move(i:s(),3,100, length(i:s()),length(i:s())).

t2(MAX) ->
    Len=1000,
    CSize=1000,
    L = i:s(),
    M = lists:max(i:s())+1,
    P = lists:seq(M,Len),
    {Time,R} = timer:tc(t,move, [L++P, 1, MAX, Len, CSize]),
    {Time,R}.

    
