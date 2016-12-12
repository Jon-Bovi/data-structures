"""Module defining linked list."""


class LinkedList(object):
    """Classic linked list data structure."""

    def __init__(self, iterable=None):
        """Initialize LinkedList instance."""
        self.head = None
        if iterable:
            for el in iterable:
                self.push(el)


    def push(self, val):
        """Insert val at the head of linked list."""
        self.head = Node(val, self.head)

    def pop(self):
        """Pop the first value off of the head and return it."""
        if self.head is None:
            return None
        first = self.head.val
        self.head = self.head.next
        return first

    def size(self):
        """Return length of linked list."""
        length = 0
        curr = self.head
        while curr is not None:
            length += 1
            curr = curr.next
        return length


class Node(object):
    """Node class."""

    def __init__(self, val, next):
        """Initialize Node instance."""
        self.val = val
        self.next = next
