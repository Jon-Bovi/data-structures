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
        while curr:
            length += 1
            curr = curr.next
        return length

    def search(self, val):
        """Will return the node from the list if present, otherwise none."""
        search = self.head
        while search:
            if search.val == val:
                return search
            search = search.next
        return None

    def remove(self, node):
        """Remove a node from linked list."""
        prev = None
        curr = self.head
        while curr:
            if curr is node:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
            prev = curr
            curr = curr.next

    def display(self):
        """Display linked list in tuple literal form."""
        res = "("
        curr = self.head
        while curr:
            val = curr.val
            if type(val) is str:
                val = "'" + val + "'"
            else:
                val = str(val)
            res += val
            if curr.next:
                res += ', '
            curr = curr.next
        return res + ')'


class Node(object):
    """Node class."""

    def __init__(self, val, next):
        """Initialize Node instance."""
        self.val = val
        self.next = next
