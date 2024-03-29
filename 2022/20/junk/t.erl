-module(t).
-export([t/0,move/3,calcmove/3,index_of/2, run/3, tst/0, t2/0]).
-include_lib("stdlib/include/assert.hrl").

index_of(Item, List) -> index_of(Item, List, 1).

index_of(_, [], _)  -> not_found;
index_of(Item, [Item|_], Index) -> Index;
index_of(Item, [_|Tl], Index) -> index_of(Item, Tl, Index+1).



fixzor(A,B) when A<0 ->
    fixzor(A+B,B);
fixzor(A,B) when A>=B ->
    fixzor(A-B,B);

fixzor(A,_) ->
    A.

strip(B,FA) when B>FA->
    io:format("."),
    strip(B-FA,FA);
strip(B,FA) when B<(-FA) ->
    io:format("."),
    strip(B+FA,FA);
strip(B,_) ->
    B.
	  
calcmove(XP,I,B) ->
    V=(I+B),
    fixzor(V, length(XP)).

move(X,BB,FA) ->
    L = abs(length(X)-1),
    B = strip(BB,FA),
    if 
	(L==B) or (L==B) ->
	    X;
	true ->
	    I = index_of(BB,X),
	    {X1,[_|X2]}=lists:split(I-1,X),
	    XP1=X1++X2,
    
	    TO=calcmove(XP1,I-1,B),

	    {Y1,Y2} = lists:split(TO,XP1),

	    if 
		Y1==[] ->
		    Y2++[BB];
		Y2==[] ->
		    [BB]++Y1;
		true ->
		    Y1++[BB]++Y2
	    end
    end.

run(X,0,_)->
    X;

run(X,[Y|YS],FA) ->
    io:format("Moving ~p ~n",[Y]),
    V=move(X,Y,FA),
    run(V,YS,FA);

run(X,_,_) ->
    X.

run(X,N)->
    run(X,N,1000).

test1() ->
    D=[1, 2, -3, 3, -2, 0, 4],
    R = run(D,D),
    ?assert(R==[1, 2, -3, 4, 0, 3, -2]),
    ?assert(run([1, 2, -2, -3, 0, 3, 4],[-2])==[1, 2, -3, 0, 3, 4, -2]),
    ?assert(run([1, 2, -3, 0, 3, 4, -2],[0])==[1, 2, -3, 0, 3, 4, -2]),
    ?assert(run([1, 2, -3, 0, 3, 4, -2],[4])==[1, 2, -3, 4, 0, 3, -2]),
    ?assert(run([1, 2, -3, 0, 3, -4, -2],[-4])==[1, -4, 2, -3, 0, 3, -2]),
    ?assert(run([1, -4, 2, -3, 0, 3, -2],[-4])==[1, 2, -3, -4, 0, 3, -2]).

tst()->
    D = [1,2,4,3],
    R = run(D,[4]),
    R.

test3()->
    D = [1,2,4,3],
    R = run(D,[4]),
    ?assert(R==[1,2,3,4]),
    R.


test2() ->
    D = [1,4,2,3],
    R = run(D,[2]),
    ?assert(R==[1,2,4,3]),
    R.



test4() ->
    ?assert(run([4, 5, 6, 1, 7, 8, 9],[1])==[4, 5, 6, 7, 1, 8, 9]),
    ?assert(run([4, -2, 5, 6, 7, 8, 9],[-2])==[4, 5, 6, 7, 8, -2, 9]).

tests() ->
    test1(),
    test2(),
    test3(),
    test4().

magic(R2,FA) -> 
    I = index_of(0,R2),
    {R1,R2} = lists:split(I,R2),
    R = R2++R1,
    I2 = index_of(0,R),
    io:format("I2 is ~p in ~p~n",[I2,R]),
    io:format("~p ~p ~p~n",[(I2+1000) rem length(R),(I2+2000) rem length(R),(I2+3000) rem length(R)]),
    A =	strip(lists:nth((I2+1000),R),FA),
    B =	strip(lists:nth((I2+2000),R),FA),
    C =	strip(lists:nth((I2+3000),R),FA),
    {A,B,C,A+B+C}.

readfile(FileName) ->
    {ok, Binary} = file:read_file(FileName),
    Lines = string:tokens(erlang:binary_to_list(Binary), "\n"),
    lists:map(fun(X)->
		      list_to_integer(X)
	      end, 
	      Lines).


srun(D,0,_) ->
    D;
srun(D,N,FA) ->
    srun(run(D,D,FA),N-1,FA).


t()->
    tests(),
    D1 = readfile("pp.txt"),
    FA = lists:nth(length(D1),D1),
    D = lists:droplast(D1),
    R = run(D,D,FA),
    magic(R,FA).

t2()->
    tests(),
    D1 = readfile("pp2.txt"),
    FA = lists:nth(length(D1),D1),
    D = lists:droplast(D1),
    R = srun(D,10,FA),
    magic(R,FA).
