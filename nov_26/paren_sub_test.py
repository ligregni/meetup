import unittest

from paren_sub import *

class ParenSub(unittest.TestCase):
    def check(self, s, r):
        self.assertEqual(longest_paren(s), r)

    def test_empty(self):
        self.check('', 0)

    def test_one_open(self):
        self.check('(', 0)

    def test_one_close(self):
        self.check(')', 0)

    def test_one_pair(self):
        self.check('()', 2)

    def test_one_wrong_pair(self):
        self.check(')(', 0)

    def test_two_nested(self):
        self.check('(())', 4)

    def test_two_concatenated(self):
        self.check('()()', 4)

    def test_two_concatenated_and_nested(self):
        self.check('(()())', 6)

    def test_two_groups_second(self):
        self.check('())(()())', 6)

    def test_two_groups_second(self):
        self.check('(()()))()', 6)
