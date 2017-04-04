import socket
import json
import datetime
import time
import Adafruit_DHT as dht

# Logstash TCP/JSON Host
JSON_PORT = 5959
JSON_HOST = '192.168.3.101'

if __name__ == '__main__':
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((JSON_HOST, JSON_PORT))

		while True:
			h,t = dht.read_retry(dht.DHT22, 4)
			x = datetime.datetime.now()

			data = {'timestamp': '%s' % x, 'temperature': '%0.1f' % t, 'humidity': "%0.1f" % h}

			s.send(json.dumps(data))
			s.send('\n')
			time.sleep(60)

	# interrupt
	except KeyboardInterrupt:
		print("Program interrupted")

