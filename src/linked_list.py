"""Module defining linked list."""


class LinkedList(object):
    """Classic linked list data structure."""

    def __init__(self, head=None):
        """Initialize LinkedList instance."""
        self.head = head

    def push(self, val):
        """Insert val at the head of linked list."""
        self.head = Node(val, self.head)


class Node(object):
    """Node class."""

    def __init__(self, val, next):
        """Initialize Node instance."""
        self.val = val
        self.next = next
