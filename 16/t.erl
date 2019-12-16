-module(t).
-export([t/0,pattern/2,applypattern/1,pmatrix/1]).

t() ->
    ok.

pattern(1) ->
    [0,1,0,-1].

pattern(N, Length) ->
    BasePattern = lists:flatten(lists:map(fun(X)->
						  lists:duplicate(N, X) end, pattern(1))),
    Instances = (Length div length(BasePattern))+1,
    RepeatedPattern = lists:flatten(lists:duplicate(Instances, BasePattern)),
    lists:reverse(lists:nthtail(length(RepeatedPattern)-Length-1, lists:droplast(lists:reverse(RepeatedPattern)))).

pmatrix(Txt)->					
    TP1 = lists:map(fun(X)->pattern(X, length(Txt)) end, lists:seq(1,length(Txt))),
    TP1.

applypattern(Signal) ->
    Txt = integer_to_list(Signal),
    NList = lists:map(fun(X)->X-48 end,Txt),
    NMatrix = lists:duplicate(length(Txt),NList),
    PMatrix = pmatrix(Txt),
    TM1 = lists:zipwith(fun(X,Y)->
				lists:zipwith(fun(W,V)->
						      (W*V) end, X,Y) end,
			NMatrix,PMatrix),
    TM2 = lists:map(fun(X)->
			    lists:foldl(fun(W,Acc)->
						W+Acc end,0, X) end, TM1),
    TM3 = lists:map(fun(W)->
			    (abs(W) rem 10) end, TM2),
    TM3.





%signal1() ->
%    "12345678".



