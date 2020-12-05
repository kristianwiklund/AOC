-module(ett).
-export([a/0]).
-export([b/0]).

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

b1() ->
    lists:filter(fun({V,_,_})->
			 V < 2020
		 end,
		 lists:flatten(lists:map(fun(X)->
						 lists:map(
						   fun(Y) ->
							   {X+Y,X,Y} 
						   end,
						   input:short())
					 end,
					 input:short()))).

b() ->
    [{_,A,B,C}|_] =                                                                                                
    lists:filter(fun({V,_,_,_}) ->
			 V == 2020
		 end,
    lists:flatten(lists:map(fun(Z) ->
		      lists:map(
			fun({S,X,Y})->
				{S+Z,X,Y,Z}
			end,
			b1())
	      end,
			    input:long()))),
    A*B*C.
		      
