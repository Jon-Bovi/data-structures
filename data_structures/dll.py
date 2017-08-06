"""Module containing DoublyLinkedList class."""

from data_structures import LinkedList


class DoublyLinkedList(LinkedList):
    """Doubly-linked list class."""

    def __init__(self, iterable=None):
        """Construct new doubly-linked list."""
        self.head = None
        self.tail = None
        self._length = 0
        if iterable:
            try:
                for item in iterable:
                    self.push(item)
            except:
                raise ValueError("DoublyLinkedList optional parameter must be iterable.")

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
        return self._popshift(self.head, 'pop')

    def shift(self):
        """Remove the tail and return its value."""
        return self._popshift(self.tail, 'shift')

    def _popshift(self, node, name):
        if node is None:
            raise IndexError('Cannot ' + name + ' from an empty linked list.')
        self._length -= 1
        value = node.val
        if self.head.next is None or self.tail.prev is None:
            self.tail = None
            self.head = None
        else:
            if name == 'pop':
                self.head = self.head.next
                self.head.prev = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        return value

    def remove(self, val):
        """Remove node from dll."""
        curr = self.head
        if not curr:
            raise IndexError("Cannot remove from an empty list.")
        found = False
        while not found and curr:
            if curr.val == val:
                found = True
                self._length -= 1
                if curr.prev is None:
                    self.head = self.head.next
                else:
                    curr.prev.next = curr.next
                if curr.next is None:
                    self.tail = self.tail.prev
                else:
                    curr.next.prev = curr.prev
            curr = curr.next
        if not found:
            raise ValueError("Value not in list.")


class DoubleNode(object):
    """Node class."""

    def __init__(self, val, prev=None, next=None):
        """Construct new DoubleNode."""
        self.val = val
        self.prev = prev
        self.next = next
