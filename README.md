### OrangeC


kafka-docker
============

Dockerfile for [Apache Kafka](http://kafka.apache.org/)

The image is available directly from [Docker Hub](https://hub.docker.com/r/wurstmeister/kafka/)

## Pre-Requisites

- check  [docker-compose.yml](https://raw.githubusercontent.com/wurstmeister/kafka-docker/master/docker-compose.yml) for setup


**NOTE:** ```KAFKA_LOG_RETENTION_MS: 60000``` messages will be deleted after 60 seconds

## Usage
Start cluster:
- ```docker-compose up -d ```

Install python libraries:
-  ```pip install -r requirements.txt ```

Run python:
- unittest ```test_producer.py```.
- Producer ```producer.py```.
- unittest ```test_produced_messages.py```: check all messages are produced.
- Consumer ```consumer.py```.
- unittest ```test_consumer.py```: check all messages are consumed.
