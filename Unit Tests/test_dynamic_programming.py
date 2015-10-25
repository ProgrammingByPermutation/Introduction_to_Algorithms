from unittest import TestCase

from dynamic_programming import *
from data_structures import *


class TestFastestWay(TestCase):
    def test_example(self):
        n = 6
        a = OneBasedList([1, 2])
        a[1] = OneBasedList([7, 9, 3, 4, 8, 4])
        a[2] = OneBasedList([8, 5, 6, 4, 5, 7])

        t = OneBasedList([1, 2])
        t[1] = OneBasedList([2, 3, 1, 3, 4])
        t[2] = OneBasedList([2, 1, 2, 2, 1])

        e = OneBasedList([2, 4])
        x = OneBasedList([3, 2])

        f_star, l_star, l = fastest_way(a, t, e, x, n)


        # Output should be:
        # line 1, station 6
        # line 2, station 5
        # line 2, station 4
        # line 1, station 3
        # line 2, station 2
        # line 1, station 1
        # print_stations(l, l_star, n)
