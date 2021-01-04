#!/bin/bash

(echo -n  0;cat $1 | sed 's/[^-0-9]/ /g' |  tr -d '\n' | tr -s ' ' | sed 's/ / + /g'; echo 0)|paste
