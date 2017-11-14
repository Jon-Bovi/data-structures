"""Implementation of Priority Queue."""
from data_structures.bin_heap import BinaryHeap


class PriorityQueue(object):
    """Priority list queue."""

    def __init__(self, iterable=None):
        """Construct priority queue."""
        self._heap = BinaryHeap()
        self._count = 0
        if iterable:
            try:
                for item in iterable:
                    self.insert(*item)
            except TypeError:
                raise TypeError("Optional argument of priority queue must be iterable.")

    def insert(self, data, priority=0):
        """Add item to queue given data and item's priority."""
        self._heap.push((priority, self._count, data))
        self._count += 1

    def pop(self):
        """Remove and return first inserted item of highest priority."""
        try:
            res = self._heap.pop()[2]
            self._count -= 1
            return res
        except IndexError:
            raise IndexError('Cannot pop from empty priority queue.')

    def peek(self):
        """Peek at the highest priority tuple."""
        try:
            return self._heap._list[1][2]
        except IndexError:
            return
