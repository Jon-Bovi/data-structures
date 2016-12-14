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


def test_push_to_empty(new_dll):
    """Test push to empty dll."""
    new_dll.push(21)
    assert new_dll.head.val == 21 and new_dll.head.next is None


def test_new_node(new_dll):
    """Test if new node is created."""
    from dll import DoubleNode
    node = DoubleNode(27)
    assert node.prev is None and node.next is None and node.val == 27


def test_new_node_optional(new_dll):
    """Testing optional parameters on the newly created node."""
    from dll import DoubleNode
    node2 = DoubleNode(10)
    node3 = DoubleNode(11)
    node1 = DoubleNode(17, node2, node3)
    assert node1.prev is node2 and node1.next is node3


def test_append(new_dll):
    """Testing the append function to add to the tail of the node."""
    new_dll.append('11')
    assert new_dll.tail.val == "11"
