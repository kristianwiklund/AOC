-module(ic).
%%-export([two/1]).
-export([readfile/1]).
-export([run/2]).
-export([datan/0]).
-export([datan2/0]).
-export([datan5/0]).
-export([datan9/0]).
-export([setnth/3]).
-export([mod/4]).

setnth(1, [_|Rest], New) ->
    [New|Rest];
setnth(I, [E|Rest], New) -> 
    [E|setnth(I-1, Rest, New)].


readfile(FileName) ->
		   {ok, Binary} = file:read_file(FileName),
		   string:tokens(erlang:binary_to_list(Binary), ",\n").

readfrom(48, Mem, Param, _) ->
    % position mode
    lists:nth(Param+1, Mem);
readfrom(49, _, Param, _) ->
    % immediate mode
    Param;
readfrom(50, Mem, Param,Rel) ->
    lists:nth(Param+Rel+1, Mem).

writeto(48, Mem, Param, _, Value)->
    %io:fwrite("~B->Mem[~B]\n",[Value,Param]),
    setnth(Param+1, Mem, Value);
writeto(49, _,_,_,_) ->
    exit(cannotwriteimmediateerror);
writeto(50, Mem, Param, Rel, Value) ->
    setnth(Param+Rel+1, Mem, Value).

updatemem(ProgMem, DataMem) ->
    lists:nthtail(length(DataMem)-length(ProgMem), DataMem).

setresultandcall(LongI, LIO, P3, ProgMem, DataMem, Pid, Rel, Result) ->
    DataMemP = writeto(lists:nth(LIO,LongI), DataMem, P3, Rel, Result),
    NewProgMem = updatemem(ProgMem,DataMemP),
    r(NewProgMem, DataMemP, Pid, Rel).

%------------------ instruction decoder -----------------------

decode(1, LongI, [P1,P2,P3|ProgMem], DataMem, Pid, Rel) ->
    A1 = readfrom(lists:nth(3,LongI), DataMem, P1, Rel),
    A2 = readfrom(lists:nth(4,LongI), DataMem, P2, Rel),
    Result = A1+A2,
    %io:fwrite("Add: ~B+~B=~B\n",[A1,A2,Result]),
    setresultandcall(LongI, 5, P3,ProgMem, DataMem, Pid, Rel, Result);

decode(2, LongI, [P1,P2,P3|ProgMem], DataMem, Pid, Rel) ->
    A1 = readfrom(lists:nth(3,LongI), DataMem, P1, Rel),
    A2 = readfrom(lists:nth(4,LongI), DataMem, P2, Rel),
    Result = A1*A2,
    %io:fwrite("Mul: ~B*~B=~B\n",[A1,A2,Result]),
    setresultandcall(LongI, 5, P3,ProgMem, DataMem, Pid, Rel, Result);

decode(3, LongI, [P1|ProgMem], DataMem, Pid, Rel) ->
    if 
	Pid == undefined ->
	    {ok, Result} = io:read("Enter value> ");
	true ->
	    receive
		Result ->
		    Result
	    end
    end,

    setresultandcall(LongI, 3, P1, ProgMem, DataMem, Pid, Rel, Result);

decode(4, LongI, [P1|ProgMem], DataMem, Pid, Rel) ->
    A1 = readfrom(lists:nth(3,LongI), DataMem, P1, Rel),
    if 
	Pid == undefined ->
	    io:fwrite("Output: ~B\n", [A1]);
	true ->
	    Pid ! A1
    end,
    r(ProgMem, DataMem, Pid, Rel);

decode(5, LongI, [P1,P2|ProgMem], DataMem, Pid, Rel) ->
    A1 = readfrom(lists:nth(3,LongI), DataMem, P1, Rel),
    A2 = readfrom(lists:nth(4,LongI), DataMem, P2, Rel),
    
    if 
	A1 =/= 0 ->
	    NewProgMem = lists:nthtail(A2,DataMem);
	true  ->
	    NewProgMem = lists:nthtail(length(DataMem)-length(ProgMem),DataMem)
    end,
    r(NewProgMem, DataMem, Pid, Rel);

decode(6, LongI, [P1,P2|ProgMem], DataMem, Pid, Rel) ->
    A1 = readfrom(lists:nth(3,LongI), DataMem, P1, Rel),
    A2 = readfrom(lists:nth(4,LongI), DataMem, P2, Rel),
    
    if 
	A1 == 0 ->
	    NewProgMem = lists:nthtail(A2,DataMem);
	true  ->
	    NewProgMem = lists:nthtail(length(DataMem)-length(ProgMem),DataMem)
    end,
    r(NewProgMem, DataMem, Pid, Rel);

