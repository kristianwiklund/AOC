-module(t).
-export([t/0]).

-include_lib("../../cecho/_build/default/lib/cecho/include/cecho.hrl").

setup() ->
    code:add_patha("../../cecho/_build/default/lib/cecho/ebin"),
    application:start(cecho),
        % Set attributes
    cecho:cbreak(),
    cecho:noecho(),
    cecho:curs_set(?ceCURS_INVISIBLE),
    cecho:refresh(),
    cecho:erase(),
    cecho:refresh().



probespot(World, X, Y) ->
    cecho:mvaddstr(0,0, io_lib:format("(~B,~B)",[X,Y])),
    Bot = spawn(ic, run, [datan:datan(), self()]),
    
    Bot ! X,
    Bot ! Y,
    receive
	Probe ->
	    if 
		Probe == 1 ->
		    cecho:mvaddstr(Y+1,X+1,"#"),
		    ic:setcol(World, X,Y,1),
		    true;
	
		true ->
		    cecho:mvaddstr(Y+1,X+1,"."),
		    false		    
	    end
    end,
    cecho:refresh().

t()->
    setup(),
    World = #{},
    D=lists:map(fun(Y)->
			 lists:map(fun(X)->
					   probespot(World,X,Y) end, 
lists:seq(0,50)) end, lists:seq(0,50)),
    application:stop(cecho),
    D.

% idea: use the above to identify the projection lines from the emitter
% use this to fit a square box within the lines. done

