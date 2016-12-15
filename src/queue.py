"""Queue module."""
from linked_list import LinkedList


class Queue(LinkedList):
    """First in first out queue structure."""

    def __init__(self, iterable=None):
        """Construct queue."""
        self.head = None
        self.tail = None
        self._length = 0

    def enqueue(self, val):
        """Add value to the queue."""
        if self.tail is None:
            self._insert_new(val)
        else:
            self.tail.append(val)
        self._length += 1

    def dequeue(self):
        """Remove item from the queue and returns an error if queue empty."""
        if self.head is None:
            raise IndexError('Cannot dequeue from an empty queue.')
        else:
            self.head.pop()

    def peek(self, val):
        """Return the next value in the queue without dequeueing it. If the."""
        """queue is empty, returns None."""
        if self.head is None:
            raise IndexError('Cannot dequeue from an empty queue.')
        else:
            self.head -= 1
            return val

    def size(self):
        """Return the size of the queue, if empty return 0."""
        if self.head is None:
            raise IndexError('There is no items in the queue.')
        else:
            return self._length
