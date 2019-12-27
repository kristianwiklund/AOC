-module(t).
-export([t/0]).
-include_lib("../../../cecho/_build/default/lib/cecho/include/cecho.hrl").

setup() ->
    code:add_patha("../../../cecho/_build/default/lib/cecho/ebin"),
    application:start(cecho),
        % Set attributes
    %cecho:cbreak(),
    %cecho:noecho(),
    %cecho:curs_set(?ceCURS_INVISIBLE),
    %cecho:refresh(),
    %cecho:erase(),
    %cecho:refresh().
    ok.

findlimits([{{X,Y},_}|D],XMIN,YMIN,XMAX,YMAX) ->
    {X1,Y1,X2,Y2} = findlimits(D, XMIN,YMIN,XMAX,YMAX),
    {min(X,X1),min(Y,Y1),max(X2,X),max(Y2,Y)};
findlimits(_,XMIN,YMIN,XMAX,YMAX) ->
    {XMIN,YMIN,XMAX,YMAX}.
    
findlimits(D) ->
    findlimits(D, 
	       100000000000000000000000000000000000,
	       100000000000000000000000000000000000,
	       -100000000000000000000000000000000000,
	       -100000000000000000000000000000000000).

reallyprintfield([{{X,Y},_}|DS],DX,DY) ->
    cecho:mvaddstr(Y-DY+1,X-DX,"*"),
    reallyprintfield(DS, DX, DY);
reallyprintfield(_,_,_) ->
    cecho:refresh().


reallyprintfield(D,V) ->
    {{XMIN,YMIN,_,_},_,_} = V,
    reallyprintfield(D,XMIN,YMIN).

printfield(D, OLD, OLDD,Acc) ->
    {XMIN,YMIN,XMAX,YMAX} =  findlimits(D),
    V = {{XMIN,YMIN,XMAX,YMAX},XMAX-XMIN,YMAX-YMIN},
%    io:fwrite("~p\n", [V]),
    
    if 
	OLD==undefined ->
	    V;
	true ->
	    {_,OLDX, OLDY} = OLD,
	    if (OLDX < (XMAX-XMIN)) and (OLDY < (YMAX-YMIN)) ->
		    setup(),		    
		    cecho:mvaddstr(0,0,io_lib:format("~B seconds",[Acc])),		    
		    reallyprintfield(OLDD,V),
		    exit(normal);
	       true ->
		    V
	    end
    end.

move(D, OX,Acc)->
    
    D_ = lists:map(fun({{X,Y},{DX,DY}}) ->
			   {{X+DX,Y+DY},{DX,DY}} end, D),
    OX_ = printfield(D_,OX, D,Acc),
    move(D_, OX_,Acc+1).



t() ->
    move(datan:datan(),undefined,0).


