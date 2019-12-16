-module(t).
-export([lcm/2,t/0,t2/0, t3/0, t4/0, t5/0, pattern/2,applypattern/1,pmatrix/1,applypattern/2,datan/0,datan2/0]).
-export([app2/4,varannan/3, interleave/4, app2/1, combinator/2, cunningcalc/3]).

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
    io:fwrite("~B:",[N]),
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

combinator(L1, L2) ->
    Mx = lists:zipwith(fun(X,Y) -> case X of -1 -> -Y;0->0;1->Y end end, L1, L2),
    Sum = lists:foldl(fun(X,A)->X+A end, 0, Mx),
    Sum.

gcd(A, 0) ->
    A;
gcd(A,B) ->
    gcd (B, A rem B).

lcm(A,B) ->    
   trunc(abs(A*B)/gcd(A,B)).

app2(Signal, Row, Acc, Siglen) ->
    Length = length(Signal),
    if 
	Row>Length -> % this is okay
	    {[],0};
	
	Row>trunc(Length/2) -> % this is okay
	    {AccP, Sum} = app2(Signal, Row+1, Acc, Siglen),
	    SumP = lists:nth(Row, Signal)+Sum,
	    {[(SumP)|AccP], SumP};

	Row == 1 -> % this is okay
	    Sum=varannan(Signal,1,0),
	    {AccP, SumP} = app2(Signal, Row+1, Acc, Siglen),
	    {[(Sum)|AccP], Sum+SumP};
	Row =< trunc(Length/2) ->	    
	    % do something really clever here
	    {AccP, _} = app2(Signal, Row+1, Acc, Siglen),
	    Sum = cunningcalc(Signal, Row, Siglen),
	    {[(Sum)|AccP], Sum};

	true ->
	    {[],0}
    end.

app2(Signal) ->
    {L,_} = app2(Signal,1,[], length(Signal)),
    lists:map(fun(X)->abs(X rem 10) end, L).

app2(Signal, 0, Siglength)->
    Signal;

app2(Signal, N, Siglength) ->
    io:fwrite("~B:",[N]),
    {NS,_} = app2(Signal,1,[],Siglength),
    app2(NS, N-1, Siglength).

t() ->
    Signal = datan(),
    NList = lists:map(fun(X)->X-48 end,Signal),
    TM3=applypattern(NList, 100),
    lists:map(fun(X)->X+48 end, TM3).


	    
t3() ->
    Signal = lists:flatten(lists:duplicate(100,[1,2,3,4,5,6,7,8])),
    io:fwrite("orig: ~p\n",[t:applypattern(Signal)]),
    {L,_} = app2(Signal,1,[],8),
    io:fwrite("new: ~p\n,",[lists:map(fun(X)->abs(X rem 10) end,L)]).

t2() ->
    NList = lists:map(fun(X)->X-48 end,datan2()),
    TM3=applypattern(NList, 100),
    TM4 = lists:map(fun(X)->X+48 end, TM3),
    {ok, S} = file:open("task2.txt", [write]),
    io:format(S, "~s", [TM4]).

t4() ->
    NList = lists:map(fun(X)->X-48 end,datan2()),
    TM3=app2(NList, 100, 631),
    TM4 = lists:map(fun(X)->X+48 end, TM3),
    {ok, S} = file:open("task2.txt", [write]),
    io:format(S, "~s", [TM4]).

t5() ->
    Signal = datan(),
    NList = lists:map(fun(X)->X-48 end,Signal),
    TM3=app2(NList, 100,length(Signal)),
    TM4=lists:map(fun(X)->abs(X rem 10) end,TM3),
    lists:map(fun(X)->X+48 end, TM4).


%signal1() ->
%    "12345678".

% it should be possible to use the recurring pattern behavior to figure out how to do this quicker.
% the first pattern starts one step in, which means that the first (X-1) items are special on all
% rows. Then we have X items matching the calc pattern, where the first part of the item is actually the
% last of the input pattern (e.g. 81234567)

% example:

% pattern 1-8, row 2 (8 long), combinator on 3 patterns long -> -24, sum of 3 separate combinator -> -24
% row 3 -> pattern is 12 long, if we have an 8 long array, we need to use 2+3 to calc it
% so the first is run on a set of three "8s" and two patterns. Now, if we repeat this, we get double
% the sum, and so on

% Hence - if we generalize this, for a pattern of length N that will be applied to a data of length M
% if M=N -> run once, no worries
% if N!=M -> calculate lcm(N,M), then make sure that each fits within that banana lcm(N,M)/N patterns and lcm(N,M)/M datas

cunningcalc(Signal, Row, Siglen) ->
    N = Row*4,
    LCM = lcm(N,Siglen),
    PatRep = trunc(LCM/N),
    SigRep = trunc(LCM/Siglen),    

    if 
	length(Signal) > LCM ->
	    Pat = pattern(Row, Row*4),
	    {Sig,_} = lists:split(Siglen, Signal), 


	    %io:fwrite("Cunning: Signal length: ~B, Siglen: ~B, N: ~B, Patrep: ~B, Sigrep: ~B, LCM: ~B\n", [length(Signal), Siglen, N, PatRep, SigRep, LCM]),
	    
	    combinator(lists:flatten(lists:duplicate(PatRep, Pat)), lists:flatten(lists:duplicate(SigRep, Sig)));
       true -> 
%	    io:fwrite("Classic: Signal length: ~B, Siglen: ~B, N: ~B, LCM: ~B\n", [length(Signal), Siglen, N, LCM]),
	    Pat = pattern(Row, length(Signal)),
	    Mx = lists:zipwith(fun(X,Y) ->
				       X*Y end, Pat, Signal),
	    Sum = lists:foldl(fun(X,A)->
				      X+A end, 0, Mx),
	    Sum
    end.


