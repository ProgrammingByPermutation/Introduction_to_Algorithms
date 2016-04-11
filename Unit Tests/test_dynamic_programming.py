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

        dims = [p[x].shape[0] for x in range(len(p))] + [p[len(p) - 1].shape[1]]
        recursive_solution = recursive_matrix_chain(dims, 0, len(dims) - 2)

        memoized_solution = memoized_matrix_chain(p)

        self.assertEqual(m[0, len(p) - 1], 15125)
        self.assertEqual(ordered_string, "((A(AA))((AA)A))")
        self.assertEqual(recursive_solution, 15125)
        self.assertEqual(memoized_solution, 15125)


class LCS(TestCase):
    def test_lcs_length(self):
        x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
        y = ['B', 'D', 'C', 'A', 'B', 'A']
        c, b = lcs_length(x, y)

        # Accept answers
        self.assertEqual(c[0], [0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(c[1], [0, 0, 0, 0, 1, 1, 1])
        self.assertEqual(c[2], [0, 1, 1, 1, 1, 2, 2])
        self.assertEqual(c[3], [0, 1, 1, 2, 2, 2, 2])
        self.assertEqual(c[4], [0, 1, 1, 2, 2, 3, 3])
        self.assertEqual(c[5], [0, 1, 2, 2, 2, 3, 3])
        self.assertEqual(c[6], [0, 1, 2, 2, 3, 3, 4])
        self.assertEqual(c[7], [0, 1, 2, 2, 3, 4, 4])

        self.assertEqual(b[0], [None, None, None, None, None, None, None])
        self.assertEqual(b[1], [None, "up", "up", "up", "up_left", "left", "up_left"])
        self.assertEqual(b[2], [None, "up_left", "left", "left", "up", "up_left", "left"])
        self.assertEqual(b[3], [None, "up", "up", "up_left", "left", "up", "up"])
        self.assertEqual(b[4], [None, "up_left", "up", "up", "up", "up_left", "left"])
        self.assertEqual(b[5], [None, "up", "up_left", "up", "up", "up", "up"])
        self.assertEqual(b[6], [None, "up", "up", "up", "up_left", "up", "up_left"])
        self.assertEqual(b[7], [None, "up_left", "up", "up", "up", "up_left", "up"])

        self.assertEqual(print_lcs(b, x), "BCBA")
