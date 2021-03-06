from sorting import randomized_partition


def minimum(collection):
    """
    Chapter 9: Determines the minimum value in the collection.
    :param collection: The collection to find the minimum in.
    :return: The minimum value in the collection.
    """
    min = collection[0]
    for i in range(1, len(collection)):
        if min > collection[i]:
            min = collection[i]

    return min


def maximum(collection):
    """
    Chapter 9: Determines the maximum value in the collection.
    :param collection: The collection to find the maximum in.
    :return: The maximum value in the collection.
    """
    max = collection[0]
    for i in range(1, len(collection)):
        if max < collection[i]:
            max = collection[i]

    return max


def minimum_maximum(collection):
    """
    Chapter 9: A more efficient version of finding the minimum and maximum value of collection when both are desired.
    Throwing out the time savings achieved by avoiding a function call. This method both:
    1. Finds the minimum and maximum by looping over the collection only once.
    2. Determines the minimum and maximum using 3 comparison instead of 4.
    :param collection: The collection to find the minimum and maximum of.
    :return: A tuple where the first value is the minimum and the second in the maximum.
    """
    n = len(collection)

    # If the collection is even, compare the first two elements, the smaller is the starter min and the larger is the
    # started max.
    # If the collection is odd, set both elements to both the min and max value.
    if n % 2 == 0:
        if collection[0] < collection[1]:
            min = collection[0]
            max = collection[1]
        else:
            min = collection[1]
            max = collection[0]
        first_index = 2
    else:
        min = collection[0]
        max = collection[0]
        first_index = 1

    # Loop through the elements of the collection in pairs. First compare the pair to each other, this will tell us
    # which element we need to compare to the minimum and which we need to compare to the maximum. By using this
    # technique we're only performing 3 comparisons instead of 4.
    # Our way:
    # 1. Compare pair (i and i + 1)
    # 2. Compare min to smaller of pair
    # 3. Compare max to larger of pair
    #
    # Other way:
    # 1. Compare i to min
    # 2. Compare i to max
    # 3. Compare i + 1 to min
    # 4. Compare i + 1 to max
    for i in range(first_index, n, 2):
        if collection[i] < collection[i + 1]:
            if min > collection[i]:
                min = collection[i]

            if max < collection[i + 1]:
                max = collection[i + 1]
        else:
            if min > collection[i + 1]:
                min = collection[i + 1]

            if max < collection[i]:
                max = collection[i]

    return min, max


def randomized_select(collection, p, r, i):
    """
    Chapter 9: Performs a randomized select. The algorithm works much like the quicksort algorithm and has the side
    effect of having to sort the collection in place to accomplish the selection. The algorithm starts by partitioning
    the array into two sub-arrays and a pivot point. It then sorts the sub-arrays so that everything less than the
    pivot point is on the left and anything larger is on the right. Next, the algorithm counts the number of elements
    in the left side array plus 1 for the pivot point. If at this point if the count and i are the same we've found
    the i-th smallest value. Otherwise we recurse down the left or right side array until they are.
    :param collection: The collection to select from.
    :param p: The starting index of the search.
    :param r: The ending index of the search.
    :param i: The i-th smallest element in the array to find. i = 1 is the minimum and i = len(collection) is the
              maximum.
    :return: The value of the i-th smallest element in the array.
    """
    # If there is only one thing in the collection it is the i-th value. Surely no one would pass us a i value that
    # is larger than their entire collection. That would be cruel!
    if p == r:
        return collection[p]

    # Randomly split the array into a right and left side and sort them such that less than or equal to values are on
    # the left side and greater than values are on the right.
    q = randomized_partition(collection, p, r)

    # Find the pivot index
    k = q - p + 1

    # If the i-th value we're looking for = k then the pivot values is the i-th value. We know this because the
    # collection is sorted as such.
    #
    # Otherwise, recurse down the path of the left or right array to find the i-th value.
    if i == k:
        return collection[q]
    elif i < k:
        return randomized_select(collection, p, q - 1, i)
    else:
        return randomized_select(collection, q + 1, r, i - k)
