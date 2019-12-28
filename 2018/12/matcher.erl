-module(matcher).
-export([match/1]).
% ._.##
match([A,B,C,D,E|STR], Acc) when {$.,$.,$#,$#,$T} == {A,C,D,E,$T} ->
REM = [B,C,D,E|STR],
match(REM,"#"++Acc);
% ##_._
match([A,B,C,D,E|STR], Acc) when {$#,$#,$.,$T} == {A,B,D,$T} ->
REM = [B,C,D,E|STR],
match(REM,"#"++Acc);
% ._#.#
match([A,B,C,D,E|STR], Acc) when {$.,$#,$.,$#,$T} == {A,C,D,E,$T} ->
REM = [B,C,D,E|STR],
match(REM,"#"++Acc);
% _###.
match([A,B,C,D,E|STR], Acc) when {$#,$#,$#,$.,$T} == {B,C,D,E,$T} ->
REM = [B,C,D,E|STR],
match(REM,"#"++Acc);
% #_#_.
match([A,B,C,D,E|STR], Acc) when {$#,$#,$.,$T} == {A,C,E,$T} ->
REM = [B,C,D,E|STR],
match(REM,"#"++Acc);
% #._#.
match([A,B,C,D,E|STR], Acc) when {$#,$.,$#,$.,$T} == {A,B,D,E,$T} ->
REM = [B,C,D,E|STR],
match(REM,"#"++Acc);
% .#.__
match([A,B,C,D,E|STR], Acc) when {$.,$#,$.,$T} == {A,B,C,$T} ->
REM = [B,C,D,E|STR],
match(REM,"#"++Acc);
match([_|STR],Acc) ->
match(STR,"."++Acc);
match(_,Acc) -> Acc.
match(S) -> lists:reverse(match(lists:flatten(io_lib:format(".....~s.....",[S])),"..")).
