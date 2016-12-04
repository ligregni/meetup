import unittest

from word_split import *

class WordSplitTest(unittest.TestCase):
    def check(self, string, words, expected):
        d = Dictionary(words)
        self.assertEqual(word_split(string, d), expected)

    def test_empty(self):
        self.check('', [], 0)

    def test_no_solution(self):
        self.check('abc', [], 0)

    def test_one_word(self):
        self.check('hello', ['hello'], 1)

    def test_two_words(self):
        self.check('helloworld', ['hello', 'world'], 2)

    def test_two_words_many(self):
        self.check('helloworldhey',
            ['hello', 'world', 'helloworld', 'hey'], 2)

