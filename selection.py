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
