-module(t).
-export([draw/1,score/1,t/0]).

draw({[P1|P1S],[P2|P2S]}) when P1>P2 ->
    draw({P1S++[P1,P2],P2S});
draw({[P1|P1S],[P2|P2S]}) when P1<P2 ->
    draw({P1S, P2S++[P2,P1]});
draw({[P1|P1S],[P2|P2S]}) when P1==P2 ->
    draw({P1S++[P1], P2S++[P2]});
draw(X) ->
    X.

score(L)->
    Z = lists:zipwith(fun(X,Y) ->
			      X*Y
		      end,
		      lists:reverse(L),
		      lists:seq(1,length(L))),
    lists:sum(Z).

t()->
    {P1,P2} = draw(i:input()),
    max(score(P1),score(P2)).

% -----------------------
