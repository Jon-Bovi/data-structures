"""Testing module for linked_list module."""

import pytest

from data_structures.linked_list import Node, LinkedList


@pytest.fixture
def new_list():
    """Empty linked-list fixture."""
    return LinkedList()


@pytest.fixture
def initialized_list():
    """Non-empty linked-list fixture."""
    return LinkedList([3, "boomshakalaka", 4])


def test_linked_list_init(new_list, initialized_list):
    """Test LinkedList class init method."""
    assert new_list.head is None
    ll = initialized_list
    assert ll.head.val == 4
    assert ll.head.next.val == "boomshakalaka"
    assert ll.head.next.next.val == 3


def test_node_init():
    """Test Node class init method."""
    node1 = Node(1)
    node2 = Node(2, node1)
    assert node1.val == 1
    assert node1.next is None
    assert node2.val == 2
    assert node2.next is node1


def test_linked_list_push(initialized_list):
    """Test linked list push method."""
    ll = initialized_list
    assert ll.head.val == 4
    assert ll.head.next.val == "boomshakalaka"
    assert ll.head.next.next.val == 3
    assert ll.head.next.next.next is None


def test_linked_list_pop(new_list):
    """Testing the pop method to return the head."""
    with pytest.raises(IndexError):
        new_list.pop()


def test_linked_list_pop_first(new_list):
    """Testing the first variable in the pop method."""
    ll = new_list
    ll.push(12)
    assert ll.pop() == 12


def test_linked_list_size(initialized_list):
    """Test linked list size method."""
    assert initialized_list.size() == 3


def test_empty_linked_list_size(new_list):
    """Test linked list size method for an empty linked list."""
    assert new_list.size() == 0


def test_linked_list_search(initialized_list):
    """Test linked list search method."""
    search_list = initialized_list
    assert search_list.search('boomy') is None
    assert search_list.search(3).val == 3
    assert search_list.search(4).val == 4


def test_linked_list_remove():
    """Remove the given node from the list."""
    linked_lst = LinkedList([1, 2, 3])
    linked_lst.remove(linked_lst.head.next)
    assert linked_lst.head.next.val == 1
    linked_lst.remove(linked_lst.head)
    assert linked_lst.head.val == 1


def test_remove_non_node(initialized_list):
    """Test remove raises error when called with non-node."""
    with pytest.raises(ValueError):
        initialized_list.remove(4)


def test_remove_not_in_list(initialized_list):
    """Test remove raises error when node to be removed is not in list."""
    with pytest.raises(ValueError):
        n = Node(33)
        initialized_list.remove(n)


def test_linked_list_display(new_list, initialized_list):
    """Test display method."""
    assert new_list.display() == "()"
    assert initialized_list.display() == "(4, 'boomshakalaka', 3)"


def test_empty_linked_list_len(new_list):
    """Test empty linked list has length of 0."""
    assert len(new_list) == 0


def test_linked_list_len(initialized_list):
    """Test empty linked list has length of 0."""
    assert len(initialized_list) == 3


def test_repr(new_list, initialized_list):
    """Test repr displays list properly."""
    assert repr(new_list) == "()"
    assert repr(initialized_list) == "(4, 'boomshakalaka', 3)"
