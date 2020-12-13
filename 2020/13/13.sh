cat input | tr ',' '\n' | grep -v x | sed 's/^\(.*\)/1000510-(1000510\/\1)*(\1)-\1/' | bc
