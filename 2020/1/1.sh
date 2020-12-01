
(for i in `cat input`; do grep "^`expr 2020 - $i`\$" input; done;echo -n 1)|echo `tr '\n' '*'`|bc
