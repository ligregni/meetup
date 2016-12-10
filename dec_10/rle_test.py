import unittest

import rle

class RLETest(unittest.TestCase):
    def check(self, decompressed, compressed):
        decompressed_list = list(decompressed)
        rle.encode(decompressed_list)
        # print decompressed, decompressed_list
        self.assertEqual(
            decompressed_list[:decompressed_list.index(None)],
            list(compressed))

    def test_empty(self):
        self.check('', '')

    def test_one_char(self):
        self.check('a', 'a')

    def test_all_one(self):
        self.check('abcd', 'abcd')

    def test_two(self):
        self.check('abbd', 'abbd')

    def test_three(self):
        self.check('aaa', '3a')

    def test_many(self):
        self.check('aaabbbbbcddeee', '3a5bcdd3e')

    def test_many_double_digit(self):
        self.check('aaabbbbbbbbbbbbc', '3a12bc')

