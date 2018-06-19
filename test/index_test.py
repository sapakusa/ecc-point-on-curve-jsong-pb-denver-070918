from unittest import TestCase
from ipynb.fs.full.index import *

class PointTest(TestCase):

    def test_on_curve(self):
        with self.assertRaises(RuntimeError):
            Point(x=-2, y=4, a=5, b=7)
        # these should not raise an error
        Point(x=3, y=-7, a=5, b=7)
        Point(x=18, y=77, a=5, b=7)
