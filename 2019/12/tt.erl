-module(tt).
-export([gravity/2]).
-export([vadd/2]).
-export([vsub/2]).
-export([moons/0]).
-export([testmoons/0]).
-export([newspeed/3]).
-export([runall/3]).
-export([updatemoons/3]).
-export([movemoons/1]).
-export([movemoons/2]).
-export([energy/1]).
-export([stupidmove/3]).
-export([stripmoonsx/2]).
-export([stripmoonsy/2]).
-export([stripmoonsz/2]).
-export([testmoons2/0]).
-export([flopp/0]).
-export([lmax/1]).
-export([x/0,y/0,z/0]).
-export([x2/0,y2/0,z2/0]).
-export([gcd/2,lcm/2]).

s(A,B) ->
    %io:fwrite("~w,~w\n",[B,A]),
    if B =/= A ->
	    (B-A)/abs(B-A);
       true ->
	    0
    end.

gravity({X1},{X2}) ->    
    DX = s(X1,X2),
    {DX}.

vadd({X1},{DX}) ->
    {X1+DX}.

vsub({X1},{DX}) ->
    {X1-DX}.

testmoons2() ->
    [{0, {-1,0,2},{0,0,0}},
     {1, {2,-10,-7},{0,0,0}},
     {2, {4,-8,8},{0,0,0}},
     {3, {3,5,-1},{0,0,0}}].

testmoons() ->
    [{0, {-8,-10,0},{0,0,0}},
     {1, {5,5,10},{0,0,0}},
     {2, {2,7,3},{0,0,0}},
     {3, {9,-8,-3},{0,0,0}}].


moons() ->
    [{0, {16,-8,13},{0,0,0}},
     {1, {4,10,10},{0,0,0}},
     {2, {17,-5,6},{0,0,0}},
     {3, {13,-3,0},{0,0,0}}].


newspeed(Moon, [M|Moons], Acc) ->
    
    {ID, Pos, _} = Moon,
    {ID2, Pos2, _} = M,
    
    if 
	ID == ID2 ->
	    newspeed(Moon,Moons, Acc);
	true ->
	    V1 = gravity(Pos, Pos2),
	    AccP = vadd(V1, Acc),
	    newspeed(Moon, Moons, AccP)
    end;
newspeed(_,_,Acc) ->
    Acc.

runall(Moons, [W|WS], Acc) ->
    runall(Moons, WS, Acc++[newspeed(W, Moons,{0})]);
runall(_,_,Acc) ->
    Acc.

updatemoons([Moon|Moons], [ND|Newspeeds], Acc) ->
    {ID, Pos, Vel} = Moon,
    N = vadd(ND, Vel),
    AccP = [{ID,vadd(Pos,N),N}|Acc],
    updatemoons(Moons, Newspeeds, AccP);
updatemoons(_,_,Acc) ->
    lists:reverse(Acc).
movemoons(Moons) ->
    Newspeeds = runall(Moons, Moons, []),
    Newmoons = updatemoons(Moons, Newspeeds, []),
    Newmoons.
movemoons(Moons, [_|Steps]) ->
    %io:fwrite("~B\n",[S]),
    NewMoons = movemoons(Moons),
    movemoons(NewMoons, Steps);
movemoons(Moons,_) ->
    Moons.

energy([M|Moons],Acc) ->
    {_, {X,Y,Z}, {DX,DY,DZ}} = M,
    Pot = abs(X)+abs(Y)+abs(Z),
    Kin = abs(DX)+abs(DY)+abs(DZ),
    energy(Moons,Acc+Pot*Kin);
energy(_,Acc) ->
    Acc.


energy(Moons) ->
    energy(Moons, 0).

% --

comparepos1({_,A,C},{_,B,D}) ->
    (A==B).

comparepos(true, [N|New], [O|Orig]) ->
    comparepos(comparepos1(N,O), New, Orig);
comparepos(false, _, _) ->
    false;
comparepos(true, _, _) ->
    true.

stripmoonsx([M|Moons], Acc) ->
    {ID, {X,_,_}, {DX,_,_}} = M,
    stripmoonsx(Moons, Acc ++ [{ID, {X}, {DX}}]);
stripmoonsx(_,Acc) ->
    Acc.

stripmoonsy([M|Moons], Acc) ->
    {ID, {_,Y,_}, {_,DY,_}} = M,
    stripmoonsy(Moons, Acc ++ [{ID, {Y}, {DY}}]);
stripmoonsy(_,Acc) ->
    Acc.

stripmoonsz([M|Moons], Acc) ->
    {ID, {_,_,Z}, {_,_,DZ}} = M,
    stripmoonsz(Moons, Acc ++ [{ID, {Z}, {DZ}}]);
stripmoonsz(_,Acc) ->
    Acc.


x2() ->
    stupidmove(stripmoonsx(moons(),[]), stripmoonsx(moons(),[]),0).

y2() ->
    stupidmove(stripmoonsy(moons(),[]), stripmoonsy(moons(),[]),0).

z2() ->
    stupidmove(stripmoonsz(moons(),[]), stripmoonsz(moons(),[]),0).

x() ->
    stupidmove(stripmoonsx(testmoons(),[]), stripmoonsx(testmoons(),[]),0).

y() ->
    stupidmove(stripmoonsy(testmoons(),[]), stripmoonsy(testmoons(),[]),0).

z() ->
    stupidmove(stripmoonsz(testmoons(),[]), stripmoonsz(testmoons(),[]),0).


stupidmove(Moons, OrigMoons, Step) ->
    NewMoons = movemoons(Moons),
    
    Test = comparepos(true, NewMoons, OrigMoons),
    if
	Test ->
	    Step+2;
	true ->
	    stupidmove(NewMoons, OrigMoons, Step+1)
    end.


    
    
lmax(XS)->
    lists:foldl(fun(X,Acc) ->
			if (X>Acc) ->
				X;
			   true -> Acc
			end
			end, 0, XS).

gcd(A, 0) ->
    A;
gcd(A,B) ->
    gcd (B, A rem B).

lcm(A,B) ->    
   trunc(abs(A*B)/gcd(A,B)).

lcm([X]) ->
    X.

flopp() ->
    lcm(x2(),lcm(y2(),z2())).


    

    
    
    
