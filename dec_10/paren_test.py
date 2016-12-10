import unittest

import paren

class ParenTest(unittest.TestCase):
    def check(self, n, expected):
        # self.assertEqual(paren.solve(n), set(expected))
        self.assertEqual(paren.solve2(n), set(expected))

    def test_zero(self):
        self.check(0, [])

    def test_one(self):
        self.check(1, ['()'])

    def test_two(self):
        self.check(2, ['()()', '(())'])

    def test_three(self):
        self.check(3, ['(()())', '((()))', '()()()', '()(())', '(())()'])

    def test_four(self):
        self.check(4,
            ['((()()))', '(((())))', '(()()())', '(()(()))', '((())())',
             '()(()())', '()((()))', '()()()()', '()()(())', '()(())()',
             '(()())()', '((()))()', '(())()()', '(())(())'])

