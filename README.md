# Elasticsearch ELK IoT
An Elasticsearch Stack based configuration to monitor sensor data into Kibana.

The idea of this repository is to give some tips and config files (for Logstash, for example) to deploy a PoC in which we are  able to monitor data received from sensors.

## Requisites
Obviously, we will need a Elastic Stack (previously known as ELK Stack) to Collect, Store and Visualize the data. The steps to deploy such environment are given below. Note: Here we've used the version 5.x of the stack.

### Download and install Logstash
1. Download Logstash from [here](https://www.elastic.co/downloads/logstash) depending on your OS version.
2. Prepare a logstash.conf config file or copy the file given in this repository to accept input TCP connections and output the results to the Elasticsearch database.
3. Run bin/logstash -f logstash.conf

### Download and install Elasticsearch
1. Download Elasticsearch from [here](https://www.elastic.co/downloads/elasticsearch) depending on your OS version.
2. Just run bin/elasticsearch (or bin\elasticsearch.bat on Windows)

### Download and install Kibana
1. Download Kibana from [here](https://www.elastic.co/downloads/kibana) depending on your OS version.
2. Open config/kibana.yml in an editor and set the elasticsearch.url to point at your Elasticsearch instance (by default it will be a commented line, so you just have to uncomment it to point to your localhost Elasticsearch instance).
3. Check your Kibana installation by pointing your browser at http://localhost:5601
```
username: elasticsearch
password: changeme
```
Now, if you have used (which I highly recommend) the given [logstash-tcp.conf]() file, then you should be able to test the whole stack by executing the given Python script. This script just sends via socket an String to Logstash. Logstash receives it and then sends it back to Elasticsearch. 

To check that the message has been correctly sent to both Logstash and Elasticsearch, do the following:
### Logstash
Just watch the terminal in which you have previously launched the Logstash instance. You should see something like the following message:

### Elasticsearch 
In a new terminal just type:
```
curl -XGET localhost:9200/_searchsearch
```
You should see a response like:
```
$ curl -XGET localhost:9200/_search

> ... {"_index":"logstash-2017.03.22","_type":"logs","_id":"AVr1gjIWwi6wlimJjWcA","_score":1.0,"_source":{"@timestamp":"2017-03-22T10:13:54.737Z","port":38228,"@version":"1","host":"127.0.0.1","message":"String message to Logstash"}}]}}
```