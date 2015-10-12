import math
import random


# region Comparison Sorts
# Comparison sorts are categorized by the assumption that the sorted order they determine is based only on
# comparisons between the input elements.


def insertion_sort(collection):
    """
    Chapter 2: Insertion sorts in place. An insertion sort works by visiting each element
    in a collection and placing into the correct position relative to each of the elements before it.
    :param collection: A collection that can be indexed. Will be modified in place.
    """
    for j in range(1, len(collection)):
        key = collection[j]

        # Insert the key into the sorted sequence collection[1..j-1]
        i = j - 1
        while i >= 0 and collection[i] > key:
            collection[i + 1] = collection[i]
            i = i - 1
        collection[i + 1] = key


def merge_sort(collection, p=None, r=None):
    """
    Chapter 2: Merge sorts in place. The merge sort works by taking an array, or a section of an array, of starting
    index p and ending index r, finding the midpoint between them q and diving it into two arrays:
    left [p...q] and right [q+1...r]. It then recursively loops through these arrays re-applying and redefining p, r,
    and consequently q for each recursion until there is only 1 thing each array. It then climbs back up the recursive
    calls merging the two arrays together by comparing the values at each position and always placing the lower value
    element in the left or right array before the higher value in the opposite array.
    :param collection: The collection to sort.
    :param p: The starting index.
    :param r: The ending index.
    """

    def merge(collection, p, q, r):
        """
        Merges two sorted portions of a collection in place.
        :param collection: The collection to sort.
        :param p: The first index first array.
        :param q: The last index of the first array.
        :param r: The last index of the second array.
        """
        n1 = q - p + 1
        n2 = r - q
        left_array = [None] * (n1 + 1)
        right_array = [None] * (n2 + 1)
        for i in range(n1):
            left_array[i] = collection[p + i]
        for j in range(n2):
            right_array[j] = collection[q + j + 1]
        left_array[n1] = None  # Dummy value that means this value is larger than any possible value
        right_array[n2] = None  # Dummy value that means this value is larger than any possible value
        i = 0
        j = 0
        for k in range(p, r + 1):
            # If the right array is automatically larger
            # OR
            # If the left array is not automatically larger AND the actual left value is less than or equal to the
            # actual right value
            if right_array[j] is None or (left_array[i] is not None and left_array[i] <= right_array[j]):
                collection[k] = left_array[i]
                i = i + 1
            else:
                collection[k] = right_array[j]
                j = j + 1

    # Check the inputs
    if p == None:
        p = 0

    if r == None:
        r = len(collection) - 1

    # Perform the search
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(collection, p, q)
        merge_sort(collection, q + 1, r)
        merge(collection, p, q, r)


def bubble_sort(collection):
    """
    Chapter 2: Bubble Sorts in place. Bubble sort works by looping through each element in an array and comparing it to
    the element below it. If the values are out of order they are switched.
    :param collection: The collection to sort in place.
    """
    for i in range(len(collection)):
        for j in range(len(collection) - 1, i, -1):
            if collection[j] < collection[j - 1]:
                collection[j], collection[j - 1] = collection[j - 1], collection[j]


def stooge_sort(collection, i=None, j=None):
    """
    Chapter 7: Sorting algorithm proposed by Professors Howard, Fine, and Howard...
    :param collection: The collection to sort in place.
    :param i: The lower bound.
    :param j: The upper bound.
    """

    # Check the inputs
    if i == None:
        i = 0

    if j == None:
        j = len(collection) - 1

    if collection[i] > collection[j]:
        collection[i], collection[j] = collection[j], collection[i]

    if i + 1 >= j:
        return

    k = math.floor((j - i + 1) / 3)

    # First two-thirds
    stooge_sort(collection, i, j - k)

    # Last two-thirds
    stooge_sort(collection, i + k, j)

    # First two-thirds again
    stooge_sort(collection, i, j - k)


# region Quick Sort


