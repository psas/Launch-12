#!/usr/bin/env python

# convert a geiger log file to a csv file with Calendar Dates

import numpy
import matplotlib.pyplot as plt
import matplotlib
import datetime

infile    = "radlog-4.dat"
outfile   = "geiger-4.csv"
counts    = {}
geigdata  = []
numCounts = []

countsRaw = open(infile,'r')
while True:
    ts = countsRaw.readline()
    if not ts:
            break
    ts = ts.rstrip()
    if ts in counts:
            counts[ts] += 1
    else:
            counts[ts] = 1

csvfile= open(outfile, 'w')

csvfile.write("#CalDate[0], Epoch[1], GeigerHits[2]\r\n")
for time in sorted(counts):
    #utc_offset =  datetime.datetime.utcfromtimestamp(float(time)) -datetime.datetime.fromtimestamp(float(time))
    #print(utc_offset)
    geigdata.append(datetime.datetime.utcfromtimestamp(float(time)))
    geigdata.append(time)
    geigdata.append(counts[time])
    s = str(geigdata[0]) + "," + str(geigdata[1]) + "," + str(geigdata[2]) + "\r\n"
    csvfile.write(s)
    geigdata = []

csvfile.close()

print("Done. Output in file: %s\r\n" % outfile)

