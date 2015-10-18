from unittest import TestCase

from data_structures import *


class TestOneBasedList(TestCase):
    def test_indexes(self):
        one_based = OneBasedList(range(10))
        regular = range(10)

        # Make sure everything is one off
        for i in range(1, 11):
            self.assertEquals(one_based[i], regular[i - 1])


class TestStack(TestCase):
    def test_stack_empty(self):
        stack = Stack([])
        self.assertEquals(stack.stack_empty(), True, "Stack not reporting empty.")

        stack = Stack([1, 2, 3])
        self.assertEquals(stack.stack_empty(), False, "Stack reporting empty when populated.")

    def test_push(self):
        stack = Stack([1, 2, 3])
        stack.push(4)

        for x in range(3, -1, -1):
            self.assertEquals(stack.pop(), x + 1, "Value not pushed onto stack.")
        self.assertEquals(stack.stack_empty(), True, "Stack not reporting empty.")

    def test_pop(self):
        stack = Stack([1, 2, 3])

        for x in range(2, -1, -1):
            self.assertEqual(stack.pop(), x + 1, "Value not popping off stack.")
        self.assertEquals(stack.stack_empty(), True, "Stack not reporting empty.")


class TestQueue(TestCase):
    def test_enqueue(self):
        queue = Queue([None] * 12)
        queue[7] = 15
        queue[8] = 6
        queue[9] = 9
        queue[10] = 8
        queue[11] = 4
        queue.head = 7
        queue.tail = 12

        queue.enqueue(17)
        queue.enqueue(3)
        queue.enqueue(5)

        for x in [15, 6, 9, 8, 4, 17, 3, 5]:
            self.assertEquals(queue.dequeue(), x, "Enqueue operation unsuccessful.")

    def test_dequeue(self):
        queue = Queue(range(0, 10))

        for i in range(0, 10):
            self.assertEqual(queue.dequeue(), i, "Dequeue operation unsuccessful.")


class TestLinkedList(TestCase):
    def test_insert(self):
        list = LinkedList()
        list.list_insert(1)
        list.list_insert(2)
        list.list_insert(3)
        list.list_insert(4)

        node = list.head
        for x in range(4, 0, -1):
            self.assertEquals(node.key, x, "Insert failed.")
            node = node.next_node

    def test_search(self):
        list = LinkedList()
        list.list_insert(1)
        list.list_insert(2)
        list.list_insert(3)
        list.list_insert(4)

        for x in range(4, 0, -1):
            self.assertEquals(list.list_search(x).key, x, "Search failed.")

    def test_delete(self):
        list = LinkedList()
        list.list_insert(1)
        list.list_insert(2)
        list.list_insert(3)
        list.list_insert(4)

        for x in range(4, 0, -1):
            list.list_delete(x)

            node = list.head
            for i in range(x - 1, 0, -1):
                self.assertEquals(node.key, i, "Delete failed.")
                node = node.next_node

        self.assertEqual(len(list), 0, "List not empty.")


class TestLinkedListSentinel(TestCase):
    def test_insert(self):
        list = LinkedListSentinel()
        list.list_insert(1)
        list.list_insert(2)
        list.list_insert(3)
        list.list_insert(4)

        node = list.sentinel.next_node
        for x in range(4, 0, -1):
            self.assertEquals(node.key, x, "Insert failed.")
            node = node.next_node

    def test_search(self):
        list = LinkedListSentinel()
        list.list_insert(1)
        list.list_insert(2)
        list.list_insert(3)
        list.list_insert(4)

        for x in range(4, 0, -1):
            self.assertEquals(list.list_search(x).key, x, "Search failed.")

    def test_delete(self):
        list = LinkedListSentinel()
        list.list_insert(1)
        list.list_insert(2)
        list.list_insert(3)
        list.list_insert(4)

        for x in range(4, 0, -1):
            list.list_delete(x)

            node = list.sentinel.next_node
            for i in range(x - 1, 0, -1):
                self.assertEquals(node.key, i, "Delete failed.")
                node = node.next_node

        self.assertEqual(len(list), 0, "List not empty.")


