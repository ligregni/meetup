import unittest

from clicks import Clicker, SegmentTree

class SegmentTreeTest(unittest.TestCase):
    def test_should_have_values(self):
        with self.assertRaises(AssertionError):
            segment = SegmentTree([])

    def test_should_have_positive_values(self):
        with self.assertRaises(AssertionError):
            segment = SegmentTree([1, 0, 4])

    def test_update_should_have_valid_index_negative(self):
        segment = SegmentTree([1, 7, 4])
        with self.assertRaises(AssertionError):
            segment.update(-1, 7)

    def test_update_should_have_valid_index_bounded(self):
        segment = SegmentTree([1, 7, 4])
        with self.assertRaises(AssertionError):
            segment.update(3, 7)

    def test_update_should_have_positive_value(self):
        segment = SegmentTree([1, 7, 4])
        with self.assertRaises(AssertionError):
            segment.update(3, 0)

    def test_size_returns_value(self):
        segment = SegmentTree([1, 7, 4])
        self.assertEqual(segment.size(), 3)

class ClickerTest(unittest.TestCase):
    def test_should_have_x(self):
        with self.assertRaises(AssertionError):
            clicker = Clicker([], [1])

    def test_should_have_y(self):
        with self.assertRaises(AssertionError):
            clicker = Clicker([1], [])

    def test_resize_should_be_valid_index(self):
        clicker = Clicker([1,2,3], [4,4,4])
        with self.assertRaises(AssertionError):
            clicker.resize(Clicker.ROW, -1, 10)

        with self.assertRaises(AssertionError):
            clicker.resize(Clicker.ROW, 3, 10)

        with self.assertRaises(AssertionError):
            clicker.resize(Clicker.COLUMN, -1, 10)

        with self.assertRaises(AssertionError):
            clicker.resize(Clicker.COLUMN, 3, 10)

    def test_resize_should_be_a_positive_number(self):
        clicker = Clicker([1,2,3], [4,4,4])
        with self.assertRaises(AssertionError):
            clicker.resize(Clicker.ROW, 0, -1)

        with self.assertRaises(AssertionError):
            clicker.resize(Clicker.COLUMN, 0, -1)

    def test_click_should_be_positive_coordinate(self):
        clicker = Clicker([1,2,3], [4,4])
        with self.assertRaises(AssertionError):
            clicker.click(-1, 1)

        with self.assertRaises(AssertionError):
            clicker.click(1, -1)