decode(7, LongI, [P1,P2,P3|ProgMem], DataMem, Pid, Rel) ->
    A1 = readfrom(lists:nth(3,LongI), DataMem, P1, Rel),
    A2 = readfrom(lists:nth(4,LongI), DataMem, P2, Rel),
    
    if 
	A1 < A2 ->
	    Result = 1;
	true ->
	    Result = 0
    end,
    %io:fwrite("LT: ~B<~B=~B\n",[A1,A2,Result]),
    setresultandcall(LongI, 5, P3,ProgMem, DataMem, Pid, Rel, Result);


decode(8, LongI, [P1,P2,P3|ProgMem], DataMem, Pid, Rel) ->
    A1 = readfrom(lists:nth(3,LongI), DataMem, P1, Rel),
    A2 = readfrom(lists:nth(4,LongI), DataMem, P2, Rel),
    
    if 
	A1 == A2 ->
	    Result = 1;
	true ->
	    Result = 0
    end,
    %io:fwrite("EQ: ~B==~B=~B\n",[A1,A2,Result]),
    setresultandcall(LongI, 5, P3,ProgMem, DataMem, Pid, Rel, Result);

decode(9, LongI, [P1|ProgMem], DataMem, Pid, Rel) ->
    A1 = readfrom(lists:nth(3,LongI), DataMem, P1, Rel),
    r(ProgMem, DataMem, Pid, Rel+A1);


decode(99, _, _, DataMem, _, _) ->
    DataMem.

    

r([TLongI|L],O,Pid,Rel) ->
    I = TLongI rem 100,
    {T1,_} = lists:split(5,
			 lists:reverse("00000000"++
					   integer_to_list(TLongI))),
    %io:fwrite("Opcode ~B modes ~w\n",[I, T1]),

    decode(I,T1,L,O,Pid,Rel).

	
%%Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).

run(OP,Pid) ->
    O1 = array:from_list(OP,0), 
    O = array:to_list(array:set(10100,0,O1)),
    r(O,O,Pid,0),
    ok.

mod(X,Y,O,Pid) ->
    OP = setnth(2,O,X),
    OR = setnth(3,OP,Y),
    run(OR,Pid).

%----------------------------------------------------------------------------------------

datan() ->
    [3,8,1001,8,10,8,105,1,0,0,21,42,51,76,93,110,191,272,353,434,99999,3,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,3,9,1001,9,4,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,5,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99].


datan2() ->
    [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,2,23,6,27,1,27,5,31,2,6,31,35,1,5,35,39,2,39,9,43,1,43,5,47,1,10,47,51,1,51,6,55,1,55,10,59,1,59,6,63,2,13,63,67,1,9,67,71,2,6,71,75,1,5,75,79,1,9,79,83,2,6,83,87,1,5,87,91,2,6,91,95,2,95,9,99,1,99,6,103,1,103,13,107,2,13,107,111,2,111,10,115,1,115,6,119,1,6,119,123,2,6,123,127,1,127,5,131,2,131,6,135,1,135,2,139,1,139,9,0,99,2,14,0,0].

%t(P,X,Y,Pid) ->
%    R = lists:nth(1,mod(X,Y,P,Pid)).
    
datan5() ->
    [3,225,1,225,6,6,1100,1,238,225,104,0,
     1101,78,5,225,1,166,139,224,101,-74,224,224,4,224,
     1002,223,8,223,1001,224,6,224,1,223,224,223,1002,136,18,224,101,-918,224,224,4,224,
     1002,223,8,223,101,2,224,224,1,224,223,223,1001,83,84,224,1001,224,-139,224,4,224,
     102,8,223,223,101,3,224,224,1,224,223,223,1102,55,20,225,1101,53,94,225,2,217,87,224,1001,224,-2120,224,4,224,
     1002,223,8,223,1001,224,1,224,1,224,223,223,102,37,14,224,101,-185,224,224,4,224,
     1002,223,8,223,1001,224,1,224,1,224,223,223,1101,8,51,225,1102,46,15,225,1102,88,87,224,1001,224,-7656,224,4,224,
     102,8,223,223,101,7,224,224,1,223,224,223,1101,29,28,225,1101,58,43,224,1001,224,-101,224,4,224,
     1002,223,8,223,1001,224,6,224,1,224,223,223,1101,93,54,225,101,40,191,224,1001,224,-133,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,40,79,225,4,223,
     99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1107,226,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,374,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,404,101,1,223,223,1007,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,434,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,494,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,509,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,539,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,7,677,677,224,1002,223,2,223,1005,224,599,101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,644,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226].

