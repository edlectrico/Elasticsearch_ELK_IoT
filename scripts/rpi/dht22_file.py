#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import time
import Adafruit_DHT as dht

if __name__ == '__main__':
	while True:
		h,t = dht.read_retry(dht.DHT22, 4)
		x = datetime.datetime.now()

		outFile = open("/home/pi/dht22/dht22.log", "a")
		outFile.write("%s, %0.1f, %0.1f\n" % (x, t, h))
		outFile.close()

		time.sleep(60)

