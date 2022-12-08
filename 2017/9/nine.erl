-module('nine').
-export([parse/1,t/0]).

garbage([$!,_|XS])->
    garbage(XS);
garbage([$>|XS]) ->	
    XS;
garbage([_|XS]) ->       
    garbage(XS).

parse([$<|XS],N) ->
    garbage(XS),
    N;
parse([${|XS],N) ->
    parse(XS,N);
parse([$}|XS],N) ->
    parse(XS,N+1);
parse([_|XS],N) ->
    parse(XS,N);
parse(_,N) ->
    N.

parse(X) ->
    parse(X,0).

% ----  tests ----

t() ->
    [
     parse("<>"),
     parse("<<<<>"),
     parse("<{!>}>"),
     parse("{}"),
     parse("{{{}}}"),
     parse("{{{},{},{{}}}}"),
     parse("{{},{}}")
    ].