def partition(collection, p, r):
    """
    Chapter 7: Rearranges the sub array (indexes p-r of the passed in collection) in place such that for a chosen pivot
    (always the last element) all elements to the left of the pivot are less than or equal to it and all elements to the
    right are larger than it.
    :param collection: The collection to sort.
    :param p: The lower bounds of the sort.
    :param r: The upper bounds of the sort.
    """
    # Define the pivot point
    pivot = collection[r]

    # Sort the array given the following criteria
    # 1. If p <= k <= i, then collection[k] <= pivot
    # 2. If i + 1 <= k <= j - 1, then collection[k] > pivot
    # 3. If k = r, then collection[k] = pivot
    i = p - 1
    for j in range(p, r):
        if collection[j] <= pivot:
            i += 1
            collection[i], collection[j] = collection[j], collection[i]
    collection[i + 1], collection[r] = collection[r], collection[i + 1]
    return i + 1


def randomized_partition(collection, p, r):
    """
    Chapter 7: Rearranges the sub array (indexes p-r of the passed in collection) in place such that for a chosen pivot
    (a random element) all elements to the left of the pivot are less than or equal to it and all elements to the
    right are larger than it.
    :param collection: The collection to sort.
    :param p: The lower bounds of the sort.
    :param r: The upper bounds of the sort.
    """
    i = random.randint(p, r)
    collection[r], collection[i] = collection[i], collection[r]
    return partition(collection, p, r)


