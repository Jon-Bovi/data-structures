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


def test_push(new_dll):
    """Test push to empty dll."""
    new_dll.push(21)
    assert new_dll.head.val == 21 and new_dll.tail is None


def test_new_node(new_dll):
    """Test if new node is created."""
    from dll import DoubleNode
    node = DoubleNode(27)
    assert node.previous is None and node.next is None and node.val == (27)
