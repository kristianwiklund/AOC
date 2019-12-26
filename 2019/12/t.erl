-module(t).
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
-export([run/0]).

s(A,B) ->
    %io:fwrite("~w,~w\n",[B,A]),
    if B =/= A ->
	    (B-A)/abs(B-A);
       true ->
	    0
    end.

gravity({X1,Y1,Z1},{X2,Y2,Z2}) ->
    
    DX = s(X1,X2),
   DY = s(Y1,Y2),
    DZ = s(Z1,Z2),
    {DX,DY,DZ}.

vadd({X1,Y1,Z1},{DX,DY,DZ}) ->
    {X1+DX,Y1+DY,Z1+DZ}.

vsub({X1,Y1,Z1},{DX,DY,DZ}) ->
    {X1-DX,Y1-DY,Z1-DZ}.

testmoons() ->
    [{0, {-1,0,2},{0,0,0}},
     {1, {2,-10,-7},{0,0,0}},
     {2, {4,-8,8},{0,0,0}},
     {3, {3,5,-1},{0,0,0}}].


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
    runall(Moons, WS, Acc++[newspeed(W, Moons,{0,0,0})]);
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

comparepos1({_, A,_},{_,B,_}) ->
    A==B.

comparepos(true, [N|New], [O|Orig]) ->
    comparepos(comparepos1(N,O), New, Orig);
comparepos(false, _, _) ->
    false;
comparepos(true, _, _) ->
    true.


stupidmove(Moons, OrigMoons, Step) ->
    NewMoons = movemoons(Moons),
    
    Test = comparepos(true, NewMoons, OrigMoons),
    if
	Test ->
	    Step+2;
	true ->
	    stupidmove(NewMoons, OrigMoons, Step+1)
    end.

run() ->
    T = stupidmove(moons(), moons(), 0),
    io:fwrite("~B\n", [T]).

    
    

    
    
	    
    



    

    
    
    
