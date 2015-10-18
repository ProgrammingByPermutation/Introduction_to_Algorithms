import random
import math
import enum


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
        if type(x) is not LinkedList.LinkedListNode:
            x = LinkedList.LinkedListNode(x)
        x.next_node = self.head
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
        if type(x) is not LinkedList.LinkedListNode:
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
        if type(x) is not LinkedListSentinel.LinkedListNode:
            x = self.list_search(x)

        x.prev_node.next_node = x.next_node
        x.next_node.prev_node = x.prev_node


class BinaryTreePointers:
    """
    Chapter 10: A representation of a tree using pointers. Each node has a pointer to a left child, a right child, and
    its parent.
    """

    class TreeNode:
        """
        A tree node. If the parent node is None the node is assumed to be the root node.
        """

        def __init__(self, key, p=None, left=None, right=None, satellite=None):
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
            self.satellite = satellite

        def __str__(self):
            return str(self.key)

    def __init__(self):
        self.root = None


class BinarySearchTree(BinaryTreePointers):
    """
    Chapter 12: A binary search tree satisfies the constraints that for every node x its left child will be less than
    or equal to it and its right child will be greater than or equal to it.
    """

    def __init__(self):
        BinaryTreePointers.__init__(self)
        self.root = None

    def inorder_tree_walk(self, x, function=lambda x: print(x.key)):
        """
        Chapter 12: Walks the binary tree in ascending order.
        :param x: The node to start the walk from.
        :param x: The node to walk from.
        :param function: The function to call for each node.
        """
        # Pre-conditions
        if x is None:
            return

        self.inorder_tree_walk(x.left)
        function(x.key)
        self.inorder_tree_walk(x.right)

    def tree_search(self, x, k):
        """
        Chapter 12: Searches for a given key in the binary search tree.
        :param x: The node to search from.
        :param k: The key to search for.
        :return: The tree node with the given key.
        """
        if x is None or k == x.key:
            return x

        if k < x.key:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    def iterative_tree_search(self, x, k):
        """
        Chapter 12: Iteratively searches for the given key in a binary tree. Faster than tree_search.
        :param x: The node to search from.
        :param k: The key to search for.
        :return: The tree node with the given key.
        """
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right

        return x

    def tree_minimum(self, x):
        """
        Chapter 12: Finds the minimum key value in the tree.
        :param x: The node to search from.
        :return: The node with the minimum key value in the tree.
        """
        while x.left is not None:
            x = x.left

        return x

    def tree_maximum(self, x):
        """
        Chapter 12: Finds the maximum key value in the tree.
        :param x: The node to search from.
        :return: The node with the maxmimum key value in the tree.
        """
        while x.right is not None:
            x = x.right

        return x

    def tree_successor(self, x):
        """
        Chapter 12: Finds the successor of a given node.
        :param x: The node to find the successor of.
        """
        if x.right is not None:
            return self.tree_minimum(x.right)

        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p

        return y

    def tree_predecessor(self, x):
        """
        Chapter 12: Finds the predecessor of a given node.
        :param x: The node to find the predecessor of.
        """
        if x.left is not None:
            return self.tree_maximum(x.left)

        y = x.p
        while y is not None and x == y.left:
            x = y
            y = y.p

        return y

    def tree_insert(self, z):
        """
        Chapter 12: Inserts the given node into the tree.
        :param z: The node or value to add to the tree.
        """
        if type(z) is not BinaryTreePointers.TreeNode:
            z = BinaryTreePointers.TreeNode(z)

        z.left = None
        z.right = None

        y = None
        x = self.root

        # Find the correct place in the tree for the node given the rules for a binary tree.
        # Save off the parent
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        # Determine if the new node is the root of the tree otherwise set the parent and link the two
        # nodes together.
        z.p = y
        if y is None:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    def tree_delete(self, z):
        """
        Chapter 12: Removes a node from the tree. This is trickier than inserting. You'll be in one of three situations that will
        be handled accordingly:
        1. z has no children: Just remove z by disconnecting it from the parent.
        2. z has one child: Splice out z by connecting its child to z's position in its parent.
        3. z has two children: Splice out its successor (y) which will have at most one child and then replace z's key
                               and satellite data with y's key and satellite data.
        :param z: The node to remove.
        :return: The removed node.
        """
        # Determine the node to splice out. y is either the node passed in or the successor of the node passed in.
        if z.left is None or z.right is None:
            y = z
        else:
            y = self.tree_successor(z)

        # Set x to the child of y if one exists.
        if y.left is not None:
            x = y.left
        else:
            x = y.right

        # Splice out node y
        if x is not None:
            x.p = y.p

        if y.p is None:
            self.root = x
        else:
            if y == y.p.left:
                y.p.left = x
            else:
                y.p.right = x

        # If y was the successor of z (i.e if z had two children when passed in) move y's data to z
        if y != z:
            # Copy all the data, not just the key
            z.key = y.key
            z.satellite = y.satellite

        return y


