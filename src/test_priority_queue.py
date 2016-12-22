"""Testing module for priority queue."""
import pytest


@pytest.fixture
def empty_pq():
    """Return empty initialized PriorityQueue."""
    from priority_queue import PriorityQueue
    return PriorityQueue()


@pytest.fixture
def two_long_pq():
    """Return PriorityQueue of length two."""
    from priority_queue import PriorityQueue
    pq = PriorityQueue()
    pq.insert('value1', 3)
    pq.insert('value2', 1)
    return pq


@pytest.fixture
def long_pq():
    """Return an extensive priority queue."""
    from priority_queue import PriorityQueue
    return PriorityQueue([
        ('data1', 1),
        ('data2', 2),
        ('data3', 3),
        ('data4', 4),
        ('data5', 5),
        ('data6', 6),
        ('data7', 7),
        ('data8', 8),
        ('data9', 9),
        ('data10', 10),
    ])


def test_pq_init(empty_pq):
    """Test priority queue init."""
    assert len(empty_pq._heap._list) == 0


def test_pq_insert(empty_pq):
    """Test insert into empty pqueue."""
    empty_pq.insert('val', 1)
    assert len(empty_pq._heap._list) == 1


def test_pq_insert_default_priority(empty_pq):
    """Assert insert without provided priority."""
    empty_pq.push(34)
    assert


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
