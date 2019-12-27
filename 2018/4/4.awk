/begins shift/ {guard=$4}
/falls asleep/ {date=$1;time=$2}
/wakes up/ {print guard, $2-time,date, time, "-", $1,$2-1}
