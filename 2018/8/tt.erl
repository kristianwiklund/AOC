-module(tt).
-export([tt/0]).

ind(N) ->
    lists:flatten(lists:duplicate(N,"-->")).


% ---

summetadata(_, 0, DATA) ->
    {DATA, 0};
summetadata(Indent, N, [D|DATA]) ->
%    io:fwrite("~sMeta: ~B\n", [lists:flatten(lists:duplicate(Indent, "-->")),D]),
    {DATA_,M} = summetadata(Indent, N-1, DATA),
    {DATA_, M+D}.

% ---


parsechildren(Indent, 0, DATA) ->
    {DATA, []};
parsechildren(Indent, N, DATA) ->
    
    {DATA_, Value} =  parsenode(Indent, DATA),
    {DATA__, Values} = parsechildren(Indent, N-1, DATA_),
    {DATA__, [Value|Values]}.
% ---

indexmetadata(Indent, 0, Children, DATA) ->
    {DATA, 0};
indexmetadata(Indent, N, Children, [D|DATA]) ->

    Value = 
	if 
	    (D>0) and (D=<length(Children)) ->
		lists:nth(D, Children);
	    true ->
		0
	end,
    {DATA_, Acc} = indexmetadata(Indent, N-1, Children, DATA),
    {DATA_, Acc+Value}.
	
% ---

parsenode(Indent, [NrChildren,NrMetadata|DATA]) ->
    
	if 
	    NrChildren == 0 ->
						% no children, the value of the node is the sum of the metadata
		summetadata(Indent, NrMetadata, DATA);
	    true -> 
						% children, we need to do the parsing of the children into an array
						% and use it for lookup of the values
						% we have NrChildren children
		{DATA__, Children} = parsechildren(Indent+1, NrChildren, DATA),
		indexmetadata(Indent, NrMetadata, Children, DATA__)
	end.
       

tt() ->
    IN = kw:file2lines("input.txt"),
    INL = string:tokens(string:chomp(lists:nth(1,IN))," "),
    DATA = lists:map(fun(X)->
			     list_to_integer(X) end,INL),
    parsenode(0, DATA).


