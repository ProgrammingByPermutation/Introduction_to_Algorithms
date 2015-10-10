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


def merge_sort(collection, p, q, r):
    n1 = q - p
    n2 = r - q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    for i in range(n1):
        L[i] = collection[p + i]
    for j in range(n2):
        R[j] = collection[q + j]
    L[n1] = None
    R[n2] = None
    i = 0
    j = 0
    for k in range(p, r - 1):
        if L[i] <= R[j]:
            collection[k] = L[i]
            i = i + 1
        else:
            collection[k] = R[j]
            j = j + 1


if __name__ == "__main__":
    collection = [5, 2, 4, 6, 1, 3]
    insertion_sort(collection)
    assert (collection == [1, 2, 3, 4, 5, 6])

    collection = [2, 4, 5, 7, 1, 2, 3, 6]
    merge_sort(collection, 0, 4, 8)
    print(collection)
