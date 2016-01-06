# Launch 12 Debrief

## Objectives:


 1. :white_check_mark: **Launch** our LV2.3 airframe fall 2014
 1. :white_check_mark: **Successful flight** to at least 75% of projected altitude; recover all hardware intact.
 1. :white_check_mark: **Telemetry**
   - get data from:
      - :white_check_mark: Inertial sensors
      - :white_check_mark: Events (e.g., 'launch')
      - :x: Commands _read below_
   - :white_check_mark: Record telemetry on rocket
   - :white_check_mark: Live stream to ground
   - :white_check_mark: Record on ground
   - :white_check_mark: Real time display on ground
   - :x: Record on data creating device  _read below_
 1. **Ground Support**
   - :white_check_mark: Remote, safe, digital ignition control
   - :white_check_mark: Effective recovery
      - :white_check_mark: Coordination between recovery teams and mission control
      - :white_check_mark: Know rocket location immediately after landing
      - :white_check_mark: Easy transportation back to flight line
 1. **Experiments**
   - :white_check_mark: Roll control
      - :white_check_mark: Documented algorithm and analysis
      - :white_check_mark: Include control data in telemetry
   - :white_check_mark: Record raw GPS RF environment to SD card
   - Digital Video
      - :white_check_mark: Downward facing camera: _read below_
        - :white_check_mark: Record locally
        - :x: Live digital feed of camera to ground in integrated telemetry stream
        - :x: Record on ground
        - :x: Real time ground display
      - :x: Outward facing camera
        - :x: Record localy
        - :x: Optionally stream to ground


Overall this flight was a **huge** success!!


# Major Failures

## Main Parachute Opened Early

Though it didn't have an adverse effect on anything, the main parachute opened accidentally at apogee rather then at the planned altitude of 300 meters.

**[Breakdown of what likely caused this](parachute-system-failure.markdown)**


## Missing Data In Flight Log

We had a major failure in the data streaming system at the Flight Computer. There is several milliseconds of data missing at regular intervals. This data apparently never made it to the flight computer process.

**[Breakdown of missing data and causes](missing-fc-data.markdown)**


## No Streaming Camera

We had two cameras on linux embedded boards. The original idea was to be able to optionally stream either while writing the raw video to disk.

We ended up having enourmous trouble configuring the camera streaming/recording in a sane way. We fell back to record only for the primary (downward facing) camera. The secondary (outward facing camera) would stream at low resolution to the ground.

Due to time constraints we never implemented a true ground display, but instead simply used VLC to view and record video. This worked well in testing the day before flight.

During the terminal launch procedures (rocket fueled, armed, and on the launch tower) we were unable to get a signal from the secondary (outward facing camera). Some quick debugging determined that the camera had simply disappeared from the point of view of linux, the device was not enumerated.

The Flight Director made the decision to fly without the camera and that node was turned off. 

Back in the lab after the flight the problem was reproduced, the camera still didn't connect. After moving the ribbon cable slightly the camera came back.

We conclude that this failure was due to poor connector seating.
 

# Minor Issues

## Log Commands In Telemetry

It was our intention to listen to the command channels and record exactly when commands (such as FC On, Arm, or Launch) were sent from the flight director.

Unfortunately due to time constraints this was never implemented.

We did get some partial recording, there is an ARM message recorded by the flight computer in the logfile.


## Record Sensor Data At The Individual Nodes

Our flight computer is broken into parts that send data over an ethernet link to the primary flight computer. To try and guard against missing data over the network, it was intended to write to a microSD card on each and every sensor node.

After much discussion this was decided to be too low of priority and potentially complicated (introducing file system issues at the microcontroller level) to implement. Unfortunately we did actually loose data.

