"""Module containing implementation of a binary heap."""


class Binary_Heap(object):
    """Binary heap: methods: push and pop."""
    def __init__(self, iterable=None):
        """Construct new binary heap."""
        self._list = []
        if iterable:
            try:
                for item in sorted(iterable):
                    self._list.append(item)
            except TypeError:
                raise TypeError("Optional binary heap argument must be iterable.")

