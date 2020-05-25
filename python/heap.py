import operator


class Heap:
    """
    A class that satisfies the properties of a binary heap.

    Conditions:
    - complete tree
    - root node must be min/max among all child nodes of min/max heap
    - all subtrees follow the above conditions
    """

    def __init__(self, lst=[], comparator=operator.lt):
        self._heap = [None] + lst
        self.compare = comparator

        self._heapify()

    def is_empty(self):
        """ Check whether the heap is empty. """
        return len(self._heap) <= 1

    def insert(self, value):
        """
        Insert a value into the heap, keeping the integrity of the heap.

        Time complexity: O(logn)
        """
        self._heap.append(value)
        self._heapify_up(self.size())

    def get_top(self):
        """
        Peek at the top value of the heap, heap remains unchanged.

        Time complexity: O(1)
        """
        return None if self.is_empty() else self._heap[1]

    def extract_top(self):
        """
        Remove and return the top value of the heap, heap is modified.

        Time complexity: O(logn)
        """
        ret_val = self.get_top()
        self._heap[1] = self._heap[-1]
        self._heap.pop()
        self._heapify_down(1)
        return ret_val

    def _heapify_up(self, curr):
        """
        Propogates from a starting position up to maintain the integrity of the heap.
        Used in tandem with insert to ensure integrity of heap properties.

        Time complexity: O(logn)
        """
        while curr > 1:
            parent = self._parent(curr)
            if self.compare(self._heap[parent], self._heap[curr]):
                return
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    def _heapify_down(self, curr):
        """
        Propogates from a starting position down to maintain the integrity of the heap.
        Used in tandem with deletions and heapify.

        Time complexity: O(logn)
        """
        if self.size() <= 1:
            return

        while not self._is_leaf(curr):
            left, right = self._child(curr), self._child(curr, is_right=True)

            # check whether need to propogate further down
            child = left
            if right <= self.size() and self.compare(self._heap[right], self._heap[left]):
                child = right
            if self.compare(self._heap[curr], self._heap[child]):
                return

            # propogate down to either left or right sub-child
            self._swap(curr, child)
            curr = child

    def _heapify(self):
        """
        Convert the underlying list structure into a heap.

        Time complexity: O(n)
        """
        for idx in range(self.size() // 2, 0, -1):
            self._heapify_down(idx)

    def size(self):
        """ Get the size of the heap. """
        return len(self._heap) - 1

    def to_list(self):
        """ Get the underlying list structure of the heap. """
        return self._heap[1:]

    def is_heap(self, curr=1):
        """ Check whether the heap satisfies all the conditions of a heap. """
        if self.is_empty():
            return True
        return self._is_heap(curr)

    def _is_heap(self, curr):
        if self._is_leaf(curr):
            return True

        left, right = self._child(curr), self._child(curr, is_right=True)
        res = self.compare(
            self._heap[curr], self._heap[left]) or self._heap[curr] == self._heap[left]

        if res and right <= self.size():
            res = self.compare(
                self._heap[curr], self._heap[right]) or self._heap[curr] == self._heap[right]

        return res

    def _is_leaf(self, pos):
        """ Check whether the position is a leaf node. """
        return (2 * pos) > self.size()

    def _parent(self, pos):
        """ Get the parent node given a position in the heap. """
        return pos // 2

    def _child(self, pos, is_right=False):
        """ Get the child node given a position. By default gets the left child. """
        return (2 * pos) + is_right

    def _swap(self, pos1, pos2):
        """ Helper method to swap two elements of the heap. """
        self._heap[pos1], self._heap[pos2] = self._heap[pos2], self._heap[pos1]

    def __str__(self):
        return str(self.to_list())


if __name__ == "__main__":
    # min heap by default
    print("---- Min Heap")
    lst = [2, 4, 72, 7, 9, 1, 5, 6, 21]
    heap = Heap(lst)
    while not heap.is_empty():
        min_val = heap.extract_top()
        assert heap.is_heap()
        print(min_val, heap)

    print("\n---- Max Heap")
    lst = [9, 72, 21, 7]
    heap = Heap(lst, comparator=operator.gt)
    while not heap.is_empty():
        max_val = heap.extract_top()
        assert heap.is_heap()
        print(max_val, heap)
