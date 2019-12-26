-module(t).
-export([t/0,checkpoint1/0,combos/1]).

readline(Acc,Timeout) ->
    receive 
	A1->
	    if A1 > 255 ->
		    io:fwrite("~B\n", [A1]);
	       true ->
		    readline([A1|Acc],Timeout)
	    end
    after
	Timeout ->
	    lists:reverse(Acc)
    end.

readline() ->
    io:fwrite("~s",[readline("",100)]).

s(Bot, Prog) ->
    
    P = Prog++[10],
    lists:foreach(fun(X)->
			  Bot ! X end, P),
    readline().

ss(Bot, Prog) ->
    
    P = Prog++[10],
    lists:foreach(fun(X)->
			  Bot ! X end, P).


checkpoint1() ->
     [
      "easter egg",
      "sand",
      "fixed point",
      "coin",
      "spool of cat6",
      "shell",
      "hypercube",
      "asterisk"
     ].

forever(C) ->
    readline(),
    Command = io:get_line(">"),
    s(C, Command),
    forever(C).

% https://panduwana.wordpress.com/2010/04/21/combination-in-erlang/
combos(1, L) -> [[X] || X <-L];
combos(K, L) when K == length(L) -> [L];
combos(K, [H|T]) ->
    [[H | Subcombos] || Subcombos <- combos(K-1, T)]
    ++(combos(K, T)).
 
combos(L) ->
    lists:foldl(
        fun(K, Acc) -> Acc++(combos(K, L)) end,
        [[]],
        lists:seq(1, length(L))
    ).

readandsearch(C, Regexp) ->
    V = readline("",1000),

    {ok, MP} = re:compile(Regexp),
    
    X = re:run(V, Regexp),
    case X of
	nomatch ->
	    io:fwrite(">>> NO match with ~s\n", [Regexp]),
	    io:fwrite("------------------\n~s\------------------------",[V]),
	    false;
	{match, _} ->
	    io:fwrite("<<< MATCH with ~s\n", [Regexp]),
	    true
    end.
	    
    
dropandrununtildone(C, [L|LS], Dir, Regexp) ->
    
    io:fwrite("Trying ~p\n",[L]),


    Take=lists:map(fun(X) ->
		      T = lists:flatten(io_lib:format("take ~s",[X])) end, L),

    Drop=lists:map(fun(X) ->
		      T = lists:flatten(io_lib:format("drop ~s",[X])) end, L),

    lists:foreach(fun(X) -> io:fwrite("CMD>~s\n", [X]),ss(C, X), readline("",100) end, Take),
    
    ss(C, Dir),
    
    Result = readandsearch(C, Regexp),
    
    if
	Result ->
	    lists:foreach(fun(X) -> io:fwrite("CMD>~s\n", [X]),ss(C, X),readline("",100) end, Drop),
	    dropandrununtildone(C, LS, Dir, Regexp);
	true ->
	    io:fwrite(">>> ~p <<<",[L])
    end.
		
			 


forcecp1(C) ->
    Objects = combos(checkpoint1()),
    
    dropandrununtildone(C,Objects, "north", "heavier than|lighter than").

    
    % heavier than the detected
    % lighter than the detected




t()->

    C = spawn(ic, run, [datan:datan(), self()]),
    s(C, "east"),
    s(C, "take asterisk"),
    s(C, "north"),
    s(C, "north"),
    s(C, "take hypercube"),
    s(C, "north"),
    s(C, "take coin"),
    s(C, "north"),
    s(C, "take easter egg"),
    s(C, "south"),
    s(C, "south"),
    s(C, "south"),
    s(C, "south"),
    s(C, "west"),
    s(C, "west"),
    s(C, "take fixed point"),
    s(C, "north"),
    s(C, "take sand"),
    s(C, "south"),
    s(C, "east"),
    s(C, "east"),    
    s(C, "north"),
    s(C, "west"),
    s(C, "north"),
    s(C, "take spool of cat6"),
    s(C, "north"),
    s(C, "take shell"),
    s(C, "west"),

    % drop all crap on the ground
    IC1 = checkpoint1(),
    lists:foreach(fun(X)->T=lists:flatten(io_lib:format("drop ~s",[X])),s(C, T), io:fwrite(">>~s<<\n",[T]),timer:sleep(100) end, IC1),

    % try all combinations until we are there
    
    forcecp1(C),

    forever(C).
 
