import unittest

import primes

class PrimesTest(unittest.TestCase):
    def check(self, x, result):
        self.assertEqual(primes.is_prime(x), result)

    def test_negative(self):
        with self.assertRaises(AssertionError):
            primes.is_prime(-1)

    def test_zero(self):
        self.check(0, False)

    def test_one(self):
        self.check(1, False)

    def test_two(self):
        self.check(2, True)

    def test_three(self):
        self.check(3, True)

    def test_four(self):
        self.check(4, False)

    def test_five(self):
        self.check(5, True)

    def test_six(self):
        self.check(6, False)

    def test_seven(self):
        self.check(7, True)

    def test_ten(self):
        self.check(10, False)

