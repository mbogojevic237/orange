
import unittest
from producer import Producer, PMessage
import uuid
from datetime import datetime
import json



class TestProduc(unittest.TestCase):

    # test all mesage are created
    def test_message(self):

        for i in range(0, 100):
            message = PMessage(str(uuid.uuid4()), datetime.now().isoformat(), i + 1)
            m = json.dumps(message.__dict__)

            self.assertIsNotNone(m)

    # test if producer works
    def test_producer_running(self):

        producer = Producer().producer()
        self.assertTrue(producer._running)

    # test if topic exists
    def test_topic_exists(self):

        producer = Producer().producer()
        self.assertEqual(producer._topic.name, 'oc-interview-homework'.encode('utf-8'))







