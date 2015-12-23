all: data-unwrap

data-unwrap: fc-data tele-data

fc-data:
	mkdir -p fc-data
	cd fc-data; log2csv ../LAUNCH/flightcomputer.log

tele-data:
	mkdir -p tele-data
	cd tele-data; log2csv ../LAUNCH/telemetry.log
