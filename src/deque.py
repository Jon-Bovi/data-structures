"""Module with implementation of deque data structure."""
from dll import DoublyLinkedList


class Deque(object):
    """."""

    def __init__(self, iterable=None):
        """Construct deque."""
        self._dll = DoublyLinkedList(iterable)
