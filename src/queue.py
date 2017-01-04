"""Queue module."""
from dll import DoublyLinkedList


class Queue(object):
    """First in first out queue structure."""

    def __init__(self, iterable=None):
        """Construct queue."""
        try:
            self._dll = DoublyLinkedList(iterable)
        except ValueError:
            raise ValueError("Queue optional parameter must be iterable.")

    def enqueue(self, val):
        """Add value to the queue."""
        self._dll.append(val)

    def dequeue(self):
        """Remove item from the queue and returns an error if queue empty."""
        try:
            return self._dll.pop()
        except:
            raise IndexError('Cannot dequeue from an empty queue.')

    def peek(self):
        """Return the next value in the queue without dequeueing it. If the."""
        """queue is empty, returns None."""
        return self.head.val if self.head else None

    def size(self):
        """Return the size of the queue, if empty return 0."""
        return self._dll._length

    def clear(self):
        """Empty queue."""
        self._dll.head = None
        self._dll.tail = None
        self._dll._length = 0

    def __len__(self):
        """Return length of queue."""
        return self.size()

    @property
    def head(self):
        """Read only head property."""
        return self._dll.head

    @property
    def tail(self):
        """Read only tail property."""
        return self._dll.tail
