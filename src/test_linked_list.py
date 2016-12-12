"""Testing module for linked_list module."""
from linked_list import LinkedList


def test_linked_list_push():
    """Test linked list push method."""
    linked_lst = LinkedList()
    linked_lst.push(3)
    linked_lst.push("boomshakalaka")
    assert linked_lst.head.val == "boomshakalaka"
    assert linked_lst.head.next.val == 3
    assert linked_lst.head.next.next is None
