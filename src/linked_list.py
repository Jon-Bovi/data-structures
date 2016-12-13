"""Module defining linked list."""


class LinkedList(object):
    """Classic linked list data structure."""

    def __init__(self, iterable=None):
        """Initialize LinkedList instance."""
        self.head = None
        self._length = 0
        if iterable and hasattr(iterable, '__iter__'):
            for el in iterable:
                self.push(el)

    def push(self, val):
        """Insert val at the head of linked list."""
        self.head = Node(val, self.head)
        self._length += 1

    def pop(self):
        """Pop the first value off of the head and return it."""
        if self.head is None:
            return None
        first = self.head.val
        self.head = self.head.next
        self._length -= 1
        return first

    def size(self):
        """Return length of linked list."""
        return self._length

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
                self._length -= 1
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

    def __len__(self):
        """Return length of linked_list."""
        return self.size()


class Node(object):
    """Node class."""

    def __init__(self, val, next=None):
        """Initialize Node instance."""
        self.val = val
        self.next = next
