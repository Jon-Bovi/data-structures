"""Testing module for priority queue."""
import pytest


@pytest.fixture
def test_pq():
    from priority_queue import PriorityQueue
    return PriorityQueue()


def test_pq_init(test_pq):
    """Test priority queue init."""
    assert len(test_pq._heap._list) == 0


def test_pq_insert(test_pq):
    """Test insert into empty pqueue."""
    test_pq.insert((1, 'val'))
    assert len(test_pq._heap._list) == 0
