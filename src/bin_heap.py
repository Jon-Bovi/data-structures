"""Module containing implementation of a binary heap."""


class BinaryHeap(object):
    """Implementation of Binary heap: methods: push and pop."""

    def __init__(self, iterable=None, minmax='max'):
        """Construct new binary heap."""
        self._list = []
        if minmax == 'min':
            self._minmax = -1
        elif minmax == 'max':
            self._minmax = 1
        else:
            raise TypeError("min/max optional parameter must be 'min' or 'max'")
        if iterable:
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
            self._swap(0, len(self._list) - 1)
            res = self._list.pop()
            self._organize_children(0)
            return res
        except IndexError:
            raise IndexError('Cannot pop from an empty heap.')

    def _organize_up(self, i):
        """Organize heap starting from node i and moving up towards root."""
        while i > 0 and self._minmax * self._list[i] < self._minmax * self._list[self._parent(i)]:
            self._swap(self._parent(i), i)
            i = self._parent(i)

    def _organize_children(self, i):
        """Organize from node at index i down."""
        self._organize_branch(i, 2 * i + 1)
        self._organize_branch(i, 2 * i + 2)

    def _swap(self, i, k):
        """Swap nodes at indexes i and k."""
        self._list[i], self._list[k] = self._list[k], self._list[i]

    def _parent(self, i):
        """Return index of node i's parent."""
        return i // 2 + (i % 2 - 1)

    def _organize_branch(self, parent_i, child_i):
        """Compare parent with child, swap and continue to organize if needed."""
        if child_i < len(self._list):
            parent_value = self._minmax * self._list[parent_i]
            child_value = self._minmax * self._list[child_i]
            if child_value < parent_value:
                self._swap(parent_i, child_i)
                self._organize_children(child_i)
