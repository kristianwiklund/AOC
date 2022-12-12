-module('nine').
-export([parse/1,t/0,x/0]).

garbage([$!,_|XS],C)->
    garbage(XS,C);
garbage([$>|XS],C) ->	
    {XS,C};
garbage([_|XS],C) ->       
    garbage(XS,C+1).

parse([$<|XS],N) ->
    {XSP,NP}=garbage(XS,N),
    parse(XSP,NP);
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

x() ->
    parse(i:i()).
% 8784 too high
% 14190 too high





