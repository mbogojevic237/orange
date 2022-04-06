import unittest
from consumer import Consumer


class TestConsumer(unittest.TestCase):


    # test if producer is running
    def test_consumer_running(self):

        consumer = Consumer().consumer()
        self.assertTrue(consumer._running)

    # test if all messages are produced
    def test_all_message_consumed(self):

        topic = Consumer.topic
        m = topic.latest_available_offsets()[0].offset[0] - topic.earliest_available_offsets()[0].offset[0]

        with open('stackpath-homework-output.txt', 'r') as f:
            mf = len(f.readlines())

        self.assertEqual(m,mf)