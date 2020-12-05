-module(ett).
-export([a/0,a1/1]).
-export([b/0,b1/2]).

a1(Input) ->
    lists:flatten(lists:map(fun(X)->
				    lists:map(
				      fun(Y) ->
					      {X+Y,X,Y} 
				      end,
				      Input)
					 end,
					 Input)).
    
a(Input) ->
    {_,{_,A,B},_} =
	lists:keytake(2020,1,a1(Input)),
    A*B.

b1(Input,D) ->
    lists:filter(fun({V,_,_})->
			 V < 2020-D
		 end,
		 a1(Input)).

b(Input) ->
    D = lists:min(Input),
    If = lists:filter(fun(V)->
			      V < 2020-2*D
		      end,
		      Input),
    {_,{_,A,B,C},_} =                                                                                                
    lists:keytake(2020,1,
		  lists:flatten(lists:map(fun(Z) ->
						  lists:map(
						    fun({S,X,Y})->
							    {S+Z,X,Y,Z}
						    end,
						    b1(If,D))
					  end,
					  If))),
    A*B*C.


a() ->
    a(input:long()).

b()->		      
    b(input:long()).
