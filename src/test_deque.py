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
    """."""
    assert new_deque._dll.head is None and new_deque._dll.tail is None
