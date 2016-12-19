"""Module with implementation of deque data structure."""
from dll import DoublyLinkedList


class Deque(object):
    """."""

    def __init__(self, iterable=None):
        """Construct deque."""
        self._dll = DoublyLinkedList(iterable)

    def appendleft(self, val):
        """Add value at the from of deque."""
        self._dll.push(val)

    def append(self, val):
        """Add value to the back of deque."""
        self._dll.append(val)

    def pop(self):
        """Remove value from back of deque."""
        try:
            return self._dll.shift()
        except IndexError:
            raise IndexError('Cannot pop from an empty deque.')

    def popleft(self):
        """Remove value from front of deque."""
        try:
            return self._dll.pop()
        except IndexError:
            raise IndexError('Cannot pop from an empty deque.')
