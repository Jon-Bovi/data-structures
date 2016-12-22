"""Implementation of Priority Queue."""


class PriorityQueue(object):
    """Priority list queue."""

    def __init__(self, iterable=None):
        """Construct priority queue."""
        self.queues = {}
        if iterable is not None:
            for data, priority in iterable:
                self.insert(data, priority)

    def insert(self, data, priority=0):
        """Test insert into pq."""
        if priority in self.queues:
            self.queues[priority].insert(0, data)
        else:
            self.queues[priority] = [data]

    def pop(self):
        """Test pop from pq."""
        for priority in sorted(self.queues):
            if len(self.queues[priority]) > 0:
                return self.queues[priority].pop()
        raise IndexError('Cannot pop from empty priority queue.')

    def peek(self):
        """Peek at the highest priority tuple."""
        for priority in sorted(self.queues):
            if len(self.queues[priority]) > 0:
                return self.queues[priority][-1]
