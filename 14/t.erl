-module(t).
-export([t/0,tdata1/0]).
-export([rchem/3]).
-export([cooker/4,cooker2/4]).
-export([readlines/1,readdata/1,readdata/2]).
-export([trycook/4]).
% minimum amount  of what I will get, and a tuple with how much and its components
tdata1() ->
    #{"FUEL"=>
	      {1,[{7,"A"},{1,"E"}]},
      "E" => {1,[{7,"A"},{1,"D"}]},
      "D" => {1,[{7,"A"},{1,"C"}]},
      "C" => {1,[{7,"A"},{1,"B"}]},
      "B" => {1,[{1,"ORE"}]},
      "A" => {10, [{10,"ORE"}]}}.
    
readlines(FileName) ->    {ok, Data} = file:read_file(FileName),
			      string:split(Data, ["\n"], [global]).
  
file2lines(File) ->
   {ok, Bin} = file:read_file(File),
   string2lines(binary_to_list(Bin), []).


string2lines("\n" ++ Str, Acc) -> [lists:reverse([$\n|Acc]) | string2lines(Str,[])];
string2lines([H|T], Acc)       -> string2lines(T, [H|Acc]);
string2lines([], Acc)          -> [lists:reverse(Acc)].

% line looks like this: 10 ORE => 10 A or 7 A, 1 B => 1 C
% split on =>, then split the first on , and recurse again
parsecomps([C|CS], Acc) ->
    %%io:fwrite("Component ~s\n", [C]),
    ToL = string:split(string:trim(C)," "),
    ToN = lists:nth(1,ToL),
    ToWhat = lists:nth(2,ToL),
    AccP = [{list_to_integer(ToN),ToWhat}|Acc],
    parsecomps(CS, AccP);
parsecomps(_,Acc) ->
    Acc.

readdata([""|LS], Acc) ->
    readdata(LS, Acc);
    
readdata([L|LS], Acc) ->
    %%io:fwrite("Parsing ~s\n", [L]),
    FromTo=string:split(string:trim(L)," => "),
    From = lists:nth(1,FromTo),
    To = lists:nth(2,FromTo),

    ToL = string:split(string:trim(To)," "),
    ToN = lists:nth(1,ToL),
    ToWhat = lists:nth(2,ToL),

    %%io:fwrite("From: ~s\n", [From]),
    Comps = string:split(From,",",all),
    %%io:fwrite("Comps: ~p\n", [Comps]),
    CompList = parsecomps(Comps,[]),
    
    AccP = maps:put(ToWhat,{list_to_integer(ToN),CompList},Acc),
    readdata(LS,AccP);
readdata(_, Acc) ->
    Acc.
    

readdata(FN) ->
    D = file2lines(FN),
    readdata(D, #{}).


rchem(Amount, What, Reactions) ->
    % I want at least Amount of What, what do I need to get that, and what do I get?
    {A, W} = maps:get(What,Reactions),
    Factor = (Amount div A) + if ((Amount rem A)>0) -> 1; true-> 0 end,
    
    {A*Factor,lists:map(fun({Am, Wh})->
			 {Am*Factor, Wh} end, W)}.


%% cooker helper

cooker1([{Amount, What}|AS], Store, Reactions) ->
    %%io:fwrite("Cooking: ~B units of ~s\n",[Amount, What]),  
    StoreP = cooker(Amount, What, Store, Reactions), % withdraw A W
    cooker1(AS, StoreP, Reactions);

cooker1([], Store, _) ->
    Store.

% cook the things we order, unless they are in store, in which case we pull them
cooker(Amount, What, Store, Reactions) ->
    
    if What=="ORE" ->
	    % increase the store with the amount of ore
	    %io:fwrite("Digging: for ~B ore\n", [Amount]),
	    TotalDug = maps:get("TOTALORE", Store)+Amount,
	    StoreP = maps:put("TOTALORE", TotalDug, maps:put(What, Amount, Store));
       true ->

	    Havekey = maps:is_key(What, Store),
	    HaveAmount = if Havekey -> (maps:get(What, Store)); true -> 0 end,
	    
	    if HaveAmount >= Amount ->
		    %io:fwrite("Consuming ~B units of ~s\n", [Amount, What]),
		    StoreP = maps:put(What, HaveAmount-Amount,Store);
	       true ->
		    
		   % %io:fwrite("Have ~B units of ~s, need ~B -> cooking ~B\n", [HaveAmount, What, Amount, Amount-HaveAmount]),
						% cook it
		    {Getting, Needed} = rchem(Amount-HaveAmount, What, Reactions),
		    
						% iterate over these to get what we cook
		    StoreP = maps:put(What, Getting-Amount+HaveAmount, cooker1(Needed, Store, Reactions))
	    end
    end,
    %io:fwrite("Done cooking ~s: Store now contains: ~p\n", [What, StoreP]),
    StoreP.


% cooker without infinite ore

cooker21([{Amount, What}|AS], Store, Reactions) ->
    %%io:fwrite("Cooking: ~B units of ~s\n",[Amount, What]),  
    StoreP = cooker2(Amount, What, Store, Reactions), % withdraw A W
    cooker21(AS, StoreP, Reactions);

cooker21([], Store, _) ->
    Store.

cooker2(Amount, What, Store, Reactions) ->

    if What == "ORE" ->
	    OreStore = maps:get("ORE", Store),
	    if OreStore-Amount =< 0 ->
		    % leave
		    StoreP= #{},
		    throw(failerror);
	       true ->
		    StoreP = maps:put("ORE", OreStore-Amount, Store)
	    end;
       true ->
    
	    Havekey = maps:is_key(What, Store),
	    HaveAmount = if Havekey -> (maps:get(What, Store)); true -> 0 end,
	    
	    if HaveAmount >= Amount ->
		    %%io:fwrite("Consuming ~B units of ~s\n", [Amount, What]),
		    StoreP = maps:put(What, HaveAmount-Amount,Store);
	       true ->
		    
		    %%io:fwrite("Have ~B units of ~s, need ~B -> cooking ~B\n", [HaveAmount, What, Amount, Amount-HaveAmount]),
						% cook it
		    {Getting, Needed} = rchem(Amount-HaveAmount, What, Reactions),
		    
						% iterate over these to get what we cook
		    StoreP = maps:put(What, Getting-Amount+HaveAmount, cooker21(Needed, Store, Reactions))
	    end
    end,
    
    
%%io:fwrite("Done cooking ~s: Store now contains: ~p\n", [What, StoreP]),
StoreP.
		    
	       
trycook(Amount,What, Store, Reactions) ->
    %io:fwrite("trying ~B\n", [Amount]),
    try
	cooker2(Amount, What, Store, Reactions),
	NewAmount = Amount*10,
	trycook(NewAmount, What, Store, Reactions)
    catch
	failerror ->Amount
    end.

trycook(What, Store, Reactions) ->
    Max = trycook(10000,What, Store, Reactions),
    Min = Max/10,
    Min.
    
t()->
    ok.

% 3568888
