from math import floor
f = open("1.txt","r")

totalfuel = 0
for t in f:
    m = int(t)
    fuel = floor(m/3-2)
    totalfuel = totalfuel + fuel

print(totalfuel)

