 cat input | sort -n | awk 'BEGIN {pre=0} {print $1-pre;pre=$1}'  | sort | uniq -c
echo add 1 to 3, multiply the numbers
