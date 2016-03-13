from unittest import TestCase

from dynamic_programming import *


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


class MatrixMultiplication(TestCase):
    def test_matrix_multiply(self):
        m = numpy.matrix('1 2 3; 4 5 6')
        n = numpy.matrix('7 8; 9 10; 11 12')

        output = matrix_multiply(m, n)
        self.assertTrue((output == numpy.matrix('58 64; 139 154')).all())

    def test_matrix_chain_order(self):
        p = [
            numpy.matrix([[0] * 35] * 30),
            numpy.matrix([[0] * 15] * 35),
            numpy.matrix([[0] * 5] * 15),
            numpy.matrix([[0] * 10] * 5),
            numpy.matrix([[0] * 20] * 10),
            numpy.matrix([[0] * 25] * 20)
        ]

        m, s = matrix_chain_order(p)
        ordered_string = print_optimal_parens(s, 0, len(p) - 1)
        
        self.assertEqual(m[0, len(p) - 1], 15125)
        self.assertEqual(ordered_string, "((A(AA))((AA)A))")
