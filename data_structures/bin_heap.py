"""Module containing implementation of a binary heap."""
from operator import lt, gt


class BinaryHeap(object):
    """Implementation of Binary heap: methods: push and pop."""

    def __init__(self, iterable=None, minmax='min'):
        """Construct new binary heap."""
        self._list = [0]
        try:
            self._minmax, self._compare = {
                'min': (min, lt),
                'max': (max, gt)
            }[minmax]
        except KeyError:
            raise ValueError("min/max optional parameter must be 'min' or 'max'")
        if iterable is not None:
            try:
                for item in iterable:
                    self.push(item)
            except TypeError:
                raise TypeError("Optional binary heap argument must be iterable.")

    def push(self, val):
        """Push value to heap."""
        self._list.append(val)
        self._organize_up(len(self._list) - 1)

    def pop(self):
        """Swap root with last item -> remove old root -> heapify heap."""
        try:
            self._swap(1, -1)
            to_pop = self._list.pop()
            self._organize_down(1)
            return to_pop
        except IndexError:
            raise IndexError('Cannot pop from an empty heap.')

    def _organize_up(self, child_i):
        """Organize heap starting from node i and moving up towards root."""
        # import pdb; pdb.set_trace()
        parent_i = child_i // 2
        while parent_i > 0 and self._compare(self._list[child_i], self._list[parent_i]):
            self._swap(parent_i, child_i)
            child_i, parent_i = parent_i, parent_i // 2

    def _swap(self, i, k):
        """Swap nodes at indexes i and k."""
        self._list[i], self._list[k] = self._list[k], self._list[i]

    def _minmaxchild(self, i):
        """Get the min/max child of the parent at index i."""
        children = [(self._list[c], c)
                    for c in (2 * i, 2 * i + 1) if c < len(self._list)]
        return self._minmax(children)

    def _organize_down(self, parent_i):
        """Compare parent with child, swap and continue to organize if needed."""
        try:
            while True:
                child_value, child_i = self._minmaxchild(parent_i)
                parent_value = self._list[parent_i]
                if self._compare(child_value, parent_value):
                    self._swap(parent_i, child_i)
                    parent_i = child_i
                else:
                    return
        except ValueError:
            return
