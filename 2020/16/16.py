from tmp import check
import fileinput

sum=0
for line in fileinput.input():
    line=line.strip("\r\n")
    for p in line.split(","):
        if not check(int(p)):
            sum=sum+int(p)

print (sum)
