-module(t).
-export([t/0,tt/1,makeworld/2]).

-include_lib("../../cecho/_build/default/lib/cecho/include/cecho.hrl").

setup() ->
    code:add_patha("../../cecho/_build/default/lib/cecho/ebin"),
    application:start(cecho),
        % Set attributes
    %cecho:cbreak(),
    %cecho:noecho(),
    %cecho:curs_set(?ceCURS_INVISIBLE),
    %cecho:refresh(),
    %cecho:erase(),
    %cecho:refresh().
    ok.



probespot(World, X, Y, Yprintoffset) ->

    %cecho:mvaddstr(0,0, io_lib:format("(~B,~B)",[X,Y])),
    Bot = spawn(ic, run, [datan:datan(), self()]),
    
    Bot ! X,
    Bot ! Y,
    receive
	Probe ->
	    if 
		Probe == 1 ->
		    %cecho:mvaddstr(Y+1-Yprintoffset,X+1,"#"),
		    ic:setcol(World, X,Y,1),
		    true;
	
		true ->
		    %cecho:mvaddstr(Y+1-Yprintoffset,X+1,"."),
		    false		    
	    end
    end.

t()->
    setup(),
    World = #{},
    D=lists:map(fun(Y)->
			lists:map(fun(X)->
					  probespot(World,X,Y,0) end, 
				  lists:seq(0,200))  end, lists:seq(0,50)),
    %application:stop(cecho),
    D.

% idea: use the above to identify the projection lines from the emitter
% use this to fit a square box within the lines. done

calculon(Y)->
    %setup(),
    World = #{},
    %Y= 707,
    T1 = lists:map(fun(X)->
		      T=probespot(World,X,Y, -100),T end, 
	      lists:seq(0,2000)),
    {T2,_}=lists:mapfoldl(fun(T,Acc)->
				  {if T ->
					   Acc;
				      true->0 end,Acc+1} end, 0, T1),
    T3 = lists:filter(fun(X)->
			      X=/=0 end,T2),
    LowX = lists:min(T3), 
    HighX = lists:max(T3),
    % use LowX and HighX to find the equation going from (0,0)
    
    % m1 = (100-0)/(LowX-0)
    % m2 = (100-0)/(HighX-0)
    
    SLeft = 100/LowX,
    SRight = 100/HighX,
    {{LowX,HighX },{SLeft,SRight}}.
    
    
 % x1≈-1421.538461538461, x2≈-1521.538461538461, y1≈-807.692307692308, y2≈-707.692307692308

% (x1,y1) = 1421,807
% (x2,y2) = 1521,707
% 14210807 - too high
% 12300699 - too low
% 12370703 - too bad
% 12420706 - wrong as well
% 1228069 - too low
% 
tt(Y) ->
    io:fwrite("Calculon!  ~B\n",[Y]),
    {{LX1, HX1},_} = calculon(Y),
    {{LX2, HX2},_} = calculon(Y+99),
    io:fwrite("CALCULAR!  ~B ~B ~B ~B ~B ~B\n",[LX1,HX1,LX2,HX2,-(LX2-HX1), LX1*10000+Y]),
    if (HX1-LX2) >= 99 ->
	    tt(Y-1);
       true ->
	    {{LX1, HX1},{LX2, HX2}, -(LX2-HX1), LX1*10000+Y}
    end.

ps2(World, X, Y) ->


    Bot = spawn(ic, run, [datan:datan(), self()]),
    
    Bot ! X,
    Bot ! Y,
    receive
	Probe ->
	    if 
		Probe == 1 ->

		    ic:setcol(World, X,Y,1);
		true ->
		    World
	    end
    end.

% create an image between Y and Y2



			     
dumptofile(World,X1,Y1,X2,Y2) ->
    {ok, S} = file:open("world.txt",[write]),

    lists:foreach(fun(Y)->
			  lists:foreach(fun(X) ->
						Test=ic:getcol(World,X,Y)=/=0,io:format(S,"~s,",
											[if Test->"#";true->" " end]) end, lists:seq(X1,X2)),io:format(S,"~s\n",[""]) end,
					lists:seq(Y1,Y2)).


makeworld(MinxX, MaxX,[Y|YS],World) ->
    io:fwrite("Y:~B\n",[Y]),
    NewWorld = lists:foldl(fun(X,Acc) ->    
				   io:fwrite("XY:~B,~B\n",[X,Y]),
				   ps2(Acc, X, Y) end, World, lists:seq(MinxX, MaxX)),
    makeworld(MinxX, MaxX, YS, NewWorld);
makeworld(_,_,_,World) ->
    World.

makeworld(Y1, Y2) ->
    World = makeworld(1200,1800,lists:seq(Y1,Y2),#{}),
    io:fwrite("world made\n"),
    dumptofile(World, 1200,Y1, 1800, Y2).
    
