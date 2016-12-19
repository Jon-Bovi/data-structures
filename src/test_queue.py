"""Testing the queue.py page."""
import pytest


@pytest.fixture
def new_queue():
    """Return empty queue."""
    from queue import Queue
    return Queue()


@pytest.fixture
def init_queue():
    """Return non empty queue."""
    from queue import Queue
    return Queue([1, 2, 3])


@pytest.fixture
def once_queue():
    """Return list of queues."""
    from queue import Queue
    q = Queue()
    q.enqueue("once")
    return q


def test_init(new_queue):
    """Test initialization of empty queue."""
    assert new_queue.head is None and new_queue._dll.tail is None


def test_enqueue_on_empty(new_queue):
    """Test enqueue on empty queue."""
    new_queue.enqueue(144)
    assert new_queue.head.val == 144 and new_queue._dll.tail.val == 144


def test_enqueue_on_queue_length_one(once_queue):
    """Test enqueue on queue of length one."""
    once_queue.enqueue(14)
    assert once_queue.head.val == "once" and once_queue._dll.tail.val == 14


def test_enqueue_on_non_empty(init_queue):
    """Test enqueue adds to tail of queue of length > 1."""
    init_queue.enqueue("bees")
    assert init_queue._dll.tail.val == "bees"


def test_dequeue_on_empty(new_queue):
    """Test dequeue raises error when called on empty queue."""
    with pytest.raises(IndexError):
        new_queue.dequeue()


def test_dequeue_length_one(once_queue):
    """Test dequeue on queue of length one."""
    once_queue.dequeue()
    assert once_queue.head is None and once_queue._dll.tail is None


def test_dequeue_length_one_return_val(once_queue):
    """Test pop return value."""
    once_queue.enqueue(42)
    assert once_queue.dequeue() == "once"


def test_dequeue_mult_length(init_queue):
    """Test dequeue on queue of length > 1."""
    init_queue.dequeue()
    assert init_queue.head.val == 2


def test_peek_on_empty_queue(new_queue):
    """Test peek returns None when called on empty queue."""
    assert new_queue.peek() is None


def test_size_on_empty(new_queue):
    """Test size of empty queue is zero."""
    assert new_queue.size() == 0


def test_size_on_non_empty(init_queue):
    """Test size returns proper size."""
    assert init_queue.size() == 3


def test_size(once_queue):
    """Test size of queue."""
    assert once_queue.size() == 1


def test_len_on_empty(new_queue):
    """Test len of empty queue is zero."""
    assert len(new_queue) == 0


def test_len_on_non_empty(init_queue):
    """Test len returns proper len."""
    assert len(init_queue) == 3


def test_len(once_queue):
    """Test len of queue."""
    assert len(once_queue) == 1


def test_clear(init_queue):
    """Test clear removes all nodes in queue."""
    nodes = []
    curr = init_queue.head
    while curr:
        nodes.append(curr)
        curr = curr.next
    init_queue.clear()
    assert len(nodes) == 0
