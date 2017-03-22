import socket
import json
import time
from distancemeter import get_distance,cleanup

# Logstash TCP/JSON Host
JSON_PORT = 5959
JSON_HOST = '127.0.0.1'

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((JSON_HOST, JSON_PORT))

        while True:
            distance = get_distance()
            data = {'message': 'distance %.1f cm' % distance, 'distance': distance, 'hostname': socket.gethostname()}

            s.send(json.dumps(data))
            s.send('\n')
            print ("Received distance = %.1f cm" % distance)
            time.sleep(0.2)

    # interrupt
    except KeyboardInterrupt:
        print("Program interrupted")
