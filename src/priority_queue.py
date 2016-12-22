"""Implementation of Priority Queue."""
from bin_heap import BinaryHeap


class PriorityQueue(object):
    """Priority list queue."""

    def __init__(self, iterable=None):
        """Construct priority queue."""
        self._heap = BinaryHeap()
        if iterable:
            try:
                for item in iterable:
                    self._insert(*item)
            except TypeError:
                raise TypeError("Optional argument of priority queue must be iterable.")

    def insert(self, data, priority=0):
        """."""
        self._heap.push((priority, data))

    def pop(self):
        """."""
        try:
            return self._heap.pop()
        except IndexError:
            raise IndexError('Cannot pop from empty priority queue.')

    def peek(self):
        """Peeks at the highest priority tuple."""
        return self._heap._list[0]


