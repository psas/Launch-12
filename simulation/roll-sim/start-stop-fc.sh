#!/bin/sh

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON="/home/natronics/PSAS/flight-computer/av3-fc/fc"
NAME=fc
DESC=fc
PROJECTPATH="/home/natronics/PSAS/Launches/12/Launch-12/simulation/roll-sim/"

start_service () {
	mkdir -p /var/run/$NAME
	echo "Starting PSAS FC"
	start-stop-daemon --start --background --make-pidfile --pidfile /var/run/$NAME/$NAME.pid --chdir $PROJECTPATH --exec $DAEMON 
}

stop_service () {
	echo "stopping PSAS FC"
	start-stop-daemon --stop --quiet --pidfile /var/run/$NAME/$NAME.pid
}

case "$1" in
'start')
  start_service
  ;;
'stop')
  stop_service
  ;;
'restart')
  stop_service
  start_service
  ;;
*)
  echo "Usage: $0 { start | stop | restart }"
  ;;
esac

exit 0
