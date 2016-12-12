"""Testing module for linked_list module."""
from linked_list import LinkedList
from linked_list import Node


LINKED_LIST = LinkedList()
LINKED_LIST.push(3)
LINKED_LIST.push("boomshakalaka")
LINKED_LIST.push(4)


def test_linked_list_init():
    """Test LinkedList class init method."""
    lst1 = LinkedList()
    assert lst1.head is None
    lst2 = LinkedList([1, 2, 3])
    assert lst2.head.val == 1
    assert lst2.head.next.val == 2
    assert lst2.head.next.next.val == 3


def test_node_init():
    """Test Node class init method."""
    node1 = Node(1, None)
    node2 = Node(2, node1)
    assert node1.val == 1
    assert node1.next is None
    assert node2.val == 2
    assert node2.next is node1


def test_linked_list_push():
    """Test linked list push method."""
    assert LINKED_LIST.head.val == 4
    assert LINKED_LIST.head.next.val == "boomshakalaka"
    assert LINKED_LIST.head.next.next.val == 3
    assert LINKED_LIST.head.next.next.next is None


def test_linked_list_pop():
    """Testing the pop method to return the head."""
    linked_lst = LinkedList()
    assert linked_lst.pop() is None


def test_linked_list_pop_first():
    """Testing the first variable in the pop method."""
    linked_lst = LinkedList()
    linked_lst.push(12)
    assert linked_lst.pop() == 12


def test_linked_list_size():
    """Test linked list size method."""
    assert LINKED_LIST.size() == 3


def test_empty_linked_list_size():
    """Test linked list size method for an empty linked list."""
    empty_list = LinkedList()
    assert empty_list.size() == 0


def test_linked_list_search():
    """Test linked list search method."""
    search_list = LinkedList([1, "boomshakalaka", 3])
    assert search_list.search('boomy') is None
    assert search_list.search(3).val == 3
    assert search_list.search(1).val == 1


def test_linked_list_remove():
    """Remove the given node from the list."""
    linked_lst = LinkedList([1, 2, 3])
    linked_lst.remove(linked_lst.head.next)
    assert linked_lst.head.next.val == 3
    linked_lst.remove(linked_lst.head)
    assert linked_lst.head.val == 3