class TestHashTable(TestCase):
    def test_hash_function_open_address_double_hash(self):
        hash_table = HashTable(10)

        answers = [None] * 10
        for x in range(10, 20):
            answers[x - 10] = hash_table.hash_insert(x)

        for x in range(10, 20):
            self.assertEqual(hash_table.hash_search(x), answers[x - 10])

    def test_hash_function_chained_multiplication(self):
        hash_table = HashTable(10)
        hash_table.hash_function = hash_table.hash_multiplication

        answers = [None] * 10
        for x in range(1, 10):
            answers[x] = hash_table.hash_chained_insert(x)

        for x in range(1, 10):
            self.assertEqual(hash_table.hash_chained_search(x), answers[x])

    def test_hash_function_chained_division(self):
        hash_table = HashTable(10)
        hash_table.hash_function = hash_table.hash_division

        answers = [None] * 10
        for x in range(10, 20):
            answers[x - 10] = hash_table.hash_chained_insert(x)

        for x in range(10, 20):
            self.assertEqual(hash_table.hash_chained_search(x), answers[x - 10])

    def test_hash_function_linear_probing(self):
        hash_table = HashTable(10)
        hash_table.hash_function = lambda k, i: hash_table.hash_linear_probing(k, i, hash_table.hash_multiplication)

        answers = [None] * 10
        for x in range(10, 20):
            answers[x - 10] = hash_table.hash_insert(x)

        for x in range(10, 20):
            self.assertEqual(hash_table.hash_search(x), answers[x - 10])

    def test_hash_function_quadratic_probing(self):
        # Quadratics are known to be unable to resolve collisions if more than half full, have to use 3x larger
        # collection for a fair test.
        hash_table = HashTable(30)
        hash_table.hash_function = lambda k, i: hash_table.hash_quadratic_probing(k, i, hash_table.hash_multiplication)

        answers = [None] * 10
        for x in range(10, 20):
            answers[x - 10] = hash_table.hash_insert(x)

        for x in range(10, 20):
            self.assertEqual(hash_table.hash_search(x), answers[x - 10])


class TestBinarySearchTree(TestCase):
    def test_insert(self):
        tree = BinarySearchTree()
        tree.root = BinarySearchTree.TreeNode(12)
        tree.root.left = BinarySearchTree.TreeNode(5)
        tree.root.left.p = tree.root
        tree.root.left.left = BinarySearchTree.TreeNode(2)
        tree.root.left.left.p = tree.root.left
        tree.root.left.right = BinarySearchTree.TreeNode(9)
        tree.root.left.right.p = tree.root.left
        tree.root.right = BinarySearchTree.TreeNode(18)
        tree.root.right.p = tree.root
        tree.root.right.left = BinarySearchTree.TreeNode(15)
        tree.root.right.left.p = tree.root.right
        tree.root.right.right = BinarySearchTree.TreeNode(19)
        tree.root.right.right.p = tree.root.right
        tree.root.right.left.right = BinarySearchTree.TreeNode(17)
        tree.root.right.left.right.p = tree.root.right.left

        tree.tree_insert(13)

        self.assertEqual(tree.root.right.left.left.key, 13)
        self.assertEqual(tree.root.right.left.left.p, tree.root.right.left)
        self.assertEqual(tree.root.right.left.left.right, None)
        self.assertEqual(tree.root.right.left.left.left, None)

    def test_delete(self):
        tree = BinarySearchTree()
        tree.tree_insert(15)
        tree.tree_insert(5)
        tree.tree_insert(3)
        tree.tree_insert(12)
        tree.tree_insert(10)
        tree.tree_insert(13)
        tree.tree_insert(6)
        tree.tree_insert(7)
        tree.tree_insert(16)
        tree.tree_insert(20)
        tree.tree_insert(18)
        tree.tree_insert(23)

        # Did we set it up correctly?
        self.assertEqual(tree.root.left.right.right.key, 13)

        # Does deleting a node with no children work?
        tree.tree_delete(tree.root.left.right.right)
        self.assertEqual(tree.root.left.right.right, None)

        tree = BinarySearchTree()
        tree.tree_insert(15)
        tree.tree_insert(5)
        tree.tree_insert(3)
        tree.tree_insert(12)
        tree.tree_insert(10)
        tree.tree_insert(13)
        tree.tree_insert(6)
        tree.tree_insert(7)
        tree.tree_insert(16)
        tree.tree_insert(20)
        tree.tree_insert(18)
        tree.tree_insert(23)

        # Did we set it up correctly?
        self.assertEqual(tree.root.right.key, 16)

        # Does deleting a node with one child work?
        tree.tree_delete(tree.root.right)
        self.assertEqual(tree.root.right.key, 20)

        tree = BinarySearchTree()
        tree.tree_insert(15)
        tree.tree_insert(5)
        tree.tree_insert(3)
        tree.tree_insert(12)
        tree.tree_insert(10)
        tree.tree_insert(13)
        tree.tree_insert(6)
        tree.tree_insert(7)
        tree.tree_insert(16)
        tree.tree_insert(20)
        tree.tree_insert(18)
        tree.tree_insert(23)

        # Did we set it up correctly?
        self.assertEqual(tree.root.left.key, 5)

        # Does deleting a node with two children work?
        tree.tree_delete(tree.root.left)
        self.assertEqual(tree.root.left.key, 6)
        self.assertEqual(tree.root.left.right.left.left.key, 7)


