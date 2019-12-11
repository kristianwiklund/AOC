-module(one).
-export([one/1]).
-export([fuel/1]).
-export([readfile/1]).

fuel(N) when N=<0 -> 0;
fuel(N) ->
	T = N div 3 - 2,
	F = case T of
	    	 Neg when Neg<0 -> 0;
		 Pos when Pos>=0 ->  T
	end,
	F+fuel(F).

readfile(FileName) ->
		   {ok, Binary} = file:read_file(FileName),
		   string:tokens(erlang:binary_to_list(Binary), "\n").

one(FileName) ->
	      L = readfile(FileName),
	      lists:mapfoldl(fun(W,S) -> {S+fuel(W)} end, 0 , L).
	      