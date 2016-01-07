all: data-unwrap

data-unwrap: fc-data tele-data
fullflight: full-flight cal-data

fc-data:
	mkdir -p fc-data
	cd fc-data; log2csv ../LAUNCH/flightcomputer.log

tele-data:
	mkdir -p tele-data
	cd tele-data; log2csv ../LAUNCH/telemetry.log

full-flight:
	mkdir -p full-flight
	cd full-flight; log2csv ../flightcomputer.log

cal-data:
	mkdir -p cal-data
	cd cal-data; log2csv ../flightcomputer-calibration.log
