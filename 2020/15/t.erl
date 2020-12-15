-module(t).
-export([say/2,say/3,ta1/0,ta2/0]).
-export([sayh/3,say2/3]).

%
% quite inefficient solution using lists
%
say(N, L) ->
    {P,_} =  lists:mapfoldl(fun(X,Turn) -> 
				    {if X == N -> Turn; true -> 0 end, Turn+1}
			    end,
			    1,
			    L++[N]),
    U = lists:filter(
      fun (X)->
	      X /= 0 
      end,
	  lists:reverse(P)),

    Turn=length(L),
      {if 
	  U==[Turn+1] -> 0;
	  true -> [A,B|_]=U,
		  A-B
		  
      end,
       L++[N]}.


say(N,L,2020)->
    N;
say(N,L,T) ->
    {V,NL}=say(N,L),
    say(V,NL,T+1).
    

ta1() ->
    say(0,input:input(),7).


%
% less inefficient solution using maps
%
sayh(N, L, T) ->
    
    OB = maps:get(N, L,nonesuch),
    OL = if 
	OB == nonesuch ->
	    lists:sublist([T,maps:get(0, L, [])],2);
	true ->
	    OB
    end,
    [B|_] = OL,
    {V,NewTurns} = {T-B,[T,B]},    
    NM = maps:put(N,NewTurns,L),
    {V,NM}.

say2(N,L,3000000)->
    N;
say2(N,L,T) ->
    {V,NL}=sayh(N,L,T),
    say2(V,NL,T+1).

ta2() ->
    say2(0, input:mkim(input:input()),7).
