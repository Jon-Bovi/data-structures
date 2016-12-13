"""Module with implementation of stack data structure."""
from linked_list import LinkedList


class Stack(object):
    """Stack data structure class."""

    def __init__(self, iterable=None):
        """Stack constructor."""
        self._container = LinkedList(iterable)
        self._update_attr()

    def push(self, val):
        """Add value to top of stack."""
        self._container.push(val)
        self._update_attr()

    def pop(self):
        """Remove and return top of stack."""
        res = self._container.pop()
        self._update_attr()
        return res

    def _update_attr(self):
        self.top = self._container.head
        self.size = self._container.size()
