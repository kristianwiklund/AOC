-module(t).
-export([incr/1]).
-export([check/1]).

m1(S) ->
    re:run(S,"(.)\\1.*(.)\\2") /= nomatch.

check ([A,B,C,D,E,F,G,H]) ->
    S = [A,B,C,D,E,F,G,H],
    T1 = (length(lists:filter(fun(X)->
				      lists:member(X,"iol")
			   end, S)) == 0),    
    T2 = T1 and (re:run(S, "cba|dcb|edc|fed|gfe|hgf|rqp|srq|trs|uts|vut|wvu|xwv|yxw|zyx") /= nomatch),
    T3 = T2 and m1(S),
    T3;
check (_) ->
    false.

i ($z) ->
    $a;
i ($h) ->
    $j;
i ($n) ->
    $p;
i ($k) ->
    $m;
i ([L|LS]) when L==$z->
    [i(L)|i(LS)];
i ([L|LS]) ->
    [i(L)|LS];
i (L) ->
    L + 1.

incr (S,false) ->
    N = i(S),
    io:fwrite("|~10s|~n", [lists:reverse(N)]),
    incr(N, check(N));
incr (S, true) ->
    S.
incr (S) ->
    lists:reverse(incr (lists:reverse(S), false)).
    

    
