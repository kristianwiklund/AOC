
-module(fyra).
-export([checker2/1]).
-export([four1/0]).
-export([splitter/4]).
-export([four2/0]).

checker([A,B,C,D,E,F]) ->
    T = (A =< B) and (B =< C) and (C =< D) and (D =< E) and (E =< F), 
    U = (A == B) or (B == C) or (C == D) or (D == E) or (E==F),
    T and U;
checker(_) ->
    false.

four1() ->
    L = lists:seq(248345,746315),
    length(lists:filter(fun(D)->
			  checker(integer_to_list(D)) end, L)).

splitter([S|SS],OS,Cnt,L) ->
    if
	S==OS ->
	    splitter(SS, OS, Cnt+1, L);
	true ->
	    splitter(SS,S,1,[Cnt|L])
    end;
splitter(_,OS,Cnt,L) ->
    lists:reverse([Cnt|L]).



checker2(S) ->
    [A,B,C,D,E,F] = S,
    T = (A =< B) and (B =< C) and (C =< D) and (D =< E) and (E =< F), %% increasing or the same
    P = splitter(S,'',0,[]),
    T and lists:member(2,P).

four2() ->
    L = lists:seq(248345,746315),
    length(lists:filter(fun(D)->
			  checker2(integer_to_list(D)) end, L)).


