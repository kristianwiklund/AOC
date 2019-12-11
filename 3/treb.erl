-module(treb).
%%-export([two/1]).
-export([pwire/3]).
-export([parse/2]).
-export([intersect/1]).
-export([tsub/2]).
-export([orthogonal/2]).
-export([findcoll/2]).
-export([checko1/3]).
-export([crash/1]).
-export([tre1/0]).
-export([feppelize/4]).

findmin ([{X,Y}|CT],{Xmin,Ymin}) ->
    findmin (CT, {min(Xmin,X),min(Ymin,Y)});
findmin (_,M) -> 
    M.

findmax ([{X,Y}|CT],{Xmin,Ymin}) ->
    findmin (CT, {max(Xmin,X),max(Ymin,Y)});
findmax (_,M) -> 
    M.


tsub({X1,Y1},{X2,Y2}) ->
    {X1-X2,Y1-Y2}.

transpose ([C|CT],K)->
    {L,_} = lists:mapfoldl(fun(X,XC) ->
				   {tre:tsub(X,XC),XC} end, K, [C|CT]),
    L.

moveme (X,Y,DX,DY) ->
    {X+DX,Y+DY}.

pwire (["D"++D|W],{X,Y},C) ->
    P = moveme(X,Y,0,-list_to_integer(D)),
    pwire(W,P,[P|C]);
pwire (["U"++D|W],{X,Y},C) ->
    P = moveme(X,Y,0,list_to_integer(D)),
    pwire(W,P,[P|C]);
pwire (["L"++D|W],{X,Y},C) ->
    P = moveme(X,Y,-list_to_integer(D),0),
    pwire(W,P,[P|C]);
pwire (["R"++D|W],{X,Y},C) ->
    P = moveme(X,Y,list_to_integer(D),0),
    pwire(W,P,[P|C]);
pwire ([],_,C) ->
    [{0,0}|lists:reverse(C)].

orthogonal({{X1,Y1},{X2,Y2},_},{{A1,B1},{A2,B2},_}) ->
    TX = X1-X2,
    TY = Y1-Y2,
    TA = A1-A2,
    TB = B1-B2,
    if
	(TX == 0) and (TA == 0) -> false;
	(TY == 0) and (TB == 0) ->
	    false;
	true -> true
    end.
    
feppelize([X|XS],P,A,L) ->
    {X1,Y1} = X,
    {X2,Y2} = P,
    D = abs(X1-X2)+abs(Y1-Y2) + L,
    feppelize(XS, X, [{P,X,D}|A],D);
feppelize(_,_,A,_) ->
    A.


parse(S1,S2) ->
    L1=pwire(string:tokens(S1, ","),{0,0},[]),
    L2=pwire(string:tokens(S2, ","),{0,0},[]),
    [F1|F1S]=L1, %%transpose(L1,K),
    [F2|F2S]=L2, %%transpose(L2,K),
    {feppelize(F1S,F1,[],0),feppelize(F2S,F2,[],0)}.

checko2(A,[B|BS],P) ->
    O = orthogonal(A,B),
    if 
	O == false ->
	    checko2(A,BS,P);
	true ->
	    checko2(A,BS,[{A,B}|P])
    end;
checko2(_,[],P) ->
    P.

checko1([A|AS],B,P)->
    checko1(AS,B,checko2(A,B,P));
checko1([],_,P) ->
    P.

crash({{{X1,Y1},{X2,Y2},_},{{A1,B1},{A2,B2},_}}) ->
    %% vertical line. X of the second need to be within the X of the first
    %% then Y of the first need to be within the Y of the second
    Test1 = ((X1 == X2) and (((X1 < min(A1,A2)) or (X1 > max(A1,A2))) or ((B1<min(Y1,Y2)) or ((B1>max(Y1,Y2)))))),
    Test2 = ((Y1 == Y2) and (((Y1 < min(B1,B2)) or (Y1 > max (B1,B2))) or ((A1<min(X1,X2)) or ((A1>max(X1,X2)))))),
    if 
	Test1 ->
	    false;
	Test2 ->
		false;
	     true ->true
	end.

intersect({{{X1,Y1},{X2,Y2},_},{{A1,B1},{A2,B2},_},_}) ->
    if
	X1 == X2 ->
	    {X1,B1};
	true ->
	    {A1,Y1}
    end.
		  
findcoll(S1,S2) ->  
    {A,B} = parse(S1,S2),
    T = checko1(A,B,[]),
    C = lists:filter(fun(D)->crash(D) end,T),
    D = lists:map(fun({{A,B,D1},{E,F,D2}}) ->
			  {{A,B,D1},{E,F,D2},D1+D2} end, C),
    [F|FS] = lists:sort(fun({_,_,D1},{_,_,D2}) ->
				D2 > D1 end, D),
    F.

