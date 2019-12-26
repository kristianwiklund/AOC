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
    after
	1000 ->
	    io:fwrite("idle, sending NAT packet\n"),
	    {X,Y} = maps:get(255, Buffer),

	    Check = maps:is_key(4711, Buffer),
	    if Check ->
		    {XT,YT} = maps:get(4711, Buffer),
		    if 
			Y == YT ->
			    io:fwrite("~B\n", [Y]),
			    exit(normal);
		       true ->
			    ok
		    end;
	       true ->
		    io:fwrite("No NAT available, holding off\n")
			
		    
	    end,

	    lists:nth(1,C) ! X,
	    lists:nth(1,C) ! Y,	    
	    NewBuffer = maps:put(4711, {X,Y}, Buffer)
	   
	    
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
		    io:fwrite("NAT: ~B,~B\n", [X,Y]),
		    NB1 = maps:remove(F, B),
		    NB = maps:put(255,{X,Y}, NB1)
	    end;
		
	true ->
	    NB = maps:put(F, L, B)
    end,

    NB.
    
    

t() ->
    C=setup(),
    broker(C,#{}).

% 42283 - too high
