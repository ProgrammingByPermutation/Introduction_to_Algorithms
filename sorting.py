import math


def insertion_sort(collection):
    """
    Chapter 2: Sorts the provided collection using an insertion sort. Runtime: n^2
    :param collection: A collection that can be indexed. Will be modified in place.
    """
    for j in range(1, len(collection)):
        key = collection[j]

        # Insert the key into the sorted sequence collection[1..j-1]
        i = j - 1
        while i >= 0 and collection[i] > key:
            collection[i + 1] = collection[i]
            i = i - 1
        collection[i + 1] = key


def merge_sort(collection, p=None, r=None):
    """
    Chapter 2: Merge sort. Runtime: n log n.
    :param collection: The collection to sort.
    :param p: The starting index.
    :param r: The ending index.
    """

    def merge(collection, p, q, r):
        """
        Merges two sorted portions of a collection in place.
        :param collection: The collection to sort.
        :param p: The first index first array.
        :param q: The last index of the first array.
        :param r: The last index of the second array.
        """
        n1 = q - p + 1
        n2 = r - q
        left_array = [None] * (n1 + 1)
        right_array = [None] * (n2 + 1)
        for i in range(n1):
            left_array[i] = collection[p + i]
        for j in range(n2):
            right_array[j] = collection[q + j + 1]
        left_array[n1] = None  # Dummy value that means this value is larger than any possible value
        right_array[n2] = None  # Dummy value that means this value is larger than any possible value
        i = 0
        j = 0
        for k in range(p, r + 1):
            # If the right array is automatically larger
            # OR
            # If the left array is not automatically larger AND the actual left value is less than or equal to the
            # actual right value
            if right_array[j] is None or (left_array[i] is not None and left_array[i] <= right_array[j]):
                collection[k] = left_array[i]
                i = i + 1
            else:
                collection[k] = right_array[j]
                j = j + 1

    if p == None and r == None:
        p = 0
        r = len(collection) - 1

    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(collection, p, q)
        merge_sort(collection, q + 1, r)
        merge(collection, p, q, r)


def bubble_sort(collection):
    """
    Chapter 2: Bubble Sort. Runtime: Laughable
    :param collection: The collection to sort in place.
    """
    for i in range(len(collection)):
        for j in range(len(collection) - 1, i, -1):
            if collection[j] < collection[j - 1]:
                collection[j], collection[j - 1] = collection[j - 1], collection[j]


if __name__ == "__main__":
    collection = [5, 2, 4, 6, 1, 3]
    insertion_sort(collection)
    assert collection == [1, 2, 3, 4, 5, 6]

    collection = [5, 2, 4, 7, 1, 3, 2, 6]
    merge_sort(collection)
    assert collection == [1, 2, 2, 3, 4, 5, 6, 7]

    collection = [5, 2, 4, 7, 1, 3, 2, 6]
    bubble_sort(collection)
    assert collection == [1, 2, 2, 3, 4, 5, 6, 7]