datan9() ->
    [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,
     209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,
     63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,608,1029,1102,1,29,1006,1101,39,0,
     1016,1101,1,0,1021,1101,37,0,1008,1101,0,25,1003,1102,32,1,1002,1101,0,35,1007,1102,1,28,1009,
     1101,0,31,1012,1101,22,0,1010,1101,319,0,1026,1102,1,23,1019,1102,423,1,1024,1101,27,0,1017,
     1101,0,36,1005,1101,0,0,1020,1101,681,0,1022,1102,1,30,1015,1101,0,24,1004,1102,312,1,1027,1102,
     1,21,1000,1102,1,34,1018,1101,0,678,1023,1101,0,38,1011,1102,1,418,1025,1102,1,20,1014,1101,33,
     0,1001,1101,0,26,1013,1102,1,613,1028,109,3,1202,5,1,63,1008,63,36,63,1005,63,205,1001,64,1,64,1105,1,207,4,187,1002,64,2,64,109,11,21108,40,40,0,1005,1014,229,4,213,1001,64,1,64,1105,1,229,1002,64,2,64,109,-19,1202,6,1,63,1008,63,33,63,1005,63,255,4,235,1001,64,1,64,1105,1,255,1002,64,2,64,109,3,1201,8,0,63,1008,63,29,63,1005,63,277,4,261,1106,0,281,1001,64,1,64,1002,64,2,64,109,10,21107,41,42,3,1005,1011,299,4,287,1106,0,303,1001,64,1,64,1002,64,2,64,109,19,2106,0,0,1001,64,1,64,1105,1,321,4,309,1002,64,2,64,109,-15,21107,42,41,-2,1005,1010,341,1001,64,1,64,1106,0,343,4,327,1002,64,2,64,109,6,2101,0,-9,63,1008,63,30,63,1005,63,363,1106,0,369,4,349,1001,64,1,64,1002,64,2,64,109,-11,1208,-5,29,63,1005,63,389,1001,64,1,64,1106,0,391,4,375,1002,64,2,64,109,15,1206,-2,409,4,397,1001,64,1,64,1105,1,409,1002,64,2,64,109,-3,2105,1,5,4,415,1105,1,427,1001,64,1,64,1002,64,2,64,109,-18,21101,43,0,10,1008,1011,42,63,1005,63,447,1106,0,453,4,433,1001,64,1,64,1002,64,2,64,109,19,1205,1,467,4,459,1105,1,471,1001,64,1,64,1002,64,2,64,109,-5,2107,34,-8,63,1005,63,489,4,477,1106,0,493,1001,64,1,64,1002,64,2,64,109,-11,2102,1,-1,63,1008,63,28,63,1005,63,517,1001,64,1,64,1105,1,519,4,499,1002,64,2,64,109,8,2108,37,-5,63,1005,63,539,1001,64,1,64,1106,0,541,4,525,1002,64,2,64,109,17,1206,-8,557,1001,64,1,64,1105,1,559,4,547,1002,64,2,64,109,-11,1205,2,571,1105,1,577,4,565,1001,64,1,64,1002,64,2,64,109,-14,1207,0,25,63,1005,63,599,4,583,1001,64,1,64,1105,1,599,1002,64,2,64,109,32,2106,0,-8,4,605,1105,1,617,1001,64,1,64,1002,64,2,64,109,-27,2102,1,-5,63,1008,63,24,63,1005,63,639,4,623,1105,1,643,1001,64,1,64,1002,64,2,64,109,-16,2101,0,10,63,1008,63,25,63,1005,63,669,4,649,1001,64,1,64,1105,1,669,1002,64,2,64,109,22,2105,1,8,1106,0,687,4,675,1001,64,1,64,1002,64,2,64,109,-21,1208,8,32,63,1005,63,705,4,693,1105,1,709,1001,64,1,64,1002,64,2,64,109,19,1207,-5,36,63,1005,63,729,1001,64,1,64,1105,1,731,4,715,1002,64,2,64,109,9,21101,44,0,-5,1008,1017,44,63,1005,63,753,4,737,1105,1,757,1001,64,1,64,1002,64,2,64,109,-12,21108,45,46,5,1005,1015,773,1105,1,779,4,763,1001,64,1,64,1002,64,2,64,109,-8,2108,25,1,63,1005,63,801,4,785,1001,64,1,64,1105,1,801,1002,64,2,64,109,-12,2107,22,10,63,1005,63,817,1106,0,823,4,807,1001,64,1,64,1002,64,2,64,109,23,1201,-8,0,63,1008,63,38,63,1005,63,847,1001,64,1,64,1106,0,849,4,829,1002,64,2,64,109,-3,21102,46,1,4,1008,1014,46,63,1005,63,871,4,855,1106,0,875,1001,64,1,64,1002,64,2,64,109,5,21102,47,1,2,1008,1017,46,63,1005,63,899,1001,64,1,64,1105,1,901,4,881,4,64,99,21101,0,27,1,21101,0,915,0,1105,1,922,21201,1,42136,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,0,942,0,1106,0,922,21202,1,1,-1,21201,-2,-3,1,21101,0,957,0,1105,1,922,22201,1,-1,-2,1106,0,968,22101,0,-2,-2,109,-3,2105,1,0].
