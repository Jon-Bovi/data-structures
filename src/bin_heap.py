"""Module containing implementation of a binary heap."""


class Binary_Heap(object):
    """Binary heap: methods: push and pop."""

    def __init__(self, iterable=None, minmax='min'):
        """Construct new binary heap."""
        self._list = []
        if minmax == 'min':
            self._minmax = 1
        elif minmax == 'max':
            self._minmax = -1
        else:
            raise ValueError("min/max optional parameter must be 'min' or 'max'")
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
        """
        Swap root of heap with last heap item,
        remove old root, reorganize heap as needed.
        """
        try:
            self._swap(0, len(self._list) - 1)
            res = self._list.pop()
            self._organize_children(0)
            return res
        except:
            raise IndexError('Cannot pop from an empty heap.')

    def _organize_up(self, i):
        """Organize heap starting from node i and moving up towards root."""
        while i > 0 and self._minmax * (self._list[i]) < self._minmax * (self._list[self._parent(i)]):
            self._swap(self._parent(i), i)
            i = self._parent(i)

    def _organize_children(self, i):
        """Organize from the root down."""
        self._organize_left(i)
        self._organize_right(i)

    def _swap(self, parent, child):
        self._list[parent], self._list[child] = self._list[child], self._list[parent]

    def _parent(self, i):
        return i // 2 + (i % 2 - 1)

    def _organize_left(self, i):
        if 2 * i + 1 < len(self._list) and self._minmax * (self._list[2 * i + 1]) < self._minmax * (self._list[i]):
            self._swap(i, 2 * i + 1)
            self._organize_children(2 * i + 1)

    def _organize_right(self, i):
        if 2 * i + 2 < len(self._list) and self._minmax * (self._list[2 * i + 2]) < self._minmax * (self._list[i]):
            print('hey')
            self._swap(i, 2 * i + 2)
            self._organize_children(2 * i + 2)
