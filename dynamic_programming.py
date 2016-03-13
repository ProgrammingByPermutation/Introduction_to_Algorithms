import numpy

from data_structures import OneBasedList


def fastest_way(a, t, e, x, n):
    """
    Chapter 15: Computes the fastest way through a collection of stations depicted in 15.1 figures.
    :param a: The amount of time spent at a station. A two dimensional array [1...2][1...n].
    :param t: The amount of time to transfer from line 1 to line 2. A two dimensional array [1...2][1...n].
    :param e: The entrance time for the first station on line 1 or 2. A one dimensional array [1...2].
    :param x: The exit time for the last station on line 1 or 2. A one dimensional array [1...2].
    :param n: The number of stations.
    :return: A tuple where (fastest time through station, fastest line number to leave on, an array of fastest stations)

    The array of fastest stations (l) is setup such that l[line number][station number] is the fastest station
    (station number - 1) through station [line number][station number]. That being the case there is no index #1 since
    nothing proceeds the first station.

    To trace the fasted route from the output you would do the following:
    Start at "fastest line number to leave on". Assuming this is 1, we use station[1, n].
    Next we look at l[1][n] and use it's value. Assuming it's 2, we use station [2, n -1]
    Next we look at l[2][n - 1] and use it's value. Etc etc etc.

    See print_stations which does this trace.
    """
    f1 = [None] * (n + 1)
    f2 = [None] * (n + 1)
    l = OneBasedList([OneBasedList([None] * n), OneBasedList([None] * n)])

    f1[1] = e[1] + a[1][1]
    f2[1] = e[2] + a[2][1]

    for j in range(2, n + 1):
        if (f1[j - 1] + a[1][j]) <= (f2[j - 1] + t[2][j - 1] + a[1][j]):
            f1[j] = f1[j - 1] + a[1][j]
            l[1][j] = 1
        else:
            f1[j] = f2[j - 1] + t[2][j - 1] + a[1][j]
            l[1][j] = 2

        if (f2[j - 1] + a[2][j]) <= (f1[j - 1] + t[1][j - 1] + a[2][j]):
            f2[j] = f2[j - 1] + a[2][j]
            l[2][j] = 2
        else:
            f2[j] = f1[j - 1] + t[1][j - 1] + a[2][j]
            l[2][j] = 1

    if f1[n] + x[1] <= f2[n] + x[2]:
        f_star = f1[n] + x[1]
        l_star = 1
    else:
        f_star = f2[n] + x[2]
        l_star = 2

    return f_star, l_star, l


def print_stations(l, l_star, n):
    """
    Chapter 15: Prints the fastest way through the stations using the output of fastest_way.
    :param l: An array of the fastest way through the stations.
    :param l_star: The fastest station to exit from.
    :param n: The number of stations.
    """
    i = l_star
    print("line " + str(i) + ", station " + str(n))
    for j in range(n, 1, -1):
        i = l[i][j]
        print("line " + str(i) + ", station " + str(j - 1))


def matrix_multiply(a, b):
    """
    Multiplies two matrices. Matrices are assumed to use a 1 based index.
    :param a: The first matrix, expected numpy.matrix.
    :param b: The second matrix, expected numpy.matrix.
    :return: A matrix product (numpy.matrix).
    """

    def columns(matrix):
        return matrix.shape[1]

    def rows(matrix):
        return matrix.shape[0]

    if columns(a) != rows(b):
        raise Exception("incompatible dimensions")

    c = numpy.matrix([[None] * columns(b)] * rows(a))

    for i in range(0, rows(a)):
        for j in range(0, columns(b)):
            c[i, j] = 0

            for k in range(0, columns(a)):
                c[i, j] = c[i, j] + a[i, k] * b[k, j]

    return c


def matrix_chain_order(p):
    """
    Calculates the optimal order of multiplication that should take place to minimize the number of
    multiplications for a list of matrices.
    :param p: A list of numpy.matrix objects. The order should reflection the multiplication order.
    :return: A tuple where the first element is a numpy.matrix of the minimum number of multiplications required for
             each permutation of matrix multiplication. The total minimum will be at [0, len(p) - 1]. The second element
             is the numpy.matrix of indexes that achieved the optimal costs for the first element's table.
    """
    # To be a little more user friendly, we will convert the array of matrices to an array of dimensions that need
    # to be multiplied.
    #
    # It will be:
    # [The # of row elements for each matrix] + [The # of columns elements for the last matrix]
    #
    # This represents matrix multiplications where [A x B] * [B x C] would be A * B * C multiplications.
    p = [p[x].shape[0] for x in range(len(p))] + [p[len(p) - 1].shape[1]]

    # By the book code below
    n = len(p) - 1

    # Create the return matrices
    m = numpy.matrix([[0] * n] * n)
    s = numpy.matrix([[0] * n] * n)

    for l in range(1, n):
        for i in range(0, n - l):
            j = i + l
            m[i, j] = -1
            for k in range(i, j):
                # Add every permutation of (the total previous matrix *) + (the new matrix *)
                q = m[i, k] + m[k + 1, j] + p[i] * p[k + 1] * p[j + 1]

                # If this entry hasn't be set OR the total matrix * is less than the previous, set the new values
                if q < m[i, j] or m[i, j] == -1:
                    m[i, j] = q
                    s[i, j] = k

    return m, s
