-module(t).
-export([draw/1,score/1,t/0,game/4]).

% part 1

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

% part 2 - recursive banananna

% round: play a round

round({[P1|P1S],[P2|P2S]}, GameID) ->
    
    L1 = length(P1S),
    L2 = length(P2S),
    if
	(L1>=P1S) and (L2>=P2S) ->
	    game({P1S,P2S}, #{}, GameID+1, 1);
	true -> 
	    if 
		P1>P2 ->
		    {p1win, {P1S++[P1,P2],P2S}};
		P2<P1 ->
		    {p1win, {P1S,P2S++[P2,P1]}}
	    end
    end.

% game: keeps a state of rounds
% check round before playing round to see if the round had been played before

game(Deck, Rounds, GameID, RoundID) ->
    CheckDeck = maps:is_key(Deck, Rounds),
    NewState =
	if CheckDeck ->
		{p1win, Deck};
	   true ->
		round(Deck, GameID)
	end,
    NewState.


	
