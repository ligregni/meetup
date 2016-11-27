import unittest

from character_swapping import longest_swap, optimize_group

class OptimizeGroup(unittest.TestCase):
    def check(self, inp, indexes, outp):
        s = set(indexes)
        x = list(inp)
        optimize_group(x, indexes)
        self.assertEqual(''.join(x), outp)

    def test_empty(self):
        self.check('', [], '')

    def test_no_indexes(self):
        self.check('abcd', [], 'abcd')

    def test_indexes_dont_get_better(self):
        self.check('dcba', [0, 1, 2, 3], 'dcba')

    def test_indexes_can_get_better(self):
        self.check('acbd', [0, 1, 2, 3], 'dcba')

    def test_three_indexes_swaps(self):
        self.check('cabd', [0, 1, 3], 'dcba')

    def test_all_get_rearranged(self):
        self.check('abcd', [0, 1, 2, 3], 'dcba')

    def test_all_but_one_get_rearrenged(self):
        self.check('abcd', [0, 2, 3], 'dbca')

class CharacterSwapping(unittest.TestCase):
    def check(self, inp, indexes, outp):
        self.assertEqual(longest_swap(inp, indexes), outp)

    def test_empty(self):
        self.check('', [], '')

    def test_no_swaps(self):
        self.check('abcd', [], 'abcd')

    def test_swaps_dont_help(self):
        self.check('dcba', [(0, 3), (0, 1), (0, 2)], 'dcba')

    def test_swaps_help(self):
        self.check('acbd', [(0, 3), (0, 1), (0, 2)], 'dcba')

    def test_two_swaps(self):
        self.check('cabd', [(0, 3), (0, 1), (0, 2)], 'dcba')

    def test_all_swap(self):
        self.check('abcd', [(0, 1), (1, 2), (2, 3)], 'dcba')

    def test_all_but_one_swap(self):
        self.check('abcd', [(0, 2), (2, 3)], 'dbca')
