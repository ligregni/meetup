import unittest

import rectangle_overlap

class RectangleOverlapTest(unittest.TestCase):
    def check(self, result, rectangle1, rectangle2):
        self.assertEqual(
            rectangle_overlap.is_overlap(rectangle1, rectangle2), result)

    def test_no_overlap(self):
        self.check(False,
            ((0,0), (1,1)),
            ((2,2), (3,3)))
            
    def test_no_overlap_inverted(self):
        self.check(False,
            ((1,1), (0,0)),
            ((2,2), (3,3)))
            
    def test_no_overlap_reversed(self):
        self.check(False,
            ((2,2), (3,3)),
            ((1,1), (0,0)))
            
    def test_just_touch(self):
        self.check(True,
            ((2,2), (3,3)),
            ((2,2), (0,0)))
            
    def test_overlap(self):
        self.check(True,
            ((2,2), (5,5)),
            ((4,4), (0,0)))
            
    def test_contained(self):
        self.check(True,
            ((2,2), (3,3)),
            ((4,4), (0,0)))
            
    def test_contained_other_corner(self):
        self.check(True,
            ((2,3), (3,2)),
            ((4,4), (0,0)))
            
