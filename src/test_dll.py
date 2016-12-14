"""Testing dll.py."""
import pytest


@pytest.fixture
def new_dll():
    """Return empty dll."""
    from dll import DoublyLinkedList
    return DoublyLinkedList()


def test_init(new_dll):
    """Test initialization of empty doubly linked list."""
    assert new_dll.head is None and new_dll.tail is None

