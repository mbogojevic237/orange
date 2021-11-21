
import json
import uuid
from datetime import datetime

from pykafka import KafkaClient


class PMessage():

    def __init__(self, eventid, eventTimestamp, eventSequence):

        self.eventid = eventid
        self.eventTimestamp = eventTimestamp
        self.eventSequnce = eventSequence


class Producer():

    client = KafkaClient(hosts="localhost:9092")
    topic = client.topics['oc-interview-homework']

    def producer(self):

        return self.topic.get_sync_producer()


class ProduceMessage():

    def produce_message(self):

        producer = Producer().producer()

        for i in range(0, 100):

            message = PMessage(str(uuid.uuid4()), datetime.now().isoformat(), i+1)
            m = message.__dict__
            producer.produce(json.dumps(m).encode('utf-8'))


if __name__ == '__main__':

    ProduceMessage().produce_message()



