-module(t).
-export([tt/0]).
-include_lib("../../cecho/_build/default/lib/cecho/include/cecho.hrl").

tt()->
    Maze = maze:file2lines("input.txt"),
    {MX,MY} = maze:findstart(Maze, 64),
    code:add_patha("../../cecho/_build/default/lib/cecho/ebin"),
    application:start(cecho),
    % Set attributes
    cecho:cbreak(),
    cecho:noecho(),
    cecho:curs_set(?ceCURS_INVISIBLE),
    cecho:refresh(),
    cecho:erase(),
    cecho:refresh(),
    lists:foldl(fun(S,Y)->cecho:mvaddstr(Y, 1, S),Y+1 end, 1,Maze),
    cecho:refresh(),
    maze:findpath(Maze, MX, MY, 0).
