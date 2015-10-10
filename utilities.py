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
        return self.list[item - 1]

    def __setitem__(self, key, value):
        self.list[key - 1] = value

    def __str__(self):
        return str(self.list)
