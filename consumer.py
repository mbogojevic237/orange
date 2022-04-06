
import json
from pykafka import KafkaClient


class Consumer():

    client = KafkaClient(hosts="localhost:9092")
    topic = client.topics['oc-interview-homework']

    def consumer(self):
        return self.topic.get_simple_consumer()



class ConsumeMessage():

    def div_check(self, n):

        if n % 3 != 0 and n % 5 != 0:
            return n
        if n % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
        if n % 3 == 0:
            return 'Fizz'
        if n % 5 == 0:
            return 'Buzz'

    def consumer_m(self):

        consumer = Consumer().consumer()

        for message in consumer:
            m =json.loads(message.value.decode('utf-8'))
            m['translatedEventSequence'] = self.div_check(m['eventSequnce'])

            with open("stackpath-homework-output.txt", "a") as f:
                f.write(str(m) + '\n')


if __name__ == '__main__':

    ConsumeMessage().consumer_m()
