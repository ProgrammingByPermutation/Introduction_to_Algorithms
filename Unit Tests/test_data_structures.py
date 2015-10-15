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

        print(list)
        # node = list.head
        # for x in [1,2,3,4]:
        #     self.assertEquals(node.key, x, "Insert failed.")
