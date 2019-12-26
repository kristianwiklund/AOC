from math import floor
f = open("1.txt","r")

def fuelinator(weight):
    fuel = floor(weight/3 - 2)
    if fuel<0:
        return 0

    return fuel + fuelinator(fuel)

   

totalfuel = 0
for t in f:
    m = int(t)
    fuel = fuelinator(m)
    print(fuel)
    totalfuel = totalfuel + fuel

print(totalfuel)

