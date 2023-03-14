# unittest

import unittest
from string import ascii_letters


def text_filter(s: str) -> str:

    result = ''.join(c for c in s if c in set(ascii_letters + ' '))
    return result.lower()


class TestTextFilter(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(text_filter('hello world'), 'hello world')

    def test_upper_lower(self):
        self.assertEqual(text_filter('Hello World'), 'hello world')

    def test_punctuation(self):
        self.assertEqual(text_filter('hello123.,/\\ world456!'), 'hello world')

    def test_not_ascii(self):
        self.assertEqual(text_filter('hello Питонистический world'), 'hello world')

    def test_total(self):
        self.assertEqual(text_filter('Hello123, Питонистический World!'), 'hello world')


if __name__ == '__main__':
    unittest.main(verbosity=2)