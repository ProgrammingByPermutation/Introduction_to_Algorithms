from unittest import TestCase

from selection import *


class TestSelection(TestCase):
    def test_minimum(self):
        collection = [6, 7, 4, 3, 6, 8, 98, 3, 32, 6, 7, 4, 5, 1]
        self.assertEquals(minimum(collection), 1)
