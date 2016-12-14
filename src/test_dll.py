"""Testing dll.py."""
import pytest


@pytest.fixture
def new_dll():
    """Return empty dll."""
    from dll import DoublyLinkedList
    return DoublyLinkedList()


@pytest.fixture
def init_dll():
    """Return non empty dll."""
    from dll import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    return dll


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


def test_append_to_non_empty(new_dll):
    """Testing append to Node with value."""
    new_dll.append(3)
    new_dll.append(2)
    new_dll.append(1)
    assert new_dll.tail.val == 1
    assert new_dll.tail.prev.val == 2
    assert new_dll.tail.prev.next.val == 1
    assert new_dll.tail.prev.prev.val == 3


def test_pop_empty(new_dll):
    """Test to pop the head off from the node and return it."""
    with pytest.raises(IndexError):
        new_dll.pop()


def test_pop_length_one(new_dll):
    """Test pop on dll of length one."""
    new_dll.push(42)
    new_dll.pop()
    assert new_dll.head is None and new_dll.tail is None


def test_pop_length_one_return_val(new_dll):
    """Test pop return value."""
    new_dll.push(42)
    assert new_dll.pop() == 42


def test_push_twice(new_dll):
    """Test ability to push more than once."""
    new_dll.push("brandy")
    new_dll.push("chardonnay")
    assert new_dll.head.val == "chardonnay" and new_dll.tail.val == "brandy"


def test_push_multiple(init_dll):
    """Test ability to push more than once."""
    assert init_dll.head.val == 3
    assert init_dll.head.next.val == 2
    assert init_dll.head.next.next.val == init_dll.tail.val


def test_shift_from_empty(new_dll):
    """Test shift from empty raises exception."""
    with pytest.raises(IndexError):
        new_dll.shift()


def test_shift_on_one_long(new_dll):
    """Test shift on dll with length of one."""
    new_dll.push("spaghetti")
    new_dll.shift()
    assert new_dll.head is None and new_dll.tail is None


def test_shift_on_two_long(new_dll):
    """Test shift on dll with length of two."""
    new_dll.push(3)
    new_dll.push(4)
    new_dll.shift()
    assert new_dll.head.val == 4
    assert new_dll.tail is new_dll.head


def test_shift_on_more_than_two_long(init_dll):
    """Test shift on dll longer than one."""
    init_dll.shift()
    assert init_dll.tail.val == 2 and init_dll.head.val == 3


def test_remove(init_dll):
    """Remove node from dll."""
    init_dll.remove(2)
    assert init_dll.head.next.val == 1
    assert init_dll.tail.prev.val == 3

