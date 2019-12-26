-module(t).
-export([sweep/0]).
-export([sweep1/2]).
-export([perms/1]).

% set up a chain of computerers
t1(A,B,C,D,E) ->
    %O = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0],
    %O = ic:datan(),
    O = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
    C5 = spawn(ic,run,[O, self()]),
    C4 = spawn(ic,run,[O, C5]),
    C3 = spawn(ic,run,[O, C4]),
    C2 = spawn(ic,run,[O, C3]),
    C1 = spawn(ic,run,[O, C2]),
    C1 ! A,
    C2 ! B,
    C3 ! C,
    C4 ! D,
    C5 ! E,
    C1 ! 0,
    receive
	X ->
	    X
    end.

    
perms([]) -> [[]];
perms(L)  -> [[H|T] || H <- L, T <- perms(L--[H])].


pad(S) ->
    T1 = lists:append("00000",S),
    T2 = lists:reverse(T1),
    {T3,_} = lists:split(5,T2),
    lists:reverse(T3).
    

sweep1([L|LS], Max) ->
    [A,B,C,D,E]= L,
    R = t1(A-48,B-48,C-48,D-48,E-48),
    if
	R > Max ->
	    sweep1(LS,R);
	true ->
	    sweep1(LS,Max)
    end;

sweep1(_,Max) ->
    Max.

sweep1() ->  
    L = perms("01234"),
    sweep1(L,0).

% -------------- new code here

setup(A,B,C,D,E) ->
    %O = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0],
    O = ic:datan(),
    %O = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
    %O = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10],
    C5 = spawn(ic,run,[O, self()]),
    C4 = spawn(ic,run,[O, C5]),
    C3 = spawn(ic,run,[O, C4]),
    C2 = spawn(ic,run,[O, C3]),
    C1 = spawn(ic,run,[O, C2]),
    C1 ! A,
    C2 ! B,
    C3 ! C,
    C4 ! D,
    C5 ! E,
    C1 ! 0,
    {C1,C2,C3,C4,C5}.

t(COMP,MAX) ->
    {C1,_,_,_,_} = COMP,
    %io:fwrite("*****t wait for msg\n"),
    receive
	X ->
	    %io:fwrite("Msg = ~p\n",[X]),
	    %io:fwrite("***** t sendmsg\n"),
	    C1 ! X,
	    if X > MAX ->    
		    t(COMP,X);
	       true ->
		      t(COMP,MAX)
	    end
     after
	 100 -> MAX
    end.

t(A,B,C,D,E) ->
    COMP = setup(A,B,C,D,E),
    t(COMP,0).


sweep([L|LS], Max) ->
    [A,B,C,D,E]= L,
    R = t(A-48,B-48,C-48,D-48,E-48),
    if
	R > Max ->
	    %io:fwrite("New max: ~B\n",[R]),
	    sweep(LS,R);
	true ->
	    %io:fwrite("Old max: ~B\n",[Max]),
	    sweep(LS,Max)
    end;

sweep(_,Max) ->
    Max.

sweep() ->  
    L = perms("98765"),
    V = sweep(L,0),
    io:fwrite("--> ~B\n", [V]).


    