tre1() ->   
    findcoll("R997,D543,L529,D916,R855,D705,L159,U444,R234,U639,L178,D682,L836,U333,R571,D906,L583,U872,L733,U815,L484,D641,R649,U378,L26,U66,L659,D27,R4,U325,L264,D711,L837,D986,L38,U623,L830,D369,L469,D704,L302,U143,L771,U170,R237,U477,L251,D100,R561,D889,R857,D780,R258,D299,L975,D481,L692,D894,R847,D416,R670,D658,L537,U748,R468,D304,L263,D884,R806,D13,R288,U933,R4,U291,L809,D242,R669,D50,R106,D510,R409,U311,R101,D232,R370,D490,L762,D805,L981,D637,L987,U403,R965,U724,L404,D664,L687,U868,L808,D174,L363,D241,L54,D238,R444,U75,R683,U712,L759,D569,R349,D378,L576,U437,R137,D822,R21,D595,L602,U147,R959,U350,R964,U625,L718,U331,L252,D386,L251,U371,R973,D709,R915,D837,L7,U727,L501,D520,L626,U161,L287,D224,L821,U555,L312,U234,L335,D572,L113,U673,L615,D919,R925,U16,R211,U77,R630,U786,R850,D221,R939,U559,R887,U779,L222,D482,L252,D682,L904,U568,R317,D453,R689,D917,R845,U260,R69,U613,R528,D447,L791,D119,L268,U215,L806,U786,R465,D787,L792,D823,R526,D709,L362,D748,L518,U115,L898,U784,R893,U911,R98,U215,R828,D100,R153,U496,L938,D403,R886,D317,L849,D59,R156,D27,L64,D771,R956,U880,R313,D244,L483,D17,R72,U467,L475,D444,R554,D781,R524,D152,L771,U435,L622,D601,R733,D478,L686,D12,L525,D467,L302,D948,L966,U572,L303,U914,R54,D417,R635,D425,R640,D703,R17,D187,L195,U59,R166,D616,L557,U458,L743,D166,R328,D640,R908,D775,L151,D216,L964,D202,L534,D239,R998,U167,L604,D812,L527,U526,L640,U93,L733,D980,R607,D879,L593,D721,R454,U137,R683,D343,L38,D398,L81,U392,R821,U247,L361,D208,R763,D771,L515", "L1000,D189,L867,U824,L193,D12,R704,U83,R371,D858,L970,D56,R877,D448,R962,U239,R641,D198,L840,D413,R586,D920,R650,U919,R375,D540,L150,U995,R54,D200,R61,D974,R249,U893,R319,U930,R658,U680,R286,D186,R963,U553,L256,U629,L554,U576,R887,U595,R629,D680,L684,U556,L302,U348,R825,D252,L684,U705,L258,D72,R907,U702,L518,U440,R239,U258,R825,U27,L580,D613,R357,D468,R519,U833,L415,D822,L798,U904,R812,U76,R86,U252,R427,U637,L896,U147,L294,U381,R306,U423,L688,D336,R648,U677,L750,D218,L649,D360,R710,D64,R317,U232,R261,D167,L49,D138,L431,D505,L535,U294,L553,U969,L144,U227,R437,D397,R359,U848,L48,D992,R169,D580,L219,D525,R552,U546,R849,D722,R894,D735,L182,U570,R274,D349,R312,U430,R441,U183,R645,D308,L416,U333,L687,U202,L973,D736,R382,U260,L176,D207,R706,U52,L142,D746,L328,D413,R879,D429,L679,D695,L224,D462,R358,D124,L515,D629,L873,D759,L763,U28,R765,D426,L93,U927,L395,U243,L393,D488,L729,U100,R488,D83,R47,U92,L871,D410,R405,D993,R537,D10,L79,D218,L686,D563,L31,U885,L784,D462,L160,U345,R204,U275,R162,U164,R843,D578,R255,D456,L398,U470,L576,D973,L337,D971,R205,U264,R707,U975,L60,U270,R1,U808,R844,D884,L952,D435,L144,D374,R389,D741,R404,D398,R282,D807,L316,U136,L504,U720,R859,D925,L711,U343,L535,D978,R578,U636,L447,D298,R574,U590,L142,D802,L846,D617,L838,U362,R812,U295,L328,U162,L617,D857,L759,D251,L343,U394,R721,U320,R836,U726,L950,D612,R129,U549,L970,D87,L341,D269,L659,U550,R835,D318,L189,U278,R871,D62,R703,U807,L389,U824,R521,D175,L698,U313,L942,D810,L498,U18,R168,D111,R607").
			  
