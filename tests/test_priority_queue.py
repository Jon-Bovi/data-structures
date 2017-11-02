"""Testing module for priority queue."""

import pytest
from faker import Faker
from random import randint
from collections import namedtuple
from data_structures import PriorityQueue

fake = Faker()

PQ = namedtuple('PQ', (
    'pq',
    'init',
    'pop_order')
)

inits = [
    [(fake.word(), randint(0, 100)) for _ in range(randint(0, 40))]
    for _ in range(100)
]


@pytest.fixture(params=inits)
def pq_fixture(request):
    """Randomly filled priority queue."""
    init = request.param
    pq = PriorityQueue(init)
    pop_order = sorted(init, key=lambda t: t[1])
    return PQ(pq, init, pop_order)


@pytest.fixture
def empty_pq():
    """Return empty initialized PriorityQueue."""
    return PriorityQueue()


def test_pop_empty(empty_pq):
    """Test pop on empty pqueue raises IndexError."""
    with pytest.raises(IndexError, message="Cannot pop from an empty priority queue."):
        empty_pq.pop()


def test_peek_empty(empty_pq):
    """Test peek on empty pqueue raises IndexError."""
    with pytest.raises(IndexError, message="Cannot peek into an empty priority queue."):
        empty_pq.peek()


def test_pq_insert(empty_pq):
    """Test insert into empty pqueue."""
    empty_pq.insert('val', 1)
    assert empty_pq.pop() == ('val', 1)


def test_pq_insert_default_priority(empty_pq):
    """Assert insert without provided priority."""
    empty_pq.insert('mongo')
    assert empty_pq.peek() == ('mongo', 0)


def test_pq_iter_not_none():
    """Test insert into pq when iter is not None."""
    new_pq = PriorityQueue()
    new_pq.insert('kibble', 3)
    new_pq.insert('mix', 2)
    new_pq.insert('bits', 4)
    assert new_pq.pop() == ('mix', 2)


def test_pop_order(pq_fixture):
    """Test pop returns correct item."""
    pq = pq_fixture.pq
    popped = [pq.pop() for _ in range(pq._count)]
    assert popped == pq_fixture.pop_order


def test_peek(pq_fixture):
    """Test pop returns correct item."""
    if len(pq_fixture.init) == 0:
        pytest.skip()
    assert pq_fixture.pq.peek() == min(pq_fixture.init, key=lambda t: t[1])
