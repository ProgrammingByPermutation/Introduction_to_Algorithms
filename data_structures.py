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


class LinkedList:
    """
    Chapter 10: A linked list class.
    """

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

    def __len__(self):
        i = 0
        node = self.head
        while node is not None:
            i += 1
            node = node.next_node

        return i

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
        x = LinkedList.LinkedListNode(x, next_node=self.head)
        if self.head is not None:
            self.head.prev_node = x
        self.head = x
        x.prev_node = None

    def list_delete(self, x):
        """
        Chapter 10: Removes the provided key from the collection.
        :param x: The key to remove.
        """
        # Not in the original code, just here for convenience.
        if x is not LinkedList.LinkedListNode:
            x = self.list_search(x)

        if x.prev_node is not None:
            x.prev_node.next_node = x.next_node
        else:
            self.head = x.next_node

        if x.next_node is not None:
            x.next_node.prev_node = x.prev_node


class LinkedListSentinel:
    """
    Chapter 10: A linked list class that uses sentinels. A sentinel is a dummy value that allows us to avoid some
    complexity when performing operations by avoiding boundary conditions. A sentinel value can also reduce running time
    when a significant amount of time is spent checking boundary conditions in loops. The sentinel while empty and
    meaningless contains all of the methods of a valid value being understood to be the end of the list. A sentinel
    should not be used when there are a large number of small lists since the sentinel wastes memory.
    """

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

    def __init__(self):
        self.sentinel = LinkedListSentinel.LinkedListNode(None)
        self.sentinel.next_node = self.sentinel
        self.sentinel.prev_node = self.sentinel

    def __str__(self):
        value = '['
        node = self.sentinel.next_node
        if node != self.sentinel:
            while True:
                node_value = node.key

                if node.next_node != self.sentinel:
                    value += str(node_value) + ', '
                else:
                    value += str(node_value)
                    break

                node = node.next_node

        value += ']'
        return value

    def __len__(self):
        i = 0
        node = self.sentinel.next_node
        while node != self.sentinel:
            i += 1
            node = node.next_node

        return i

    def list_search(self, k):
        """
        Chapter 10: Searches for the first occurrence of the supplied key.
        :param k: The key to search for.
        :return: The node of the key if found, None otherwise.
        """
        x = self.sentinel.next_node
        while x != self.sentinel and x.key != k:
            x = x.next_node
        return x

    def list_insert(self, x):
        """
        Chapter 10: Inserts the provided key into the head of the list.
        :param x: The key to insert into the collection.
        """
        x = LinkedListSentinel.LinkedListNode(x, next_node=self.sentinel.next_node)
        self.sentinel.next_node.prev_node = x
        self.sentinel.next_node = x
        x.prev_node = self.sentinel

    def list_delete(self, x):
        """
        Chapter 10: Removes the provided key from the collection.
        :param x: The key to remove.
        """
        # Not in the original code, just here for convenience.
        if x is not LinkedListSentinel.LinkedListNode:
            x = self.list_search(x)

        x.prev_node.next_node = x.next_node
        x.next_node.prev_node = x.prev_node


class BinaryTreePointers:
    """
    Chapter 10: A representation of a tree using pointers. Each node has a pointer to a left child, a right child, and its parent.
    """

    class TreeNode:
        """
        A tree node. If the parent node is None the node is assumed to be the root node.
        """

        def __init__(self, key, p=None, left=None, right=None):
            """
            Initializes a new instance of the TreeNode class.
            :param key: The key value of the node.
            :param p: The parent node.
            :param left: The left child node.
            :param right: The right child node.
            """
            self.p = p
            self.left = left
            self.right = right
            self.key = key

    def __init__(self):
        self.root = None


class RootedTree:
    """
    Chapter 10: A tree with an unbounded number of child nodes. Nodes have a pointer to the parent, left child, and right sibling.
    This means that no node has a pointer to its right child. Instead the left child must be retrieved and its right
    sibling accessed. Right siblings do contain a reference to their parent.
    """

    class TreeNode:
        def __init__(self, key, p=None, left_child=None, right_sibling=None):
            """
            Initializes a new instance of the TreeNode class.
            :param key: The key value of the node.
            :param p: The parent node.
            :param left_child: The left child node.
            :param right_sibling: The right sibling node at the same level of the tree.
            """
            self.key = key
            self.p = p
            self.left_child = left_child
            self.right_sibling = right_sibling

    def __init__(self):
        self.root = None
