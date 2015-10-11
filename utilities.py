import random


class OneBasedList:
    """
    A list that uses a one-based index. This is how the book's arrays work. Useful for debugging when converting to a
    zero-based index.
    """

    def __init__(self, collection):
        if collection is not None:
            self.list = list(collection)
        else:
            self.list = []

    def __getitem__(self, item):
        if item < 1:
            raise Exception("Index out of range: " + item)
        elif item > len(self.list):
            raise Exception("Index out of range: " + item)

        return self.list[item - 1]

    def __setitem__(self, key, value):
        if key < 1:
            raise Exception("Index out of range: " + item)
        elif key > len(self.list):
            raise Exception("Index out of range: " + item)

        self.list[key - 1] = value

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)


def permute_by_sorting(collection):
    """
    Chapter 5: Randomly sorts the collection using a secondary list of random numbers for each index that is subsequently
    sorted.
    :param collection: The collection to randomly sort.
    :return: The randomly sorted collection.
    """
    n = len(collection)
    P = [[None, None]] * n

    # For each index, generate a random number.
    for i in range(n):
        P[i] = (random.uniform(0, n ** 3), collection[i])

    # Sort based on the random number in each position
    P = sorted(P, key=lambda tup: tup[0])

    # Return the randomly sorted collection
    return [item[1] for item in P]


def permute_without_identity(collection):
    """
    Chapter 5: Produces any permutation except the identity permutation in place.
    :param collection: The collection to permute in place.
    """
    n = len(collection)
    for i in range(n - 2):
        rnd = random.randint(i + 1, n - 1)
        collection[i], collection[rnd] = collection[rnd], collection[i]


def permute_with_all(collection):
    """
    Chapter 5: Produces a permutation using all values at all times.
    :param collection: The collection to permute in place.
    """
    n = len(collection)
    for i in range(n):
        rnd = random.randint(0, n - 1)
        collection[i], collection[rnd] = collection[rnd], collection[i]


def permute_by_cyclic(collection):
    """
    Chapter 5: Shifts the contents of the collection by a random index.
    :param collection: The collection to permute.
    :return: A new permuted collection.
    """
    n = len(collection)
    B = [None] * n
    offset = random.randint(0, n - 1)
    for i in range(n):
        dest = i + offset
        if dest >= n:
            dest = dest - n
        B[dest] = collection[i]
    return B


def randomize_in_place(collection):
    """
    Chapter 5: Randomizes the collection in place.
    :param collection: The collection to randomize in place.
    """
    n = len(collection)
    for i in range(n):
        rnd = random.randint(i, n - 1)
        collection[i], collection[rnd] = collection[rnd], collection[i]
