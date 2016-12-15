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
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    return queue


def test_init(new_queue):
    """Test initialization of empty queue."""
    assert new_queue.head is None and new_queue.tail is None


def test_pop_empty(new_queue):
    """Test to pop the head off from the node and return it."""
    with pytest.raises(IndexError):
        new_queue.pop()


def test_pop_length_one(new_queue):
    """Test pop on queue of length one."""
    new_queue.push(42)
    new_queue.pop()
    assert new_queue.head is None and new_queue.tail is None


def test_pop_length_one_return_val(new_queue):
    """Test pop return value."""
    new_queue.push(42)
    assert new_queue.pop() == 42
