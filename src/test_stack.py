"""Testing module for Stack class."""
import pytest


@pytest.fixture
def new_stack():
    """Empty stack instance fixture."""
    from stack import Stack
    return Stack()


@pytest.fixture
def initialized_stack():
    """Empty stack instance fixture."""
    from stack import Stack
    return Stack([42, "ramshackle", "discombobulate"])


ITERABLES = [
    [[1, 2, 4], 4],
    [(1, 2, 4), 4],
    ["124", '4'],
]


def test_empty_stack_init_top(new_stack):
    """Test initialization of Stack without optional iterable."""
    assert new_stack.top is None


def test_empty_stack_init_size(new_stack):
    """Test initialization of Stack without optional iterable."""
    assert new_stack.size() == 0


def test_stack_push(new_stack):
    """Test stack push method."""
    new_stack.push(3)
    assert new_stack.top.val == 3


@pytest.mark.parametrize("iterable, top_val", ITERABLES)
def test_initialized_stack_init_top(iterable, top_val):
    """Test initialization of Stack with optional iterable."""
    from stack import Stack
    init_stack = Stack(iterable)
    assert init_stack.top.val == top_val


@pytest.mark.parametrize("iterable, top_val", ITERABLES)
def test_initialized_stack_init_size(iterable, top_val):
    """Test initialization of Stack with optional iterable."""
    from stack import Stack
    init_stack = Stack(iterable)
    assert init_stack.size() == 3


def test_stack_pop(initialized_stack):
    """Test pop returns old top value."""
    assert initialized_stack.pop() == "discombobulate"


def test_len_empty(new_stack):
    """Test __len__ method on empty stack."""
    assert len(new_stack) == 0


def test_len_ll(initialized_stack):
    """Test __len__ method on non empty stack."""
    assert len(initialized_stack) == 3
