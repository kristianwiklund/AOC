-module(t).
-export([loop/2, bfl/2, revkey/3]).
-export([t/0]).

loop(V, _, 1) -> 
    V;
loop(V, Num, Iters) ->
    (V*loop(V, Num, Iters-1)) rem 20201227.
loop(Num, Iters) ->
    loop(Num, Num, Iters).


bfl(Num, Max) ->
    P=lists:seq(1,Max),
    {A,_}=lists:mapfoldl(fun(Z,Acc) -> {Acc,(Acc*7) rem 20201227} end ,7, P),
    maps:from_list(lists:zip(A,P)).

revkey(Num, Key, Max) ->
    A = bfl(Num, Max),
    I = maps:get(Key, A),
    I.

t() ->
    {Card, Door} = i:d(),
    RevCard = revkey(7, Card, 70000000),
    io:fwrite("Card ~p~n",[RevCard]),
    RevDoor = revkey(7, Door, 70000000),
    io:fwrite("Door ~p~n",[RevDoor]),
    ECard = loop(Card, RevDoor),
    io:fwrite("ECard ~p~n",[ECard]),
    EDoor = loop(Door, RevCard),
    io:fwrite("EDoor ~p~n",[EDoor]),
    {ECard, EDoor}.
