import json
import uuid
from datetime import datetime

from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")
topic = client.topics['oc-interview-homework']

producer = topic.get_sync_producer()
consumer = topic.get_simple_consumer()


def div_check(n):

    if n % 3 != 0 and n % 5 != 0:
        return n
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'

def producer_m():
    for i in range(0,100):

        data = {}
        data['eventId'] = str(uuid.uuid4())
        data['eventTimestamp'] = datetime.now().isoformat()
        data['eventSequence'] = i+1
        data['translatedEventSequence'] = div_check(i+1)

        message = json.dumps(data)
        producer.produce(message.encode('utf-8'))

def consumer_m():
    for message in consumer:

        m = message.value.decode('utf-8')
        with open("stackpath-homework-output.txt", "a") as f:
            f.write(m+'\n')


producer_m()
consumer_m()
