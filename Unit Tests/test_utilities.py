from unittest import TestCase

from utilities import OneBasedList, permute_by_sorting, randomize_in_place, permute_without_identity, permute_with_all, \
    permute_by_cyclic


class TestOneBasedList(TestCase):
    def test_indexes(self):
        one_based = OneBasedList(range(10))
        regular = range(10)

        # Make sure everything is one off
        for i in range(1, 11):
            self.assertEquals(one_based[i], regular[i - 1])


class TestRandom(TestCase):
    def assert_notequal_contains(self, source, value, printValue=False):
        """
        Determines if the source contains the values but without being in the same order.
        :param source: The source to check.
        :param value: The value to check against.
        :param printValue: True if should print to the console, false otherwise.
        """
        if printValue:
            print(source)
        self.assertNotEqual(source, value, "The source and value should not be equal.")
        for x in value:
            self.assertIn(x, source)

    def test_permute_by_sorting(self):
        # Technically this could happen...
        self.assert_notequal_contains(permute_by_sorting([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_randomize_in_place(self):
        # Technically this could happen...
        collection = [1, 2, 3, 4, 5, 6]
        randomize_in_place(collection)
        self.assert_notequal_contains(collection, [1, 2, 3, 4, 5, 6])

    def test_permute_without_identity(self):
        # Technically this could happen...
        collection = [1, 2, 3, 4, 5, 6]
        permute_without_identity(collection)
        self.assert_notequal_contains(collection, [1, 2, 3, 4, 5, 6])

    def test_permute_with_all(self):
        # Technically this could happen...
        collection = [1, 2, 3, 4, 5, 6]
        permute_with_all(collection)
        self.assert_notequal_contains(collection, [1, 2, 3, 4, 5, 6])

    def test_permute_by_cyclic(self):
        # Technically this could happen...
        collection = [1, 2, 3, 4, 5, 6]
        collection = permute_by_cyclic(collection)
        self.assert_notequal_contains(collection, [1, 2, 3, 4, 5, 6])
