#!/usr/bin/python3

#cinput = [17,13,19]
#dinput = [0,2,3]

#cinput = [67,7,59,61]
#dinput = [0,1,2,3]

x=-1
kinput= [19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,x,x,x,x,x,x,x,x,x,x,29,x,853,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23]
#kinput = [67,7,x,59,61]
t = zip(kinput, range(0,len(kinput)))
t = filter(lambda x:x[0]>1,t)
cinput = list()
dinput = list()
for x in t:
    cinput.append(x[0])
    dinput.append(x[1])

# math.lcm doesn't work on lists..
from math import gcd

lcm = cinput[0]
for i in cinput[1:]:
  lcm = lcm*i//gcd(lcm, i)
print("max",lcm,lcm//cinput[0])

# lcm is the maximum possible number to hit if there are no requirements on staggering

found = False
for i in range(lcm//cinput[0],1,-1):

    # check each of the items in the cinput if we are compliant
    # each item must fulfill  ( cinput[0]*i-dinput[<item>]) % cinput[<item>] == 0
    found = True
    for j in range(0,len(cinput)):
        found = found and (0 == (cinput[0]*i-dinput[j])%cinput[j])
    if found:
        break
    

print(i)
print(lcm-i*cinput[0])

