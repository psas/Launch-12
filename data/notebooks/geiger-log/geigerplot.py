#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib
import datetime
#countsRaw = open('radlog-3.dat','r')
counts = {}
times = []
numCounts = []
#while True:
#       ts = countsRaw.readline()
#       if not ts:
#               break
#       ts = ts.rstrip()
#       if ts in counts:
#               counts[ts] += 1
#       else:
#               counts[ts] = 1
#
countsRaw = open('radlog-4.dat','r')
while True:
        ts = countsRaw.readline()
        if not ts:
                break
        ts = ts.rstrip()
        if ts in counts:
                counts[ts] += 1
        else:
                counts[ts] = 1

for time in sorted(counts):
        times.append(datetime.datetime.fromtimestamp(float(time)))
        numCounts.append(counts[time])
        #print "%s %s" % (datetime.datetime.fromtimestamp(float(time)),counts[time])

plt.plot(times,numCounts)
plt.show()
