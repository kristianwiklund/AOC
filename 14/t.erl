-module(t).
-export([t/0,tdata1/0]).
-export([rchem/3]).
-export([cooker/4]).

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
    % I want at least Amount of What, what do I need to get that, and what do I get?
    {A, W} = maps:get(What,Reactions),
    Factor = (Amount div A) + if ((Amount rem A)>0) -> 1; true-> 0 end,
    
    {A*Factor,lists:map(fun({Am, Wh})->
			 {Am*Factor, Wh} end, W)}.


%% cooker helper

cooker1([{Amount, What}|AS], Store, Reactions) ->
    io:fwrite("Cooking: ~B units of ~s\n",[Amount, What]),  
    StoreP = cooker(Amount, What, Store, Reactions), % withdraw A W
    cooker1(AS, StoreP, Reactions);

cooker1([], Store, _) ->
    Store.

% cook the things we order, unless they are in store, in which case we pull them
cooker(Amount, What, Store, Reactions) ->
    
    if What=="ORE" ->
	    % increase the store with the amount of ore
	    io:fwrite("Digging: for ~B ore\n", [Amount]),
	    TotalDug = maps:get("TOTALORE", Store)+Amount,
	    StoreP = maps:put("TOTALORE", TotalDug, maps:put(What, Amount, Store));
       true ->

	    Havekey = maps:is_key(What, Store),
	    HaveAmount = if Havekey -> (maps:get(What, Store)); true -> 0 end,
	    
	    if HaveAmount >= Amount ->
		    io:fwrite("Consuming ~B units of ~s\n", [Amount, What]),
		    StoreP = maps:put(What, HaveAmount-Amount,Store);
	       true ->
		    
		    io:fwrite("Have ~B units of ~s, need ~B -> cooking ~B\n", [HaveAmount, What, Amount, Amount-HaveAmount]),
						% cook it
		    {Getting, Needed} = rchem(Amount-HaveAmount, What, Reactions),
		    
						% iterate over these to get what we cook
		    StoreP = maps:put(What, Getting-Amount+HaveAmount, cooker1(Needed, Store, Reactions))
	    end
    end,
    io:fwrite("Done cooking ~s: Store now contains: ~p\n", [What, StoreP]),
    StoreP.
		    
	       
	

t()->
    ok.
