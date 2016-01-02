cor:
	split --filter='../../../../../gps/gps/read-max | ../../../../../gps/gps/soft-correlator 4092000 > $$FILE &' --bytes=102300 --suffix-length=4 --numeric-suffixes - sats/fft < JGPS

single:
	../../../../../gps/gps/read-max < JGPS@04.559925043 | ../../../../../gps/gps/soft-correlator 4092000

clean:
	rm -rf sats
	mkdir sats
