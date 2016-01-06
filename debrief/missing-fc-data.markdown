Missing Flight Data
===================


Background
----------

All the sensor data on the rocket are sent via UDP packets to the flight computer. Most of the sensors are physically on an ethernet link from a microcontroller somewhere on the rocket.

So that we can know whether or not we missed anything, every packet that is sent has a sequence number. If the flight computer receives a packet out of order, (e.g. 1,2,3,7) then it records a "Sequence Error" (SEQE) event to the log.

While parsing through the flight computer log from Launch 12 we noticed that every once and a while (roughly every 20 seconds or so) the FC reported a sequence error for almost every single sensor all at once.

This means we didn't receive several milliseconds of data every 20 seconds.

It appears to happen to every sensor at the same time which suggests a common point of failure, either the switch, the ethernet cable to the flight computer, or some problem with the flight computer itself.


Correlation
---------------

In attempt to figure out where the issue is I charted several variables, like acceleration, system voltage, etc. with an overlay of times we missed data. The hope is to find something that correlates with the dropped packets that will point in the direction of a cause.


**IO Wait**

The smoking gun in turned out to be the amount to time the kernel spent in IO Wait. Attached is a chart of CPU mode share between several types of usage, System, User, IO Wait, etc. This data is from the python system monitor code we wrote using the `psutil` python package.

Docs: <http://pythonhosted.org/psutil/#cpu>

![CPU Chart](photos/CPUwithgaps.png)

This chart spans from approximately L-20 minutes all the way to the time the flight computer shut down after landing. Just before the L-8 minute mark we turn on JGPS and start slamming the flight computer with data. This is when the problems start. The correlation with lost data is very evident.


**Flush**

Looking at the 'disk write' data the same pattern is there so it's clear the IO Wait is linux flushing the data to disk on a regular interval. I believe this is expected behavior.


Reproduction
------------------

Tonight in the lab I was able to recreate the dropped data using the following steps:

 1. Using the launch director table bring up the ground systems (LTC, TM4K, etc.)
 2. Turn on the flight computer
 3. Make sure everything is running normally
 4. Turn on the IMU
 5. Turn on JGPS
 6. Wait at least 40 seconds
 7. Turn off JGPS and IMU
 8. Stop the fc process
 9. Examine the logs


There appears to be the same pattern of missed packets.
