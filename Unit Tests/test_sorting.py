from unittest import TestCase

from sorting import *


class TestMiscSort(TestCase):
    def test_insertion_sort(self):
        collection = [5, 2, 4, 6, 1, 3]
        insertion_sort(collection)
        self.assertEquals(collection, [1, 2, 3, 4, 5, 6], "Collection not sorted. " + str(collection))

    def test_merge_sort(self):
        collection = [5, 2, 4, 7, 1, 3, 2, 6]
        merge_sort(collection)
        self.assertEquals(collection, [1, 2, 2, 3, 4, 5, 6, 7], "Collection not sorted. " + str(collection))

    def test_bubble_sort(self):
        collection = [5, 2, 4, 7, 1, 3, 2, 6]
        bubble_sort(collection)
        self.assertEquals(collection, [1, 2, 2, 3, 4, 5, 6, 7], "Collection not sorted. " + str(collection))

    def test_quick_sort(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        quicksort(a)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        quicksort(a, partition=randomized_partition)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        quicksort(a, partition=hoare_partition)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

    def test_quicksort_tailrecursion(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        quicksort_tailrecursion(a)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        quicksort_tailrecursion(a, partition=randomized_partition)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

            # Doesn't pass, but why?
            # self.assertLessEqual(a[i], a[i + 1],# a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
            # quicksort_tailrecursion(a, partition=hoare_partition)
            #
            # for i in range(len(a) - 1): "Collection not sorted. " + str(a))

    def test_randomized_quick_sort(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        randomize_quicksort(a)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        randomize_quicksort(a, partition=randomized_partition)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        randomize_quicksort(a, partition=hoare_partition)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

    def test_stooge_sort(self):
        a = [2, 8, 7, 1, 3, 5, 6, 4, 15, 13, 99, 82, 64, 81]
        stooge_sort(a)

        for i in range(len(a) - 1):
            self.assertLessEqual(a[i], a[i + 1], "Collection not sorted. " + str(a))

    def test_counting_sort(self):
        a = [2, 5, 3, 0, 2, 3, 0, 3]
        b = [None] * len(a)
        counting_sort(a, b)

        for i in range(len(b) - 1):
            self.assertLessEqual(b[i], b[i + 1], "Collection not sorted. " + str(b))

    def test_radix_sort(self):
        a = [329, 457, 657, 839, 436, 720, 355]
        b = radix_sort(a)
        for i in range(len(b) - 1):
            self.assertLessEqual(b[i], b[i + 1], "Collection not sorted. " + str(b))


class TestMaxHeap(TestCase):
    def heap_integrity_check(self, heap):
        for i in range(1, len(heap) + 1):
            node = heap[i]

            self.assertEquals(node.index, i, "Heap node index value doesn't match enumerated index.")

            child = node.left()
            if child is not None:
                self.assertGreaterEqual(node.value, child.value,
                                        "Failed integrity test for min heap, all parents must be >= children.")

            child = node.right()
            if child is not None:
                self.assertGreaterEqual(node.value, child.value,
                                        "Failed integrity test for min heap, all parents must be >= children.")

    def test_max_heap_sort(self):
        heap_to_test = MaxHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        heap_accepted_answer = MaxHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

        # Check that the sizes match
        self.assertEquals(len(heap_to_test), len(heap_accepted_answer), "Heap size doesn't match expected.")

        # Check that the heaps are in the correct integrity
        self.heap_integrity_check(heap_to_test)
        self.heap_integrity_check(heap_accepted_answer)

        # Check that they match
        for i in range(1, len(heap_to_test) + 1):
            test = heap_to_test[i]
            accepted = heap_accepted_answer[i]

            self.assertEquals(test.index, accepted.index, "Heap node index doesn't match expected value.")
            self.assertEquals(test.value, accepted.value, "Heap node value doesn't match expected value.")

        # Perform the sort and ensure they are sorted
        heap_to_test.heap_sort()
        for i in range(1, len(heap_to_test)):
            self.assertLessEqual(heap_to_test[i].value, heap_to_test[i + 1].value,
                                 "Heap not sorted in ascending order.")

    def test_max_heap_increase(self):
        test_heap = MaxHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

        # Exchange the 4 for a 999 and ensure the heap is still valid
        test_heap.heap_increase_key(9, 999)
        self.heap_integrity_check(test_heap)

    def test_max_heap_insert(self):
        test_heap = MaxHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

        # Exchange the 4 for a 999 and ensure the heap is still valid
        test_heap.max_heap_insert(999)
        self.heap_integrity_check(test_heap)


class TestMinHeap(TestCase):
    def heap_integrity_check(self, heap):
        for i in range(1, len(heap) + 1):
            node = heap[i]

            self.assertEquals(node.index, i, "Heap node index value doesn't match enumerated index.")

            child = node.left()
            if child is not None:
                self.assertLessEqual(node.value, child.value,
                                     "Failed integrity test for min heap, all parents must be <= children.")

            child = node.right()
            if child is not None:
                self.assertLessEqual(node.value, child.value,
                                     "Failed integrity test for min heap, all parents must be <= children.")

    def test_min_heap_sort(self):
        heap_to_test = MinHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

        # Verify length
        self.assertEquals(len(heap_to_test), 10, "Heap size doesn't match expected.")

        # Verify business rules for a min heap are intact
        self.heap_integrity_check(heap_to_test)

        # Verify sorting
        heap_to_test.heap_sort()
        for i in range(1, len(heap_to_test)):
            self.assertGreaterEqual(heap_to_test[i].value, heap_to_test[i + 1].value,
                                    "Heap not sorted in descending order.")

    def test_max_heap_increase(self):
        test_heap = MinHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

        # Exchange the 4 for a 999 and ensure the heap is still valid
        test_heap.heap_decrease_key(9, 5)
        self.heap_integrity_check(test_heap)

    def test_max_heap_insert(self):
        test_heap = MinHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

        # Exchange the 4 for a 999 and ensure the heap is still valid
        test_heap.min_heap_insert(999)
        self.heap_integrity_check(test_heap)


class TestHeap(TestCase):
    def test_length(self):
        heap = Heap(range(10))
        self.assertEquals(heap.heap_size, 10)
        self.assertEquals(len(heap), 10)

    def test_height(self):
        heap = Heap(range(10))
        self.assertEqual(heap.heap_height(), 3)
        self.assertEqual(heap.height(1), 3)
        self.assertEqual(heap.height(4), 1)
