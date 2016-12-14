"""Module containing DoublyLinkedList class."""


class DoublyLinkedList(object):
    """Doubly-linked list class."""

    def __init__(self, iterable=None):
        """Construct new doubly-linked list."""
        self.head = None
        self.tail = None
        self._length = 0

    def push(self, val):
        """Insert new node at head of dll."""
        self.head = DoubleNode(val, None, self.head)
        self._length += 1


class DoubleNode(object):
    """Node class."""

    def __init__(self, val, prev=None, next=None):
        """Construct new DoubleNode."""
        self.val = val
        self.prev = prev
        self.next = next
