(sed "s/\(.\)/\1\n/g" | grep -v "^\$" | uniq -c | sed 's/^ *//' | sed 's/\([^ ]*\) \([^ ]\)/(\1-1)*\2+/g'| tr -d '\n';echo "0")| bc -l
