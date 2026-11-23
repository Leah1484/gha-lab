import unittest

from hello import greeting


class GreetingTests(unittest.TestCase):
    def test_greeting_returns_hello_world(self):
        self.assertEqual(greeting(), "Hello world!")
