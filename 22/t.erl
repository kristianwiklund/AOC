-module(t).
-export([t/1,t1/0,dealinto/1, cut/2, dealwithincrement/2]).
-export([dwi/3, gcd/2, bignum/0]).
-export([mcut/2, mdwi/2, mrdealinto/1]).
dealinto(Deck) ->
	lists:reverse(Deck).

cut(Deck, N) when N>0 ->
    {Pre,Post} = lists:split(N,Deck),
    Post++Pre;
cut(Deck, N) when N<0 ->
    U = length(Deck)+N,
%    io:fwrite("~B,~B\n", [N,U]),
    cut(Deck, U);
    
cut(Deck, N) when N==0 ->
    Deck.

dealwithincrement([Card|Deck], Acc, Pos, Max, N) ->
    AccP = maps:put(dwi(Pos,Max,N), Card, Acc),

    dealwithincrement(Deck, AccP, Pos+1, Max, N);

dealwithincrement([],Acc,_,_,_) ->
    Acc.
    
dealwithincrement(Deck, N) ->
    I1= dealwithincrement(Deck, #{}, 0, length(Deck), N),
    I2 = maps:to_list(I1),
    I3 = lists:keysort(1,I2),
    lists:map(fun({_,Y})->Y end, I3).


% part one DONE
t1() ->
    D = lists:seq(0,10006),
    O = input:input(D),
    What = 2019,
    {NT,_} = lists:mapfoldl(
	   fun(X,Acc)->if X==What->{Acc,Acc+1};true->{0,Acc+1} end end,0, O),
    {value,N} = lists:search(fun (X)->X=/=0 end, NT),
    N.

% part 2, factory deck of 119315717514047 cards with the input repeated 101741582076661 times...
% what is the number of the card in position 2020

% idea - only keep track of position 2020

% reverse, is reverse. It moves whatever is in position N-2020 to 2020
% ellernåt

% cut displaces position 2020 to the side back and forth
% deal with increment is the tricky one.
% when we reverse it, we take each nth item and put it in order
% dwi N means that item 2020 ends up in position X...
% 1 2 3 4 5 6 7 8 9 0 DWI 3
% 0 7 4 1 8 5 2 9 6 3 
% reverse DWI, to find only what happens to position Pos

%t:dealwithincrement(
%[0,1, 2,3,4, 5,6,7, 8,9,10,11,12,13,14,15,16],3).
%[0,6,12,1,7,13,2,8,14,3, 9,15, 4,10,16, 5,11]

% 17 long
% position 7 -> orig 8
% position 11 -> orig 15

% this is a prime
bignum() ->
    119315717514047.
%    10007.

% %[0,1, 2,   3,4, 5,   6,7, 8,   9,10,11,   12,13,14,  15,16],3).
dwi(OrigPos, NrCards, Incr) ->
    (OrigPos*Incr) rem NrCards.

gcd(A, 0) -> A;
gcd(A, B) ->
    gcd(B, A rem B).


%modinv(A, B) ->
%    {G,X,_} = xgcd(A,B),
%    if G == 1 ->
%	    X rem B;
%       true ->
%	    throw(error)
%    end.


mcut({Sum,Mul,P}, Cut) ->
    
    X={(Sum-Cut), Mul, (P-Cut) rem t:bignum()},
    %io:fwrite("~p\n", [X]),
    X.

mdwi({Sum, Mul,P}, Inc) ->
    X={Sum*Inc, Mul*Inc, (P*Inc) rem t:bignum()},
    %io:fwrite("~p\n", [X]),
    X.

mrdealinto({Sum, Mul,P}) ->
    X={t:bignum()-Sum-1, -Mul, t:bignum()-P-1}, 
    %io:fwrite("~p\n", [X]),
    X.

rewot(Wot,S,M) ->
    A = (Wot - S) rem t:bignum(),
    B = M rem t:bignum(),
    Inv = lin:inv(B, t:bignum()),
    F = (Inv*A) rem t:bignum(),
    

    {F,t:bignum()+F}.
    

t(P)->    
    X=tinput:tinput({0,1,P}),
    %io:fwrite("~p\n",[X]),
    {S,M,Wot} = X,
    Test = Wot =/= ((S+M*P) rem t:bignum()),
    if 
	Test ->
	    io:fwrite("ERROR: ~B ~B\n",[Wot,(S+M*P) rem t:bignum()]);
	true->
	    ok
    end,

    Y=rewot(Wot, S, M),
    K=rewot(2020, S, M),
    

    io:fwrite("Wot: ~B, P: ~B Y: ~p K: ~p\n",[Wot, P,Y, K]).


    % solve for (A*C mod B = 1
    % (M*X+S) mod B = Wor
    %  MX mod B = Wot-S mod B
    
						% 
			 
    

