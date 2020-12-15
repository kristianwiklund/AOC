-module(input).
-export([short1/0]).
-export([short2/0]).
-export([short3/0]).
-export([short4/0]).
-export([short5/0]).
-export([short6/0]).
-export([short7/0]).
-export([input/0]).
-export([mkim/1]).

mkim(L) ->
    A = lists:map(fun(X)->
			  [X]
		  end,
		  lists:seq(1,length(L))),
    B = maps:from_list(lists:zip(L,A)),
    B.


input() ->
    [15,12,0,14,3,1].
short1() ->
    [0,3,6].

short2() ->
    [1,3,2].

short3() ->
    [2,1,3].

short4() ->
    [1,2,3].

short5() ->
    [2,3,1].


short6() ->
    [3,2,1].

short7() ->
    [3,1,2].
