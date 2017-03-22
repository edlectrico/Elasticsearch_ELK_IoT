import socket
import json
import time
import random

# Logstash TCP/JSON Host
JSON_PORT = 5959
JSON_HOST = '127.0.0.1'

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((JSON_HOST, JSON_PORT))

        while True:
            temperature = random.uniform(0.0, 35.0) 
            data = {'message': 'temperature %1f C' % temperature, 'hostname': socket.gethostname()}

            s.send(json.dumps(data))
            s.send('\n')
            print ("Received temperature = %.1f C" % temperature)
            time.sleep(0.2)

    # interrupt
    except KeyboardInterrupt:
        print("Program interrupted")
