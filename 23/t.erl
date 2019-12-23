-module(t).
-export([t/0]).

startbox(X) ->
    C = spawn(ic, run, [datan:datan(), self()]),
    C ! X, % set nic address
    io:fwrite("~p: NIC ~B\n", [C, X]),

    C.

setup() ->
    % spawn 50 boxen

    C = lists:map(fun(X)->
			  T=startbox(X),link(T), T end, lists:seq(0,49)),
    C.

broker(C,Buffer) ->
    
    % need a small state machine per thingy here.

    receive 
	    
	{Msg, From} ->
	    %io:fwrite("~p: ~B\n", [From, Msg]),
	    NewBuffer = bapp(Buffer, From, Msg, C)
    end,
    broker(C, NewBuffer).

% keep the state of the thing to puzzle the msgs together	   
bapp(B, F, M, C) ->
    
    Check = maps:is_key(F,B),
    if Check ->
	    L = maps:get(F, B)++[M];
       true ->
	    L = [M]
    end,
    Len = length(L),
    if 
	Len == 3 ->
	    % send to other box
	    A = lists:nth(1, L),
	    if A < 50 ->
		    X = lists:nth(2,L),
		    Y = lists:nth(3,L),
		    Addr = lists:nth(A+1, C),

		    io:fwrite("(~B,~B)->~B (~p) [~p]\n", [X,Y,A,Addr,L]),

		    
		    Addr ! X,
		    Addr ! Y,
		    NB = maps:remove(F, B);
	       true ->
		    X = lists:nth(2,L),
		    Y = lists:nth(3,L),
		    io:fwrite("(~B,~B)->~B [~p]\n", [X,Y,A,L]),
		    NB = maps:remove(F, B),
		    exit(normal)
	    end;
		
	true ->
	    NB = maps:put(F, L, B)
    end,

    NB.
    
    

t() ->
    C=setup(),
    broker(C,#{}).

% 42283 - too high
