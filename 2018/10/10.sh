#!/bin/bash

INPUT=input.txt

sed 's/[^<]*<\([^>]*\)>[^<]*<\([^>]*\)>.*/{{\1},{\2}},/' < $INPUT | tr -d '\n'| sed -e 's#^#-module(datan).\n-export([datan/0]).\ndatan() -> [#' -e 's/,$/]./'  > datan.erl
erlc datan.erl
erlc t.erl

erl -noinput -s t t -s init stop