class RedBlackTree(BinaryTreePointers):
    """
    Chapter 13: A red black tree is a binary search tree that is balanced to guarantee that basic operations take logarithmic time.
    A red black tree satisfies the following constraints:
    1. Every node is either red or black.
    2. The root is black.
    3. Every leaf is black.
    4. If a node is red, then both its children are black.
    5. For each node, all paths from the node to descendant leaves contain the same number of black nodes.
    """

    class Color(enum.Enum):
        """
        Chapter 13: The color of the nodes.
        1. Red nodes have two black children.
        2. Black nodes are everything else.
        """
        red = 1
        black = 2

    class RedBlackNode(BinaryTreePointers.TreeNode):
        """
        Chapter 13: Like a binary tree node except it includes color.
        """

        def __init__(self, key):
            RedBlackTree.TreeNode.__init__(self, key)
            self.color = None

    def __init__(self):
        BinaryTreePointers.__init__(self)
        self.sentinel = RedBlackTree.RedBlackNode(None)
        self.sentinel.color = RedBlackTree.Color.black
        self.root = self.sentinel

    def black_height(self, x):
        """
        Chapter 13: The number of black nodes on the path of but not including x.
        :param x: The node to measure from.
        :return: The number of black nodes on the path.
        """
        i = 0
        node = x.p
        while node != self.sentinel:
            if node.color == RedBlackTree.Color.black:
                i += 1

        return i

    def left_rotate(self, x):
        """
        Chapter 13: Performs a left rotation on the passed in node. Left rotations assume that the right child (y) is not the
        sentinel value. A left rotation pivots the around the link from x to y. It makes y the new root of the
        subtree, with x as y's left and y's left child as x's right child.
        :param x: The node to rotate.
        """
        # Set y
        y = x.right

        # Turn y's left subtree into x's right subtree
        x.right = y.left

        if y.left != self.sentinel:
            y.left.p = x

        # Link x's parent to y
        y.p = x.p
        if x.p == self.sentinel:
            self.root = y
        else:
            if x == x.p.left:
                x.p.left = y
            else:
                x.p.right = y

        # Put x on y's left
        y.left = x
        x.p = y

    def right_rotate(self, x):
        """
        Chapter 13: Performs a right rotation on the passed in node. Left rotations assume that the left child (y) is
        not the sentinel value. A right rotation pivots the around the link from x to y. It makes y the new root of the
        subtree, with x as y's right and y's right child as x's left child.
        :param x: The node to rotate.
        """
        # Set y
        y = x.left

        # Turn y's left subtree into x's right subtree
        x.left = y.right

        if y.right != self.sentinel:
            y.right.p = x

        # Link x's parent to y
        y.p = x.p
        if x.p == self.sentinel:
            self.root = y
        else:
            if x == x.p.right:
                x.p.right = y
            else:
                x.p.left = y

        # Put x on y's left
        y.right = x
        x.p = y

    def rb_insert(self, z):
        """
        Chapter 13: Inserts into the red black tree.
        :param z: The node or key to insert.
        """
        if type(z) is not RedBlackTree.TreeNode:
            z = RedBlackTree.TreeNode(z)

        y = self.sentinel
        x = self.root

        while x != self.sentinel:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y == self.sentinel:
            self.root = z
        else:
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

        z.left = self.sentinel
        z.right = self.sentinel
        z.color = RedBlackTree.Color.red
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z):
        """
        Chapter 13: Fixes the balanced tree after an insert operation.
        :param z: The inserted node.
        """
        while z.p.color == RedBlackTree.Color.red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == RedBlackTree.Color.red:
                    z.p.color = RedBlackTree.Color.black
                    y.color = RedBlackTree.Color.black
                    z.p.p.color = RedBlackTree.Color.red
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = RedBlackTree.Color.black
                    z.p.p.color = RedBlackTree.Color.red
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == RedBlackTree.Color.red:
                    z.p.color = RedBlackTree.Color.black
                    y.color = RedBlackTree.Color.black
                    z.p.p.color = RedBlackTree.Color.red
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = RedBlackTree.Color.black
                    z.p.p.color = RedBlackTree.Color.red
                    self.left_rotate(z.p.p)

        self.root.color = RedBlackTree.Color.black


