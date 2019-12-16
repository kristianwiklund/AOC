-module(t).
-export([t/1,pattern/2,applypattern/1,pmatrix/1,applypattern/2]).


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
    Txt = Signal,
    NMatrix = lists:duplicate(length(Txt),Txt),
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


applypattern(Signal, 0)->
    Signal;


applypattern(Signal, N) ->
    applypattern(applypattern(Signal), N-1).

t(Signal) ->
    NList = lists:map(fun(X)->X-48 end,Signal),
    TM3=applypattern(NList, 100),
    lists:map(fun(X)->X+48 end, TM3).



%signal1() ->
%    "12345678".



