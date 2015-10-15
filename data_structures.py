class OneBasedList:
    """
    A list that uses a one-based index. This is how the book's arrays work. Useful for debugging when converting to a
    zero-based index.
    """

    def __init__(self, collection, auto_append=False):
        """
        Initializes a new instance of the OneBasedList class.
        :param collection: The initial collection to wrapper.
        :param auto_append: True if calls to __setitem__ should increase the collection's size when the index is
                            one index greater than the length of the one based collection, false otherwise.
        """
        if collection is not None:
            self.list = list(collection)
        else:
            self.list = []
        self.auto_append = auto_append

    def __getitem__(self, item):
        if item < 1:
            raise Exception("Index out of range: " + item)
        elif item > len(self.list):
            raise Exception("Index out of range: " + item)

        return self.list[item - 1]

    def __setitem__(self, key, value):
        key = key - 1
        if key < 0:
            raise Exception("Index out of range: " + value)
        elif key == len(self.list):
            if self.auto_append and key == len(self.list):
                self.list.append(value)
                return
            else:
                raise Exception("Index out of range: " + str(value))

        self.list[key] = value

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)


class Stack(OneBasedList):
    """
    Chapter 10: A LIFO stack. Grows dynamically if the initial collection is not large enough to hold a push.
    """

    def __init__(self, collection=None):
        OneBasedList.__init__(self, collection, True)
        self.top = len(self.list)

    def stack_empty(self):
        """
        Chapter 10: Determines if the stack is currently empty.
        :return: True if empty, false otherwise.
        """
        if self.top == 0:
            return True
        return False

    def push(self, x):
        """
        Chapter 10: Adds a value to the top of the stack.
        :param x: The new value to add.
        """
        self.top = self.top + 1
        self[self.top] = x

    def pop(self):
        """
        Chapter 10: Removes the element from the top of the stack.
        :return: The element at the top of the collection.
        """
        if self.stack_empty():
            raise Exception("underflow: Stack empty")
        else:
            self.top = self.top - 1
            return self[self.top + 1]


class Queue(OneBasedList):
    """
    Chapter 10: A FIFO queue. Does not resize to accommodate enqueues that exceed the collection's size.
    """

    def __init__(self, collection):
        OneBasedList.__init__(self, collection, False)
        self.head = 1
        self.tail = len(self) + 1

    def enqueue(self, x):
        """
        Chapter 10: Adds a value to the end of the queue.
        :param x: The new value to add.
        """
        if self.head == self.tail + 1:
            raise Exception("overflow: Queue full.")

        self[self.tail] = x
        if self.tail == len(self):
            self.tail = 1
        else:
            self.tail = self.tail + 1

    def dequeue(self):
        """
        Chapter 10: Removes a element from the beginning of the queue.
        :return: The element at the beginning of the queue.
        """
        if self.head == self.tail:
            raise Exception("underflow: Queue empty.")

        x = self[self.head]
        if self.head == len(self):
            self.head = 1
        else:
            self.head = self.head + 1
        return x


class LinkedListNode:
    """
    Represents all of the values of a linked list node.
    """

    def __init__(self, key, prev_node=None, next_node=None):
        """
        Initializes a new instance of the linked list class.
        :param key: The value to store in the linked list node.
        :param prev_node: A reference to the previous element in the list.
        :param next_node: A reference to the next_node element in the list.
        """
        self.key = key
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self):
        return str(self.key)


class LinkedList:
    """
    Chapter 10: A linked list class.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        value = '['
        node = self.head
        if node is not None:
            while True:
                node_value = node.key

                if node.next_node is not None:
                    value += str(node_value) + ', '
                else:
                    value += str(node_value)
                    break

                node = node.next_node

        value += ']'
        return value

    def list_search(self, k):
        """
        Chapter 10: Searches for the first occurrence of the supplied key.
        :param k: The key to search for.
        :return: The node of the key if found, None otherwise.
        """
        x = self.head
        while x is not None and x.key != k:
            x = x.next_node
        return x

    def list_insert(self, x):
        """
        Chapter 10: Inserts the provided key into the head of the list.
        :param x: The key to insert into the collection.
        """
        new_node = LinkedListNode(x, next_node=self.head)
        if self.head is not None:
            self.head.prev_node = new_node
        self.head = new_node
        new_node.prev_node = None

    def list_delete(self, x):
        """
        Chapter 10: Removes the provided key from the collection.
        :param x: The key to remove.
        """
        # Not in the original code, just here for convenience.
        if x is not LinkedListNode:
            x = self.list_search(x)

        if x.prev_node is not None:
            x.prev_node.next_node = x.next_node
        else:
            self.head = x.next_node

        if x.next_node is not None:
            x.next_node.prev_node = x.prev_node
