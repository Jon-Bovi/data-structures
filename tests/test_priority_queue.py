"""Testing module for priority queue."""

import pytest

from data_structures import PriorityQueue


@pytest.fixture
def empty_pq():
    """Return empty initialized PriorityQueue."""
    return PriorityQueue()


def test_pq_init(empty_pq):
    """Test priority queue init."""
    assert empty_pq is not None


def test_pq_iter_not_none():
    """Test insert into pq when iter is not None."""
    new_pq = PriorityQueue([('kibble', 3)])
    new_pq.insert('mix', 2)
    assert new_pq.pop() == 'mix'


def test_pq_insert(empty_pq):
    """Test insert into empty pqueue."""
    empty_pq.insert('val', 1)
    assert empty_pq.pop() == 'val'


def test_pq_insert_default_priority(empty_pq):
    """Assert insert without provided priority."""
    empty_pq.insert('mongo')
    assert empty_pq.peek() == 'mongo'


def test_pop_empty(empty_pq):
    """Test pop on empty pqueue raises IndexError."""
    with pytest.raises(IndexError, message="Cannot pop from an empty priority queue."):
        empty_pq.pop()


def test_pop_non_empty(empty_pq):
    """Test pop returns correct item."""
    empty_pq.insert('mix', 2)
    empty_pq.insert('meow', 1)
    assert empty_pq.pop() == 'meow'
    assert empty_pq.pop() == 'mix'


def test_pop_insert_pq():
    """Test insert to pq."""
    pq = PriorityQueue()
    pq.insert('mix', 2)
    pq.insert('meow', 2)
    assert pq.pop() == "mix"
    assert pq.pop() == "meow"
