import unittest
from producer import Producer


class TestProducedMessages(unittest.TestCase):

    # test if all messages are produced
    def test_all_message_produced(self):

        self.assertEqual(Producer.topic.latest_available_offsets()[0].offset[0] - Producer.topic.earliest_available_offsets()[0].offset[0], 100)

