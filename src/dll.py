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
        if self.head is None:
            self._insert_new(val)
        else:
            self._insert_beginning(val)
        self._length += 1

    def append(self, val):
        """Add new node at tail of dll."""
        if self.tail is None:
            self._insert_new(val)
        else:
            self._insert_end(val)
        self._length += 1

    def _insert_end(self, val):
        self.tail = DoubleNode(val, self.tail, None)
        self.tail.prev.next = self.tail

    def _insert_new(self, val):
        dnode = DoubleNode(val)
        self.head = dnode
        self.tail = dnode

    def _insert_beginning(self, val):
        self.head = DoubleNode(val, None, self.head)
        self.head.next.prev = self.head

    def pop(self):
        """Remove the head and return the value."""
        if self.head is None:
            raise IndexError('Cannot pop from an empty linked list.')
        first = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return first


class DoubleNode(object):
    """Node class."""

    def __init__(self, val, prev=None, next=None):
        """Construct new DoubleNode."""
        self.val = val
        self.prev = prev
        self.next = next
