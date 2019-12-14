-module(t).
-export([t/0,tdata1/0]).
-export([rchem/3]).

% minimum amount  of what I will get, and a tuple with how much and its components
tdata1() ->
    #{"FUEL"=>
	      {1,[{7,"A"},{1,"E"}]},
      "E" => {1,[{7,"A"},{1,"D"}]},
      "D" => {1,[{7,"A"},{1,"C"}]},
      "C" => {1,[{7,"A"},{1,"B"}]},
      "B" => {1,[{1,"ORE"}]},
      "A" => {10, [{10,"ORE"}]}}.
      



rchem(Amount, What, Reactions) ->
    % I want at least Amount of What, what do I need to get that?
    {A, W} = maps:get(What,Reactions),
    Factor = (Amount div A) + if ((Amount rem A)>0) -> 1; true-> 0 end,
    
    lists:map(fun({Am, Wh})->
			 {Am*Factor, Wh} end, W).  
    

t()->
    ok.
