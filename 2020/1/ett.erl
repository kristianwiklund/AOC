-module(ett).
-export([a/0]).

a() ->
    [{_,A,B}|_] =
    lists:filter(fun({V,_,_})->
			 V == 2020
		 end,
		 lists:flatten(lists:map(fun(X)->
				   lists:map(
				     fun(Y) ->
					     {X+Y,X,Y} 
				     end,
				     input:long())
			   end,
					 input:long()))),
    A*B.