class TestRedBlackTree(TestCase):
    @staticmethod
    def set_parents_and_sentinel(x, tree):
        """
        Lazy method for setting the parents and sentinel values for manually constructed trees
        :param x: The node to start traversing.
        :param tree: The tree.
        """
        if x.left != None:
            x.left.p = x
            TestRedBlackTree.set_parents_and_sentinel(x.left, tree)
        else:
            x.left = tree.sentinel

        if x.right != None:
            x.right.p = x
            TestRedBlackTree.set_parents_and_sentinel(x.right, tree)
        else:
            x.right = tree.sentinel

    def test_rotate(self):
        tree = RedBlackTree()
        tree.root = RedBlackTree.RedBlackNode(7)
        tree.root.p = tree.sentinel
        tree.root.left = RedBlackTree.RedBlackNode(4)
        tree.root.left.left = RedBlackTree.RedBlackNode(3)
        tree.root.left.right = RedBlackTree.RedBlackNode(6)
        tree.root.left.left.left = RedBlackTree.RedBlackNode(2)
        tree.root.right = RedBlackTree.RedBlackNode(11)
        tree.root.right.left = RedBlackTree.RedBlackNode(9)
        tree.root.right.right = RedBlackTree.RedBlackNode(18)
        tree.root.right.right.left = RedBlackTree.RedBlackNode(14)
        tree.root.right.right.left.left = RedBlackTree.RedBlackNode(12)
        tree.root.right.right.left.right = RedBlackTree.RedBlackNode(17)
        tree.root.right.right.right = RedBlackTree.RedBlackNode(19)
        tree.root.right.right.right.right = RedBlackTree.RedBlackNode(22)
        tree.root.right.right.right.left = RedBlackTree.RedBlackNode(20)

        # Lazy
        TestRedBlackTree.set_parents_and_sentinel(tree.root, tree)

        # Rotate
        tree.left_rotate(tree.root.right)

        # Check
        self.assertEqual(tree.root.right.key, 18)
        self.assertEqual(tree.root.right.right.key, 19)
        self.assertEqual(tree.root.right.left.key, 11)
        self.assertEqual(tree.root.right.left.left.key, 9)
        self.assertEqual(tree.root.right.left.right.key, 14)
        self.assertEqual(tree.root.right.left.right.left.key, 12)
        self.assertEqual(tree.root.right.left.right.right.key, 17)

        # Rotate back
        tree.right_rotate(tree.root.right)

        self.assertEqual(tree.root.right.key, 11)
        self.assertEqual(tree.root.right.left.key, 9)
        self.assertEqual(tree.root.right.right.key, 18)
        self.assertEqual(tree.root.right.right.right.key, 19)
        self.assertEqual(tree.root.right.right.left.key, 14)
        self.assertEqual(tree.root.right.right.left.left.key, 12)
        self.assertEqual(tree.root.right.right.left.right.key, 17)

    def test_insert(self):
        tree = RedBlackTree()
        tree.root = RedBlackTree.TreeNode(11)
        tree.root.p = tree.sentinel
        tree.root.color = RedBlackTree.Color.black
        tree.root.left = RedBlackTree.TreeNode(2)
        tree.root.left.color = RedBlackTree.Color.red
        tree.root.left.left = RedBlackTree.TreeNode(1)
        tree.root.left.left.color = RedBlackTree.Color.black
        tree.root.left.right = RedBlackTree.TreeNode(7)
        tree.root.left.right.color = RedBlackTree.Color.black
        tree.root.left.right.left = RedBlackTree.TreeNode(5)
        tree.root.left.right.left.color = RedBlackTree.Color.red
        tree.root.left.right.right = RedBlackTree.TreeNode(8)
        tree.root.left.right.right.color = RedBlackTree.Color.red
        tree.root.right = RedBlackTree.TreeNode(14)
        tree.root.right.color = RedBlackTree.Color.black
        tree.root.right.right = RedBlackTree.TreeNode(15)
        tree.root.right.right.color = RedBlackTree.Color.red

        TestRedBlackTree.set_parents_and_sentinel(tree.root, tree)

        # Insert
        tree.rb_insert(4)

        # Verify
        self.assertEqual(tree.root.key, 7)
        self.assertEqual(tree.root.left.key, 2)
        self.assertEqual(tree.root.left.left.key, 1)
        self.assertEqual(tree.root.left.right.key, 5)
        self.assertEqual(tree.root.left.right.left.key, 4)
        self.assertEqual(tree.root.right.key, 11)
        self.assertEqual(tree.root.right.left.key, 8)
        self.assertEqual(tree.root.right.right.key, 14)
        self.assertEqual(tree.root.right.right.right.key, 15)

        self.assertEqual(tree.root.left.left.left, tree.sentinel)
        self.assertEqual(tree.root.left.left.right, tree.sentinel)
        self.assertEqual(tree.root.left.right.right, tree.sentinel)
        self.assertEqual(tree.root.left.right.left.left, tree.sentinel)
        self.assertEqual(tree.root.left.right.left.right, tree.sentinel)
        self.assertEqual(tree.root.right.left.left, tree.sentinel)
        self.assertEqual(tree.root.right.left.right, tree.sentinel)
        self.assertEqual(tree.root.right.right.left, tree.sentinel)
        self.assertEqual(tree.root.right.right.right.left, tree.sentinel)
        self.assertEqual(tree.root.right.right.right.right, tree.sentinel)

        self.assertEqual(tree.root.color, RedBlackTree.Color.black)
        self.assertEqual(tree.root.left.color, RedBlackTree.Color.red)
        self.assertEqual(tree.root.left.left.color, RedBlackTree.Color.black)
        self.assertEqual(tree.root.left.right.color, RedBlackTree.Color.black)
        self.assertEqual(tree.root.left.right.left.color, RedBlackTree.Color.red)
        self.assertEqual(tree.root.right.color, RedBlackTree.Color.red)
        self.assertEqual(tree.root.right.left.color, RedBlackTree.Color.black)
        self.assertEqual(tree.root.right.right.color, RedBlackTree.Color.black)
        self.assertEqual(tree.root.right.right.right.color, RedBlackTree.Color.red)

    def test_remove(self):
        tree = RedBlackTree()
        tree.root = RedBlackTree.TreeNode(11)
        tree.root.p = tree.sentinel
        tree.root.color = RedBlackTree.Color.black
        tree.root.left = RedBlackTree.TreeNode(2)
        tree.root.left.color = RedBlackTree.Color.red
        tree.root.left.left = RedBlackTree.TreeNode(1)
        tree.root.left.left.color = RedBlackTree.Color.black
        tree.root.left.right = RedBlackTree.TreeNode(7)
        tree.root.left.right.color = RedBlackTree.Color.black
        tree.root.left.right.left = RedBlackTree.TreeNode(5)
        tree.root.left.right.left.color = RedBlackTree.Color.red
        tree.root.left.right.right = RedBlackTree.TreeNode(8)
        tree.root.left.right.right.color = RedBlackTree.Color.red
        tree.root.right = RedBlackTree.TreeNode(14)
        tree.root.right.color = RedBlackTree.Color.black
        tree.root.right.right = RedBlackTree.TreeNode(15)
        tree.root.right.right.color = RedBlackTree.Color.red

        TestRedBlackTree.set_parents_and_sentinel(tree.root, tree)

        tree.rb_delete(tree.root.left.right.left)

        self.assertEqual(tree.root.key, 11)
        self.assertEqual(tree.root.left.key, 2)
        self.assertEqual(tree.root.left.left.key, 1)
        self.assertEqual(tree.root.left.right.key, 7)
        self.assertEqual(tree.root.left.right.left, tree.sentinel)
        self.assertEqual(tree.root.left.right.right.key, 8)
        self.assertEqual(tree.root.right.key, 14)
        self.assertEqual(tree.root.right.right.key, 15)
