"""Tests for deque module."""

import pytest


@pytest.fixture
def new_deque():
    """Return empty deque."""
    from deque import Deque
    return Deque()


@pytest.fixture
def initialized_deque():
    """Return non empty deque."""
    from deque import Deque
    return Deque([3, 2, 1])


def test_init(new_deque):
    """Test initialization of empty deque."""
    assert new_deque.head is None and new_deque.tail is None


def test_append_on_empty(new_deque):
    """Test append on empty deque."""
    new_deque.append('wut')
    assert new_deque.head.val == 'wut' and new_deque.tail.val == 'wut'


def test_appendleft_on_empty(new_deque):
    """Test appendleft on empty deque."""
    new_deque.appendleft('wat')
    assert new_deque.head.val == 'wat' and new_deque.tail.val == 'wat'


def test_append_on_non_empty(initialized_deque):
    """Test append adds to the tail and prev tail points to new tail."""
    initialized_deque.append('ok')
    assert initialized_deque.tail.val == 'ok' and initialized_deque.tail.prev.val == 3


def test_appendleft_on_non_empty(initialized_deque):
    """Test appendleft adds value to head of deque and new head points to prev head."""
    initialized_deque.appendleft(45)
    assert initialized_deque.head.val == 45 and initialized_deque.head.next.val == 1


def test_pop_on_empty(new_deque):
    """Test pop raises exception when called on empty deque."""
    with pytest.raises(IndexError, message='Cannot pop from an empty deque.'):
        new_deque.pop()


def test_popleft_on_empty(new_deque):
    """Test pop raises exception when called on empty deque."""
    with pytest.raises(IndexError, message='Cannot pop from an empty deque.'):
        new_deque.popleft()


def test_pop_changes_deque(initialized_deque):
    """Test pop removes end of deque and decreases size."""
    initialized_deque.pop()
    assert initialized_deque.tail.val == 2 and initialized_deque.size() == 2


def test_popleft_changes_deque(initialized_deque):
    """Test popleft removes front of deque and decreases size."""
    initialized_deque.popleft()
    assert initialized_deque.head.val == 2 and initialized_deque.size() == 2


def test_pop_on_non_empty_return_value(initialized_deque):
    """Test pop on non empty deque."""
    assert initialized_deque.pop() == 3


def test_popleft_on_non_empty_return_value(initialized_deque):
    """Test pop on non empty deque."""
    assert initialized_deque.popleft() == 1


def test_popboth(initialized_deque):
    """Test pop and popleft."""
    initialized_deque.pop()
    initialized_deque.popleft()
    assert initialized_deque.head.val == 2 and initialized_deque.tail.val == 2
    assert initialized_deque.head is initialized_deque.tail
    assert initialized_deque.size() == 1


def test_peek(initialized_deque):
    """Test return of last value a deque."""
    assert initialized_deque.peek() == 3


def test_peekleft(initialized_deque):
    """Test return of first value of deque."""
    assert initialized_deque.peekleft() == 1


def test_peek_empty(new_deque):
    """Test peek of empty deque returns None."""
    assert new_deque.peek() is None


def test_peekleft_empty(new_deque):
    """Test peekleft of empty deque returns None."""
    assert new_deque.peekleft() is None


def test_len(initialized_deque):
    """Test to return length of deque."""
    return len(initialized_deque) == 3
