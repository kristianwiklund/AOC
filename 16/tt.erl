-module(tt).
-export([app2/4,varannan/3,datan/0, pattern/2]).
-export([t3/0, t4/0]).
datan() ->
    "59790677903322930697358770979456996712973859451709720515074487141246507419590039598329735611909754526681279087091321241889537569965210074382210124927546962637736867742660227796566466871680580005288100192670887174084077574258206307557682549836795598410624042549261801689113559881008629752048213862796556156681802163843211546443228186862314896620419832148583664829023116082772951046466358463667825025457939806789469683866009241229487708732435909544650428069263180522263909211986231581228330456441451927777125388590197170653962842083186914721611560451459928418815254443773460832555717155899456905676980728095392900218760297612453568324542692109397431554".


pattern(1) ->
    [0,1,0,-1].

pattern(N, Length) ->
    BasePattern = lists:flatten(lists:map(fun(X)->
						  lists:duplicate(N, X) end, pattern(1))),
    Instances = (Length div length(BasePattern))+1,
    RepeatedPattern = lists:flatten(lists:duplicate(Instances, BasePattern)),
    lists:reverse(lists:nthtail(length(RepeatedPattern)-Length-1, lists:droplast(lists:reverse(RepeatedPattern)))).

% the message is 631 long which means that the repeated pattern is like 100000000 characters long
% but since the sum is a sum of things, we don't have to calc all of it

% for each line, use a maximum of n items where n is a multiple of the
% signal required to match the pattern
% for the lines below trunc(L/2), we can get the sum of all lines using
% the previous line plus one more digit
% then 4, 8, 12 and so on. methinks

varannan([S1|Signal], B1, B2) ->
    S1*B1 + varannan(Signal, -B2, B1);

varannan(_,_,_) ->
    0.


interleave(List, Cnt, Offs, Sign) ->
    if Cnt > length(List) ->
	    0;
       true ->
	    io:fwrite("~B=~B\n",[Cnt, Sign*lists:nth(Cnt, List)]),
	    Sign*lists:nth(Cnt, List)+
		interleave(List, Cnt+Offs, Offs, Sign)
    end.

combinator(L1, L2) ->
    Mx = lists:zipwith(fun(X,Y) -> case X of -1 -> -Y;0->0;1->Y end end, L1, L2),
    Sum = lists:foldl(fun(X,A)->X+A end, 0, Mx),
    Sum.

app2(Signal, Row, Acc, Mults) ->
    Length = length(Signal),

    if 
	Row>Length*Mults -> % this is okay
	    {[],0};
	
	Row>trunc((Length*Mults)/2) -> % this is okay
	    {AccP, Sum} = app2(Signal, Row+1, Acc, Mults),
	    if (Row rem Length)>0 ->
		    Index = Row rem Length;
	       true->
		    Index = Length
	    end,

	    SumP = Sum + 
		lists:nth(Index, Signal),
	    {[abs(SumP rem 10)|AccP], SumP};

	Row == 1 -> % this is okay
	    Sum=varannan(lists:flatten(lists:duplicate(2,Signal)),1,0)*trunc(Mults/2),
	    {AccP, SumP} = app2(Signal, Row+1, Acc, Mults),
	    {[abs(Sum rem 10)|AccP], Sum+SumP};

% 1,2  x 6
%[[1,0,-1,0,1,0,-1,0,1,0,-1,0],
% [0,1,1,0,0,-1,-1,0,0,1,1,0],
% [0,0,1,1,1,0,0,0,-1,-1,-1,0],
% [0,0,0,1,1,1,1,0,0,0,0,-1],
% [0,0,0,0,1,1,1,1,1,0,0,0],

	Row =< trunc((Length*Mults)/2) ->	    
	    % do something really clever here
	    {AccP, Sum}=app2(Signal, Row+1, Acc, Mults),
						% only run as many as we need to run
						% row N starts with (N-1) zeros, so lets cut those off first
	
	    Pattern = pattern(Row, Mults*Length),
	    SumP = combinator(Pattern, lists:flatten(lists:duplicate(Mults,Signal))),
	    {[abs(Sum rem 10)|AccP], SumP};
		
	true ->
	    {[],0}
    end.

app2(Signal) ->
    {L,_} = app2(Signal,1,[],10000),
    lists:map(fun(X)->abs(X rem 10) end, L).

app2(Signal, 0)->
    Signal;

app2(Signal, N) ->
    io:fwrite("~B:",[N]),
    {NS,_} = app2(Signal,1,[],10000),
    app2(NS, N-1).

t3() ->
    Signal = lists:flatten(lists:duplicate(100,[1,2,3,4,5,6,7,8])),
    io:fwrite("orig: ~p\n",[t:applypattern(Signal)]),
    {L,_} = app2([1,2,3,4,5,6,7,8],1,[],100),
    io:fwrite("new: ~p\n,",[lists:map(fun(X)->abs(X rem 10) end,L)]).

t2() ->
    NList = lists:map(fun(X)->X-48 end,t:datan2()),
    TM3=t:applypattern(NList, 100),
    TM4 = lists:map(fun(X)->X+48 end, TM3),
    {ok, S} = file:open("task2.txt", [write]),
    io:format(S, "~s", [TM4]).
t4() ->
    NList = lists:map(fun(X)->X-48 end,t:datan2()),
    TM3=app2(t:datan(), 100),
    TM4 = lists:map(fun(X)->X+48 end, TM3),
    {ok, S} = file:open("task2.txt", [write]),
    io:format(S, "~s", [TM4]).



