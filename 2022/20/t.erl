-module(t).
-export([t/0,move/2,calcmove/3,index_of/2]).

index_of(Item, List) -> index_of(Item, List, 1).

index_of(_, [], _)  -> not_found;
index_of(Item, [Item|_], Index) -> Index;
index_of(Item, [_|Tl], Index) -> index_of(Item, Tl, Index+1).


data() ->
    [1, 2, -3, 3, -2, 0, 4].


calcmove(XP,I,B) when B<0 ->
    V=(I+B) rem length(XP),
    if
	V<0 ->
	    V+length(XP);
	true ->
	    V
    end;
calcmove(XP,I,B) when B>0 ->
    (I+B) rem length(XP).

move(X,0) ->
    X;

move(X,B) ->
    I = index_of(B,X),
    {X1,[_|X2]}=lists:split(I-1,X),
    XP1=X1++X2,
    TO=calcmove(XP1,I-1,B),
    {Y1,Y2} = lists:split(TO,XP1),
    if 
	Y1==[] ->
	    Y2++[B];
	Y2==[] ->
	    [B]++Y1;
	true ->
	    Y1++[B]++Y2
    end.

run(X,0)->
    X;

run(X,[Y|YS]) ->
    V=move(X,Y),
    run(V,YS);

run(X,_) ->
    X.


t()->
    D = input:i(),
    R = run(D,D),
    I = index_of(0,R),
    A = lists:nth((I+1000) rem length(R),R),
    B =	lists:nth((I+2000) rem length(R),R),
    C =	lists:nth((I+3000) rem length(R),R),
    {A,B,C,A+B+C}.
			 