def hoare_partition(collection, p, r):
    """
    Chapter 7: Rearranges the sub array (indexes p-r of the passed in collection) in place such that for a chosen pivot
    all elements to the left of the pivot are less than or equal to it and all elements to the right are larger than it.
    Original partition implementation by C. A. R. Hoare.
    :param collection: The collection to sort.
    :param p: The lower bounds of the sort.
    :param r: The upper bounds of the sort.
    """
    x = collection[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j -= 1
            if collection[j] <= x:
                break
        while True:
            i += 1
            if collection[i] >= x:
                break
        if i < j:
            collection[i], collection[j] = collection[j], collection[i]
        else:
            return j


def quicksort(collection, p=None, r=None, partition=partition):
    """
    Chapter 7: Quick sorts a collection in place. Quick sort works by defining an element as the pivot point (the
    partition method chooses which element) and sorting the collection such that all elements to the left of the
    pivot point are less than or equal to it and all elements to the right are greater than it. It then recurses and
    performs the same operation the left and right sides of the pivot point. Since the pivot point is always placed in
    the correct place relative to all of the rest of the collection and the recursive calls ensure each element is
    visited as a pivot point the collection is sorted.
    :param collection: The collection to sort.
    :param p: The lower bounds of the sort.
    :param r: The upper bounds of the sort.
    :param partition: The partition method to use.
    """
    # Check the parameters
    if p is None:
        p = 0

    if r is None:
        r = len(collection) - 1

    # Perform the sort
    if p < r:
        q = partition(collection, p, r)
        quicksort(collection, p, q - 1)
        quicksort(collection, q + 1, r)


def randomize_quicksort(collection, p=None, r=None, partition=randomized_partition):
    """
    Chapter 7: Quick sorts a collection in place. Quick sort works by defining an element as the pivot point (the
    default partition method chooses randomly) and sorting the collection such that all elements to the left of the
    pivot point are less than or equal to it and all elements to the right are greater than it. It then recurses and
    performs the same operation the left and right sides of the pivot point. Since the pivot point is always placed in
    the correct place relative to all of the rest of the collection and the recursive calls ensure each element is
    visited as a pivot point the collection is sorted.
    :param collection: The collection to sort.
    :param p: The lower bounds of the sort.
    :param r: The upper bounds of the sort.
    :param partition: The partition method to use.
    """
    quicksort(collection, p, r, partition)


def quicksort_tailrecursion(collection, p=None, r=None, partition=partition):
    """
    Chapter 7: Quick sorts a collection in place. Quick sort works by defining an element as the pivot point (the
    partition method chooses which element) and sorting the collection such that all elements to the left of the
    pivot point are less than or equal to it and all elements to the right are greater than it. It then recurses and
    performs the same operation the left and right sides of the pivot point. Since the pivot point is always placed in
    the correct place relative to all of the rest of the collection and the recursive calls ensure each element is
    visited as a pivot point the collection is sorted.

    NOTE: This method doesn't work in Python as the language's compiler doesn't support tail recursion. It is
          included for the purposes of completeness.

    :param collection: The collection to sort.
    :param p: The lower bounds of the sort.
    :param r: The upper bounds of the sort.
    :param partition: The partition method to use.
    """
    # Check the parameters
    if p is None:
        p = 0

    if r is None:
        r = len(collection) - 1

    # Perform the sort
    while p < r:
        q = partition(collection, p, r)
        quicksort_tailrecursion(collection, p, q - 1)
        p = q + 1


# endregion


# region Heap Sort


class Heap():
    """
    Chapter 6: The base of a binary tree which can be sub-classed to either be a max or a min heap.
    Uses a one based index.
    """

    class HeapNode:
        def __init__(self, heap, index, value, handle=None):
            """
            Initializes a new instance of the HeapNode class.
            :param index: The index of the node in the flattened heap represented as an array with a one based index.
            :param value: The value of the node to use as a weight in the heap tree.
            :param handle: The object associated with the node.
            """
            self.heap = heap
            self.index = index
            self.value = value
            self.handle = handle

        def __str__(self):
            return "<Heap.HeapNode> Index: " + str(self.index) + " Value: " + str(self.value) + " Handle: " + str(
                self.handle)

        def left(self):
            """
            Chapter 6: Retrieves the left child.
            :return: The left child.
            """
            index = self.heap.left(self.index)
            if len(self.heap) >= index:
                return self.heap[index]
            else:
                return None

        def right(self):
            """
            Chapter 6: Retrieves the right child.
            :return: The right child.
            """
            index = self.heap.right(self.index)
            if len(self.heap) >= index:
                return self.heap[index]
            else:
                return None

        def parent(self):
            """
            Chapter 6: Retrieves the parent.
            :return: The parent.
            """
            index = self.heap.parent(self.index)
            if len(self.heap) >= index:
                return self.heap[index]
            else:
                return None

    def __init__(self, collection):
        """
        Initializes a new instance of the Heap class.
        :param collection: The collection to base the heap off of. If an entry is multi-dimensional index 0
                           will be used as the value (weight) of the node and index 1 will be used as the handle.
                           Otherwise, if the entry is able to be indexed it will only be used as a value.
        """
        self.list = []

        if collection is not None:
            for i in range(len(collection)):
                try:
                    self.list.append(Heap.HeapNode(self, i + 1, collection[i][0], collection[i][1]))
                except:
                    self.list.append(Heap.HeapNode(self, i + 1, collection[i]))

        self.heap_size = len(collection)

    def __getitem__(self, index):
        """
        Chapter 6: Gets the node at the requested index for a one based index array.
        :param index: The one based index to retrieve.
        :return: The item in the one based index location.
        """
        return self.list[index - 1]

    def __setitem__(self, index, value):
        """
        Chapter 6: Sets the node at the requested index for a one based index array.
        Handles setting HeapNode index parameter.
        :param index: The one based index to set.
        :param value: The value to set the one based index to.
        """
        if len(self.list) < index:
            raise IndexError("Index larger than collection")

        if index < 1:
            raise IndexError("Index too small")

        value.index = index
        self.list[index - 1] = value

    def __len__(self):
        """
        Chapter 6: The total number of nodes in the heap.
        :return: The total number of nodes in the heap.
        """
        return len(self.list)

    def parent(self, i):
        """
        Chapter 6: Retrieves the parent node's one based index.
        :param i: The one based index to find the parent of.
        :return: The parent node's one based index.
        """
        # Or shift i right one position
        return math.floor(i / 2)

    def left(self, i):
        """
        Chapter 6: Retrieves the left child node's one based index.
        :param i: The one based index to find the left child of.
        :return: The left child node's one based index.
        """
        # Or shift i left one position
        return 2 * i

    def right(self, i):
        """
        Chapter 6: Retrieves the right child node's one based index.
        :param i: The one based index to find the right child of.
        :return: The right child node's one based index.
        """
        # Or shift i left one position and add one as the lower order bit
        return 2 * i + 1

    def height(self, i):
        """
        Chapter 6: The height is the number of vertices between the passed in index and the leaf.
        :param i: The one based index to find the height of.
        """
        n = len(self)
        vertices = 0
        index = self.left(i)
        while index <= n:
            index = self.left(index)
            vertices += 1

        return vertices

    def heap_height(self):
        """
        Chapter 6: The heap size is the number of vertices between the root node and the farthest leaf.
        In general the height of a heap is the floor of the log2(total nodes)
        """
        return math.floor(math.log(len(self.list), 2))


class MaxHeap(Heap):
    """
    Chapter 6: A max heap is a binary tree where each node satisfies the condition:
    The parent node's value is larger than or equal to the child node's value.
    The heap uses a one based index.
    """

    def __init__(self, collection):
        """
        Initializes a new instance of the Heap class.
        :param collection: The collection to base the heap off of. If an entry is multi-dimensional index 0
                           will be used as the value (weight) of the node and index 1 will be used as the handle.
                           Otherwise, if the entry is able to be indexed it will only be used as a value.
        """
        Heap.__init__(self, collection)
        self.build_max_heap()

    def build_max_heap(self):
        """
        Chapter 6: Builds a max heap out of the current collection.
        """
        self.heap_size = len(self)
        for i in range(math.floor(len(self) / 2), 0, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        """
        Chapter 6: Manipulates the existing heap, in place, in order to satisfy the max heap condition.
        When called it is assumed that the binary tree nodes at right(i) and left(i) are already
        satisfying the max heap property but that index i may not.
        :param i: The index that is out of place in the heap.
        """
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self[l].value > self[i].value:
            largest = l
        else:
            largest = i

        if r <= self.heap_size and self[r].value > self[largest].value:
            largest = r

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def heap_sort(self):
        """
        Chapter 6: Heap sorts in place in ascending order. The heap sort works by splitting an array into two section:
        the heap [0...heap_size] and the sorted answer [heap_size - 1...len(array)]. It then sections off the entire
        array as the heap. This done automatically when a MaxHeap object is created on the passed in collection. Next,
        the largest item in the heap is removed (which is always the root node) and placed at the beginning of the
        sorted answer section. Finally, the heap is rebalanced with a new maximum value root node and the process is
        repeated until there are no more elements in the heap and the entire array is sectioned off as the sorted
        answer.
        """
        # Called as a precaution to ensure that it is already true, as long as nothing was added it should be.
        self.build_max_heap()

        # Loop through and exchange the root (which should always be the largest thing), with the right most leaf
        for i in range(len(self), 2 - 1, -1):
            self[1], self[i] = self[i], self[1]

            # We removed a node from the heap
            self.heap_size -= 1

            # Re-heapify the root, it likely will no longer the largest thing in the list and we need it to be.
            self.max_heapify(1)

    def heap_maximum(self):
        """
        Chapter 6: Retrieves the maximum of the heap. Always the root node.
        :return: The largest node of the heap.
        """
        return self[1]

    def heap_extract_max(self):
        """
        Chapter 6: Removes the largest node from the heap.
        :return: The largest node.
        """
        if self.heap_size < 1:
            raise Exception("Attempt to extract node without any nodes in heap.")

        # The root is always the max
        max = self[1]

        # Set the new root
        self[1] = self[self.heap_size]

        # Correct the new size
        self.heap_size -= 1

        # Re-stabilize the heap
        self.max_heapify(1)
        return max

    def heap_increase_key(self, i, key):
        """
        Chapter 6: Increases the key (value) of the node to the passed in key (value).
        :param i: The index to modify.
        :param key: The new value.
        """
        # None is a placeholder value for the smallest possible number.
        if self[i].value is not None and key < self[i].value:
            raise AttributeError("The passed in key was less than the current value.")

        # Set the new value
        self[i].value = key

        # Search upwards for the correct placement of the current node. If the node is None represents the
        # smallest possible number.
        while i > 1 and (self[self.parent(i)].value is None or self[self.parent(i)].value < self[i].value):
            self[i], self[self.parent(i)] = self[self.parent(i)], self[i]
            i = self.parent(i)

    def max_heap_insert(self, key):
        """
        Chapter 6: Creates a new node with the given value.
        :param key: The value to add to the heap. If the value is multidimensional index 0 will be the value
                    and index 1 will be the handle.
        """
        # Gather inputs
        handle = None
        try:
            value, handle = key[0], key[1]
        except:
            value = key

        # Increase the heap's size by one
        self.heap_size += 1

        # If the heap size is larger than the array, we need to increase the size of the array.
        if self.heap_size > len(self.list):
            # If the heap size is larger than the array by more than 1 something has gone wrong and we need to stop.
            if self.heap_size != len(self.list) + 1:
                raise Exception("Internal error, heap size is incorrect.")

            # Add to the end of the list with an invalid value, this will ensure that is the counted as one of the
            # lowest possible values in the heap
            self.list.append(Heap.HeapNode(self, self.heap_size, None, handle))
        else:
            # Add to the end of the list with an invalid value, this will ensure that is the counted as one of the
            # lowest possible values in the heap
            self.list[self.heap_size] = Heap.HeapNode(self, self.heap_size, None, handle)

        # Now change the value
        self.heap_increase_key(self.heap_size, value)


class MinHeap(Heap):
    """
    Chapter 6: A min heap is a binary tree where each node satisfies the condition:
    The parent node's value is less than or equal to the child node's value.
    The heap uses a one based index.
    """

    def __init__(self, collection):
        """
        Initializes a new instance of the Heap class.
        :param collection: The collection to base the heap off of. If an entry is multi-dimensional index 0
                           will be used as the value (weight) of the node and index 1 will be used as the handle.
                           Otherwise, if the entry is able to be indexed it will only be used as a value.
        """
        Heap.__init__(self, collection)
        self.build_min_heap()

    def build_min_heap(self):
        """
        Chapter 6: Builds a min heap out of the current collection.
        """
        self.heap_size = len(self)
        for i in range(math.floor(len(self) / 2), 0, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        """
        Chapter 6: Manipulates the existing heap, in place, in order to satisfy the min heap condition.
        When called it is assumed that the binary tree nodes at right(i) and left(i) are already
        satisfying the min heap property but that index i may not.
        :param i: The index that is out of place in the heap.
        """
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self[l].value < self[i].value:
            smallest = l
        else:
            smallest = i

        if r <= self.heap_size and self[r].value < self[smallest].value:
            smallest = r

        if smallest != i:
            self[i], self[smallest] = self[smallest], self[i]
            self.min_heapify(smallest)

    def heap_sort(self):
        """
        Chapter 6: Heap sorts in place in descending order. The heap sort works by splitting an array into two section:
        the heap [0...heap_size] and the sorted answer [heap_size - 1...len(array)]. It then sections off the entire
        array as the heap. This done automatically when a MinHeap object is created on the passed in collection. Next,
        the smallest item in the heap is removed (which is always the root node) and placed at the beginning of the
        sorted answer section. Finally, the heap is rebalanced with a new minimum value root node and the process is
        repeated until there are no more elements in the heap and the entire array is sectioned off as the sorted
        answer.
        """
        # Called as a precaution to ensure that it is already true, as long as nothing was added it should be.
        self.build_min_heap()

        # Loop through and exchange the root (which should always be the largest thing), with the right most leaf
        for i in range(len(self), 2 - 1, -1):
            self[1], self[i] = self[i], self[1]

            # We removed a node from the heap
            self.heap_size -= 1

            # Re-heapify the root, it likely will no longer the largest thing in the list and we need it to be.
            self.min_heapify(1)

    def heap_minimum(self):
        """
        Chapter 6: Retrieves the minimum of the heap. Always the root node.
        :return: The smallest node of the heap.
        """
        return self[1]

    def heap_extract_min(self):
        """
        Chapter 6: Removes the smallest node from the heap.
        :return: The smallest node.
        """
        if self.heap_size < 1:
            raise Exception("Attempt to extract node without any nodes in heap.")

        # The root is always the max
        min = self[1]

        # Set the new root
        self[1] = self[self.heap_size]

        # Correct the new size
        self.heap_size -= 1

        # Re-stabilize the heap
        self.min_heapify(1)
        return min

    def heap_decrease_key(self, i, key):
        """
        Chapter 6: Decreases the key (value) of the node to the passed in key (value).
        :param i: The index to modify.
        :param key: The new value.
        """
        # None is a placeholder value for the largest possible number.
        if self[i].value is not None and key > self[i].value:
            raise AttributeError("The passed in key was greater than the current value.")

        # Set the new value
        self[i].value = key

        # Search upwards for the correct placement of the current node. If the node is None represents the
        # largest possible number.
        while i > 1 and (self[self.parent(i)].value is None or self[self.parent(i)].value > self[i].value):
            self[i], self[self.parent(i)] = self[self.parent(i)], self[i]
            i = self.parent(i)

    def min_heap_insert(self, key):
        """
        Chapter 6: Creates a new node with the given value.
        :param key: The value to add to the heap. If the value is multidimensional index 0 will be the value
                    and index 1 will be the handle.
        """
        # Gather inputs
        handle = None
        try:
            value, handle = key[0], key[1]
        except:
            value = key

        # Increase the heap's size by one
        self.heap_size += 1

        # If the heap size is larger than the array, we need to increase the size of the array.
        if self.heap_size > len(self.list):
            # If the heap size is larger than the array by more than 1 something has gone wrong and we need to stop.
            if self.heap_size != len(self.list) + 1:
                raise Exception("Internal error, heap size is incorrect.")

            # Add to the end of the list with an invalid value, this will ensure that is the counted as one of the
            # lowest possible values in the heap
            self.list.append(Heap.HeapNode(self, self.heap_size, None, handle))
        else:
            # Add to the end of the list with an invalid value, this will ensure that is the counted as one of the
            # lowest possible values in the heap
            self.list[self.heap_size] = Heap.HeapNode(self, self.heap_size, None, handle)

        # Now change the value
        self.heap_decrease_key(self.heap_size, value)


# endregion


# endregion

def counting_sort(collection, B, k=None):
    """
    Chapter 8: Sorts using a counting sort.
    :param collection:
    :param B:
    :param k:
    :return:
    """

    C = [0] * k
    for j in range(0, len(collection)):
        C[collection[j]] = C[collection[j]] + 1

    # C[i] now contains the number of elements equal to i
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    # C[i] now contains the number of elements less than or equal to i
    for j in range(len(collection), 0, -1):
        B[C[collection[j - 1]] - 1] = collection[j - 1]
        C[collection[j - 1]] = C[collection[j - 1]] - 1


if __name__ == "__main__":
    a = [2, 5, 3, 0, 2, 3, 0, 3]
    B = [None] * len(a)
    counting_sort(a, B, 6)
    print(a)
    print(B)