class RootedTree:
    """
    Chapter 10: A tree with an unbounded number of child nodes. Nodes have a pointer to the parent, left child, and
    right sibling. This means that no node has a pointer to its right child. Instead the left child must be retrieved
    and its right sibling accessed. Right siblings do contain a reference to their parent.
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


class DirectAccessTable:
    """
    Chapter 11: A data structure that has very efficient searching capabilities when the number of keys is very small.
    """

    class Entry:
        """
        A entry in the table.
        """

        def __init__(self, key, satellite_data=None):
            self.key = key
            self.satellite_data = satellite_data

    def __init__(self, size):
        self.list = [None] * size

    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, value):
        self.list[key] = value

    def direct_address_search(self, k):
        """
        Chapter 11: Returns the passed in key directly from the collection.
        :param k: The key to return the value of.
        :return: The value at key.
        """
        return self[k]

    def direct_address_insert(self, x, satellite_data=None):
        """
        Chapter 11: Inserts an entry directly into the DirectAccessTable's collection.
        :param x: The key value to insert or the DirectAccessTable.Entry to add.
        :param satellite_data: The satellite data to include. Will not be used if x is DirectAccessTable.Entry.
        """
        if type(x) is not DirectAccessTable.Entry:
            x = DirectAccessTable.Entry(x, satellite_data)

        self[x.key] = x

    def direct_access_delete(self, x):
        """
        Chapter 11: Removes an entry from the DirectAccessTable.
        :param x: The key value or the DirectAccessTable.Entry to remove.
        """
        if type(x) is not DirectAccessTable.Entry:
            x = DirectAccessTable.Entry(x)

        self[x.key] = None


class HashTable:
    """
    Chapter 11: A data structure optimized for searching. Works by passing entries through a hash function that converts search
    data into the index of the table of values.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the hash table class.
        :param size: The size of the hash table to create.
        :param hash_function: The hash function to use. Should take arguments of "self" pointing to this object, "k"
                              representing the key to calculate the hash for, and optionally "i" if an open address
                              hash table is desired (i.e if calls will be made to the open address hash functions).
        """
        self.hash_table = [None] * size
        self.A = 0.35459254522100925
        self.c1 = None
        self.c2 = None

        # Since open address hashing is the hardest to setup we'll example using that here.
        self.hash_function = lambda k, i: self.hash_double_hashing(k, i, self.hash_division, self.hash_multiplication)

    def hash_division(self, k):
        """
        Chapter 11: Hash division is accomplished by taking the remainder of a division operation. If hash division is used
        the size of the collection should not be a power of 2. The reason being that if hash_table size equals 2^P then
        hash_division(k) will equal the lower p bits of k. Unless the keys passed in have an equally distributed pattern
        of lower p bits this will result in many collisions. Prime numbers that are not close to a power of 2 tend
        to be good sizes for this hashing algorithm.
        :param k: The key to computer the hash of.
        :return: The hash value.
        """
        return k % len(self.hash_table)

    def hash_multiplication(self, k):
        """
        Chapter 11: Hash multiplication is accomplished by plugging the key into a mathematical equation. This has the advantage of
        not placing enough emphasis on the size of the hash table.
        :param k: The key to hash.
        :return: The hash value.
        """
        if self.A is None:
            # A should be between 0 and 1, value made up.
            self.A = random.random()

        return math.floor(len(self.hash_table) * ((k * self.A) % 1))

    def hash_linear_probing(self, k, i, hash_function):
        """
        Performs linear probing for a hash. Linear probing is a technique for dealing with collisions open addressing.
        It allows us to specify an arbitrary hashing function and offset its value linearly by an index. Basically we
        take the hash provided by the passed in algorithm, add the index to its output, and then subsequently wrap the
        output by the length of the hash_table. The main issue with this approach is "primary clustering" where
        collision resolutions cause blocks of data to form which causes search times to increase.
        :param k: The key to probe for.
        :param i: The offset index.
        :param hash_function: The hash function.
        :return: The hash value.
        """
        return (hash_function(k) + i) % len(self.hash_table)

    def hash_quadratic_probing(self, k, i, hash_function):
        """
        Chapter 11: Performs quadratic probing for a hash. Quadratic probing is a technique for dealing with collisions open
        addressing. It allows us to specify an arbitrary hashing function and offset its value quadratically based off
        of an index. Basically we take the hash provided by the passed in algorithm, give it a quadratic offset, and
        then subsequently wrap the output by the length of the hash_table. The main issue with this approach is
        "secondary clustering" where collision resolutions follow the same chain of values. When the hash table is more
        than half full it can result in preventing an insert. Following the logic of a quadratic insert, no chains can
        exceed (hash_table length / 2).
        :param k: The key to probe for.
        :param i: The offset index.
        :param hash_function: The hash function.
        :return: The hash value.
        """
        if self.c1 is None:
            # A should greater than 0, value made up.
            self.c1 = random.randint(1, len(self.hash_table))

        if self.c2 is None:
            # A should greater than 0, value made up.
            self.c2 = random.randint(1, len(self.hash_table))

        return (hash_function(k) + (self.c1 * i) + (self.c2 * (i ** 2))) % len(self.hash_table)

    def hash_double_hashing(self, k, i, hash_function1, hash_function2):
        """
        Chapter 11: Implements double hashing. Double hashing uses two hash functions that should be complementary. Ideally,
        hash_function1 should be relatively prime for all values of k and hash_function2 should both not share many
        hash values with hash_function1 and not hash to zero.
        :param k: The key to probe for.
        :param i: The offset index.
        :param hash_function1: The first hash function.
        :param hash_function2: The second hash function.
        :return: The hash value.
        """
        return (hash_function1(k) + (i * hash_function2(k))) % len(self.hash_table)

    def chained_hash_insert(self, x):
        """
        Chapter 11: Inserts a value into the linked list at a given hash table location.
        :param x: The value to insert into the hash table.
        """
        if type(x) is not LinkedList.LinkedListNode:
            x = LinkedList.LinkedListNode(x)

        hash = self.hash_function(x.key)
        linked_list = self.hash_table[hash]
        if type(linked_list) is not LinkedList:
            curr_value = linked_list
            linked_list = LinkedList()
            linked_list.list_insert(curr_value)
            self.hash_table[hash] = linked_list

        linked_list.list_insert(x)

    def chained_hash_search(self, k):
        """
        Chapter 11: Finds a value in the linked list at a given hash table location.
        :param k: The key to look up.
        :return: The element at the provided key location.
        """
        linked_list = self.hash_table[self.hash_function(k)]
        return linked_list.list_search(k)

    def chained_hash_delete(self, x):
        """
        Chapter 11: Removes a value from the linked list at a given hash table location.
        :param x: The value to remove from the hash table.
        """
        linked_list = self.hash_table[self.hash_function(x.key)]
        linked_list.list_delete(x)

    def hash_chained_insert(self, k):
        """
        Chapter 11: Inserts a key into the hash table using chained collisions. It's guaranteed to handle collisions by
        creating linked lists in the hash table entries with collisions. This uses more memory in the event of a
        collision and causes increased search time for collided table entries but it also guarantees the insertion
        of keys.
        :param k: The key to insert.
        :return: The hash of the new element.
        """
        j = self.hash_function(k)
        if self.hash_table[j] is None:
            self.hash_table[j] = k
            return j
        else:
            k = LinkedList.LinkedListNode(k)
            self.chained_hash_insert(k)
            return j

    def hash_chained_search(self, k):
        """
        Chapter 11: Searches for the given key in the hash table.
        :param k: The key to search for.
        :return: The hash of the found key in the table. None if not found.
        """
        j = self.hash_function(k)
        if type(self.hash_table[j]) is LinkedList:
            node = self.hash_table[j].head
            while node is not None:
                if node.key == k:
                    return j
                node = node.next_node
            return None
        elif self.hash_table[j] == k:
            return j

        return None

    def hash_insert(self, k):
        """
        Chapter 11: Inserts a key into the hash table using open addressing. The principle of open addressing is simple. We simply
        calculate a hash code using the key and an index. This ensures that if we get a collision we can simply
        increment the index to find the next available location for the key. This algorithm works best when keys will
        not be deleted from the hash table. It has the advantage of being faster and using less memory.
        :param k: The key to insert.
        :return: The hash of the new element.
        """
        i = 0
        while True:
            j = self.hash_function(k, i)
            if self.hash_table[j] is None:
                self.hash_table[j] = k
                return j
            else:
                i += 1

            if i == len(self.hash_table):
                break

        raise Exception("hash table overflow")

    def hash_search(self, k):
        """
        Chapter 11: Searches for the given key in the hash table.
        :param k: The key to search for.
        :return: The hash of the found key in the table. None if not found.
        """
        i = 0
        while True:
            j = self.hash_function(k, i)
            if self.hash_table[j] == k:
                return j

            i = i + 1

            if self.hash_table[j] is None or i == len(self.hash_table):
                break

        return None
