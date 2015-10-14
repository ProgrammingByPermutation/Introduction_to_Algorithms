from unittest import TestCase

from selection import *


class TestSelection(TestCase):
    def test_minimum(self):
        collection = [6, 7, 4, 3, 6, 8, 98, 3, 32, 6, 7, 4, 5, 1]
        self.assertEquals(minimum(collection), 1)

    def test_maximum(self):
        collection = [6, 7, 4, 3, 6, 8, 98, 3, 32, 6, 7, 4, 5, 1]
        self.assertEquals(maximum(collection), 98)

    def test_minimum_maximum(self):
        collection = [6, 7, 4, 3, 6, 8, 98, 3, 32, 6, 7, 4, 5, 1]
        self.assertEquals(minimum_maximum(collection), (1, 98))

    def test_randomized_select(self):
        collection = [6, 4, 8, 98, 3, 32, 7, 5, 1]
        # Test explicit min
        self.assertEquals(randomized_select(collection, 0, len(collection) - 1, 1), 1)

        # Test explicit max
        self.assertEquals(randomized_select(collection, 0, len(collection) - 1, len(collection)), 98)

        # Test that each entry in the collection is found to be in correct i-th smallest entry position
        print(collection)
        print(sorted(collection))
        print(collection)

        i = 1
        for entry in sorted(collection):
            self.assertEquals(randomized_select(collection, 0, len(collection) - 1, i), entry)
            i += 1
