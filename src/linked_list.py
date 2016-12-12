class LinkedList(object):
    def __init__(self, head=None):
        self.head = head


class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
