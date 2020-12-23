-module(t).
-export([move/2,chopout/2]).

chopout(L, I) ->
    {L1,L2} = lists:split(I, L),
    L2Len = length(L2),
    {L1P,L2P} = if
	     L2Len < 3 ->
			{LT1,LT2} = lists:split(3-L2Len,L1),
			{LT2,L2++LT1};
		    true -> {LT1, LT2} = lists:split(3,L2),
			    {L1++LT2,LT1}
		end,
    {L1P,L2P}.
		 
	    
	    
move(L, Cup) ->
    I = string:str(L, [Cup]),
    L1 = chopout(L, I),
    L1.
    
