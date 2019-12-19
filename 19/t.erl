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



probespot(X, Y) ->
    cecho:mvaddstr(0,0, io_lib:format("(~B,~B)",[X,Y])),
    Bot = spawn(ic, run, [datan:datan(), self()]),
    
    Bot ! X,
    Bot ! Y,
    receive
	Probe ->
	    if 
		Probe == 1 ->
		    cecho:mvaddstr(Y+1,X+1,"#");
	
		true ->
		    cecho:mvaddstr(Y+1,X+1,".")
		    
		end

    after
	1000 ->
	    cecho:mvaddstr(Y+1,X+1,"X")
    end,
    cecho:refresh().

t()->
    setup(),
    
    lists:foreach(fun(Y)->
			 lists:foreach(fun(X)->
					       probespot(X,Y) end, lists:seq(0,50)) end, lists:seq(0,50)).