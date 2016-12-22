"""Testing module for priority queue."""
import pytest


@pytest.fixture
def empty_pq():
    """Return empty initialized PriorityQueue."""
    from priority_queue import PriorityQueue
    return PriorityQueue()


@pytest.fixture
def long_pq():
    """Return an extensive priority queue."""
    from priority_queue import PriorityQueue
    return PriorityQueue([
        ('data5', 15),
        ('data8', 8),
        ('dataeight', 8),
        ('data4', 4),
        ('dataate', 8),
        ('data7', 9),
    ])


@pytest.fixture
def two_long_pq():
    """Return PriorityQueue of length two."""
    from priority_queue import PriorityQueue
    pq = PriorityQueue()
    pq.insert('value1', 3)
    pq.insert('value2', 1)
    return pq


def test_pq_init(empty_pq):
    """Test priority queue init."""
    assert len(empty_pq._heap._list) == 0


def test_pq_init_iterable(long_pq):
    """Assert items of same priority are still FIFO."""
    long_pq.pop()
    assert long_pq.pop() == ('data8', 8)
    assert long_pq.pop() == ('dataeight', 8)
    assert long_pq.pop() == ('dataate', 8)


def test_pq_insert(empty_pq):
    """Test insert into empty pqueue."""
    empty_pq.insert('val', 1)
    assert len(empty_pq._heap._list) == 1


def test_pq_insert_default_priority(empty_pq):
    """Assert insert without provided priority."""
    empty_pq.insert(34)
    assert empty_pq.peek()[0] == 34


def test_pq_double_insert(two_long_pq):
    """Test multiple inserts on pqueue."""
    assert len(two_long_pq._heap._list) == 2


def test_pop_empty(empty_pq):
    """Test pop on empty pqueue raises IndexError."""
    with pytest.raises(IndexError, message="Cannot pop from an empty priority queue."):
        empty_pq.pop()


def test_pop_non_empty(two_long_pq):
    """Test pop returns correct item."""
    assert two_long_pq.pop() == ('value2', 1)
