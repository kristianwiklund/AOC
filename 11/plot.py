import matplotlib.pyplot as plt
import csv

fd = open("bappelsin", "r")
reader = csv.reader(fd,delimiter=',')
xes = []
yes = []

for row in reader:
        print(row)
        if int(row[2]):
                xes.append(int(row[0]))
                yes.append(int(row[1]))

plt.plot(xes,yes,"ro")
#plt.show
