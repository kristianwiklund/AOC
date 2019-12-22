-module(t).
-export([dealinto/1, cut/2, dealwithincrement/2]).

dealinto(Deck) ->
	lists:reverse(Deck).

cut(Deck, N) when N>0 ->
    {Pre,Post} = lists:split(N,Deck),
    Post++Pre;
cut(Deck, N) when N<0 ->
    {Pre, Post} = lists:split(length(Deck)+N,Deck),
    Post++Pre;
cut(Deck, N) when N==0 ->
    Deck.

dealwithincrement([Card|Deck], Acc, Pos, Max, N) ->
    AccP = maps:put(Pos, Card, Acc),
    PosP = Pos + N,
    if PosP > Max ->
	    PosY = PosP - Max;
       true  ->
	    PosY = PosP
    end,
    dealwithincrement(Deck, AccP, PosY, Max, N);
dealwithincrement([],Acc,_,_,_) ->
    Acc.
    
dealwithincrement(Deck, N) ->
    I1= dealwithincrement(Deck, #{}, 0, length(Deck), N),
    I2 = maps:to_list(I1),
    I3 = lists:keysort(1,I2),
    lists:map(fun({_,Y})->Y end, I3).
		      
