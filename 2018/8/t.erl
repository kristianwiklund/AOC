-module(t).
-export([t/0]).

parsechildren(_, [], DATA, MetaAcc) ->
    {DATA, MetaAcc};
parsechildren(Indent, [ID|IDS], DATA, MetaAcc) ->
%    io:fwrite("~sparsing child ~B: DATA ~p\n",[lists:flatten(lists:duplicate(Indent, "-->")),ID,DATA]),
    {DATA_, MetaAcc_}=parsenode(Indent,DATA, MetaAcc),
    parsechildren(Indent, IDS, DATA_, MetaAcc_).



readmetadata(_, 0, DATA) ->
    {DATA, 0};
readmetadata(Indent, N, [D|DATA]) ->
%    io:fwrite("~sMeta: ~B\n", [lists:flatten(lists:duplicate(Indent, "-->")),D]),
    {DATA_,M} = readmetadata(Indent, N-1, DATA),
    {DATA_, M+D}.


parsenode(Indent,[NChild,NMeta|DATA], MetaAcc) ->
    
%    io:fwrite("~sNode with ~B children, ~B metadata, DATA: ~p\n", [lists:flatten(lists:duplicate(Indent, "-->")),NChild, NMeta, DATA]),
    {DATA_, Macc} = if
		NChild =/= 0 ->
		    parsechildren(Indent+1,lists:seq(1, NChild), DATA, MetaAcc);
		true-> {DATA, MetaAcc}
	    end,
%    io:fwrite("~sDATA after parsing children: ~p\n", [lists:flatten(lists:duplicate(Indent, "-->")),DATA_]),
    {DATA__, MAD}= readmetadata(Indent,NMeta, DATA_),
%    io:fwrite("~sDATA after metadata and children: ~p\n", [lists:flatten(lists:duplicate(Indent, "-->")),DATA__]),
    {DATA__, Macc+MAD};

parsenode(_,_,MetaAcc) ->
    {[], MetaAcc}.

    


t() ->
    IN = kw:file2lines("input.txt"),
    INL = string:tokens(string:chomp(lists:nth(1,IN))," "),
    DATA = lists:map(fun(X)->
			     list_to_integer(X) end,INL),
    parsenode(0, DATA,0).


