cat input | sed 's/^\(.*\)$/echo "\1"|.\/a.out/' > ap
(echo "0";bash -f ap 2>&1 | cut -d. -f1 | grep [0-9] | sed 's/$/ +/';echo p) | dc
