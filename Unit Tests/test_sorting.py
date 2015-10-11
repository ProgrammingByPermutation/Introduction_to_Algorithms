from unittest import TestCase

from sorting import MaxHeap, insertion_sort, merge_sort, bubble_sort


class TestMiscSort(TestCase):
    def test_insertion_sort(self):
        collection = [5, 2, 4, 6, 1, 3]
        insertion_sort(collection)
        self.assertEquals(collection, [1, 2, 3, 4, 5, 6], "Collection not sorted.")

    def test_merge_sort(self):
        collection = [5, 2, 4, 7, 1, 3, 2, 6]
        merge_sort(collection)
        self.assertEquals(collection, [1, 2, 2, 3, 4, 5, 6, 7], "Collection not sorted.")

    def test_bubble_sort(self):
        collection = [5, 2, 4, 7, 1, 3, 2, 6]
        bubble_sort(collection)
        self.assertEquals(collection, [1, 2, 2, 3, 4, 5, 6, 7], "Collection not sorted.")


class TestMaxHeap(TestCase):
    def test_build_max_heap(self):
        heap_to_test = MaxHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        heap_to_test.build_max_heap()

        heap_accepted_answer = MaxHeap([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

        self.assertEquals(len(heap_to_test), len(heap_accepted_answer), "Heap size doesn't match expected.")
        for i in range(1, len(heap_to_test) + 1):
            test = heap_to_test[i]
            accepted = heap_accepted_answer[i]

            self.assertEquals(test.index, i, "Heap node index value doesn't match enumerated index.")
            self.assertEquals(accepted.index, i, "Heap node index value doesn't match enumerated index.")
            self.assertEquals(test.index, accepted.index, "Heap node index doesn't match expected value.")
            self.assertEquals(test.value, accepted.value, "Heap node value doesn't match expected value.")

    def test_max_heapify(self):
        # Testing test_build_max_heap tests this.
        self.test_build_max_heap()
