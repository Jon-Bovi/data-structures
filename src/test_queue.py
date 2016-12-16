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


def test_init(new_queue):
    """Test initialization of empty queue."""
    assert new_queue.head is None and new_queue.tail is None


def test_dequeue_length_one(new_queue):
    """Test dequeue on queue of length one."""
    new_queue.enqueue(42)
    new_queue.dequeue()
    assert new_queue.head is None and new_queue.tail is None


def test_pop_length_one_return_val(new_queue):
    """Test pop return value."""
    new_queue.enqueue(42)
    assert new_queue.dequeue() == 42
