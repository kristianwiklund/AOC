-module(t).
-export([t/0,t2/0, t3/0, t4/0, t5/0, pattern/2,applypattern/1,pmatrix/1,applypattern/2,datan/0]).
-export([app2/3,varannan/3, interleave/4, app2/1]).

datan() ->
    "59790677903322930697358770979456996712973859451709720515074487141246507419590039598329735611909754526681279087091321241889537569965210074382210124927546962637736867742660227796566466871680580005288100192670887174084077574258206307557682549836795598410624042549261801689113559881008629752048213862796556156681802163843211546443228186862314896620419832148583664829023116082772951046466358463667825025457939806789469683866009241229487708732435909544650428069263180522263909211986231581228330456441451927777125388590197170653962842083186914721611560451459928418815254443773460832555717155899456905676980728095392900218760297612453568324542692109397431554".

datan2() ->
    lists:flatten(lists:duplicate(10000,datan())).



pattern(1) ->
    [0,1,0,-1].

pattern(N, Length) ->
    BasePattern = lists:flatten(lists:map(fun(X)->
						  lists:duplicate(N, X) end, pattern(1))),
    Instances = (Length div length(BasePattern))+1,
    RepeatedPattern = lists:flatten(lists:duplicate(Instances, BasePattern)),
    lists:reverse(lists:nthtail(length(RepeatedPattern)-Length-1, lists:droplast(lists:reverse(RepeatedPattern)))).

pmatrix(Txt)->					
    TP1 = lists:map(fun(X)->pattern(X, length(Txt)) end, lists:seq(1,length(Txt))),
    TP1.

applypattern(Signal) ->
    Txt = Signal,
    NMatrix = lists:duplicate(length(Txt),Txt),
    PMatrix = pmatrix(Txt),
    TM1 = lists:zipwith(fun(X,Y)->
				lists:zipwith(fun(W,V)->
						      (W*V) end, X,Y) end,
			NMatrix,PMatrix),
    TM2 = lists:map(fun(X)->
			    lists:foldl(fun(W,Acc)->
						W+Acc end,0, X) end, TM1),
    TM3 = lists:map(fun(W)->
			    (abs(W) rem 10) end, TM2),
    TM3.


applypattern(Signal, 0)->
    Signal;


applypattern(Signal, N) ->
    applypattern(applypattern(Signal), N-1).


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

app2(Signal, Row, Acc) ->
    Length = length(Signal),
    if 
	Row>Length -> % this is okay
	    {[],0};
	
	Row>trunc(Length/2) -> % this is okay
	    {AccP, Sum} = app2(Signal, Row+1, Acc),
	    SumP = lists:nth(Row, Signal)+Sum,
	    {[(SumP)|AccP], SumP};

	Row == 1 -> % this is okay
	    Sum=varannan(Signal,1,0),
	    {AccP, SumP} = app2(Signal, Row+1, Acc),
	    {[(Sum)|AccP], Sum+SumP};
	Row =< trunc(Length/2) ->
	    {AccP,_} = app2(Signal, Row+1, Acc),
	    Pat = pattern(Row, Length),
	    Mx = lists:zipwith(fun(X,Y) -> X*Y end, Pat, Signal),
	    Sum = lists:foldl(fun(X,A)->X+A end, 0, Mx),
	    {[(Sum)|AccP], Sum};

	true ->
	    {[],0}
    end.

app2(Signal) ->
    {L,_} = app2(Signal,1,[]),
    lists:map(fun(X)->abs(X rem 10) end, L).

app2(Signal, 0)->
    Signal;

app2(Signal, N) ->
    io:fwrite("~B:starting\n", [N]),
    NS = app2(Signal),
    io:fwrite("~B:done\n", [N]),
    app2(NS, N-1).

t() ->
    Signal = datan(),
    NList = lists:map(fun(X)->X-48 end,Signal),
    TM3=applypattern(NList, 100),
    lists:map(fun(X)->X+48 end, TM3).


	    
t3() ->
   
    io:fwrite("orig: ~p\n",[t:applypattern([1,2,3,4,5,6,7,8])]),
    {L,_} = app2([1,2,3,4,5,6,7,8],1,[]),
    io:fwrite("new: ~p\n,",[lists:map(fun(X)->abs(X rem 10) end,L)]).

t2() ->
    NList = lists:map(fun(X)->X-48 end,datan2()),
    TM3=applypattern(NList, 100),
    TM4 = lists:map(fun(X)->X+48 end, TM3),
    {ok, S} = file:open("task2.txt", [write]),
    io:format(S, "~s", [TM4]).

t4() ->
    NList = lists:map(fun(X)->X-48 end,datan2()),
    TM3=app2(NList, 100),
    TM4 = lists:map(fun(X)->X+48 end, TM3),
    {ok, S} = file:open("task2.txt", [write]),
    io:format(S, "~s", [TM4]).

t5() ->
    Signal = datan(),
    NList = lists:map(fun(X)->X-48 end,Signal),
    TM3=app2(NList, 100),
    lists:map(fun(X)->X+48 end, TM3).


%signal1() ->
%    "12345678".



