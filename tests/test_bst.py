"""Test for binary search tree data structures."""

import pytest
import random
from collections import namedtuple

from data_structures.bst import BinaryTree, BinaryTreeNode

"""
Tests:

Node:
- attrs set properly under all circumstances: init, insert, delete, rotation

Tree:
- Size accurate under all circumstances: init, insert, insert already exists, delete, delete nonexist
- insert: location, when already exists
- search: finds existent, nonexistent returns None, O(logn)
- contains: exists, doesnt
- delete:
"""

TEST_BST1 = [1, 3, 5, 4, 9, 8, 12, 11]
"""
BALANCED
                                                 5
                        3                                                 9
           1                        4                        8                        12
     _           _            _           _            _           _            11          _

UNBALANCED

                                               1
                       _                                               3
           _                       _                       _                       5
     _           _           _           _           _           _           4           9
  _     _     _     _     _     _     _     _     _     _     _     _     _     _     8     12
"""
TEST_BST2 = [11, 6, 8, 19, 4, 12, 5, 17, 43, 49, 31]
"""
BALANCED
                                               8
                       5                                               19
           4                       6                       12                      43
     _           _           _           _           11          17          31          49

UNBALANCED
                                               11
                       6                                               19
           4                       8                       12                      43
     _           5           _           _           _           17          31          49
"""

TEST_INSERTIONS = [
    [],
    [0],
    [1, 0],
    [0, 1],
    range(10),
    range(10, 0, -1),
    TEST_BST1,
    TEST_BST2,
] + [random.sample(range(-100,100), random.randrange(30)) for i in range(30)]


def insertions():
    for inserts in zip(TEST_INSERTIONS, [True, False] * (len(TEST_INSERTIONS) // 2)):
        yield inserts


BinaryTreeFixture = namedtuple(
    'BinaryTreeFixture', (
        'tree',
        'sequence',
        'size',
        # 'depth',
        # 'balance',
        # 'left_overbalance',
        # 'right_overbalance',
        # 'to_insert',
        # 'to_delete',
        # 'contains_after_delete',
        # # 'depth_after_delete',
        # # 'balance_after_delete',
        # 'size_after_delete',
    )
)


@pytest.fixture(params=insertions())
def binarytree(request):
    sequence, balancing = request.param
    tree = BinaryTree()
    size = len(set(sequence))

    return BinaryTreeFixture(
        tree,
        sequence,
        size,
    )


# @pytest.fixture
# def bst_one_node():
#     """Return bst with one node with val of 11."""
#     new_bst = BinaryTree(TEST_BST1[-1],autobalance=False)
#     return new_bst


# @pytest.fixture
# def bst1():
#     """Return bst filled with nodes."""
#     new_bst = BinaryTree(TEST_BST1,autobalance=False)
#     return new_bst


# @pytest.fixture
# def bst2():
#     """Return bst filled with more nodes."""
#     new_bst = BinaryTree(TEST_BST2,autobalance=False)
#     return new_bst


# def test_insert_at_end_of_tree(bst1):
#     """Test insert node at end of tree."""
#     bst1.insert(7)
#     new_node = bst1.search(7)
#     assert bst1.contains(7)
#     assert new_node.parent.val == 8
#     assert new_node.is_leaf()


# def test_insert_node_at_root(empty_bst):
#     """Test insert node at root."""
#     empty_bst.insert(10)
#     assert empty_bst.root.val == 10
#     assert empty_bst.root.is_leaf()
#     assert empty_bst.depth() == 1


# def test_insert_existing_node(bst2):
#     """Test inserting a node that already exists."""
#     cur_size = bst2.size()
#     bst2.insert(8)
#     assert cur_size == bst2.size()


# def test_tree_is_empty(empty_bst):
#     """Test size of an empty tree is equal to 0."""
#     assert empty_bst.size() == 0


# def test_contains_returns_false(empty_bst):
#     """Test that contains return False if node is not found."""
#     assert empty_bst.contains(1) is False


# def test_size_is_increased_when_initialized_w_one_node(bst_one_node):
#     """Test that size is increased when initialized with one node."""
#     assert bst_one_node.size() == 1


# def test_size_is_equal_to_iterable(bst1):
#     """Test that size is increased correctly when initialized with an iterable."""
#     assert bst1.size() == len(TEST_BST1)


# def test_size_is_increased_when_adding_nodes(bst2):
#     """Test that size is increased correctly when removing a node."""
#     add = random.sample(range(1000), random.randint(0,100))
#     for n in add:
#         bst2.insert(n)
#     assert bst2.size() == len(set(TEST_BST2) | set(add))


# def test_depth_returns_correct_val(s, result, bst2):
#     """Test depth returns correct val in a full tree."""
#     bst2.insert(s)
#     assert bst2.depth(bst2.search(s)) == result


# def test_balance_returns_correct_val(s, result):
#     """Test balance returns correct val in a full tree."""
#     b = BinaryTree(s, autobalance=False)
#     assert b.balance() == result


# def test_balance_called_with_none_returns_zero(empty_bst):
#     """Test balance returns zero."""
#     assert empty_bst.balance(None) == 0


# TEST_BST1 = [2, 1, 3, 5, 4, 9, 8, 12, 11]
# TEST_BST2 = [11, 6, 8, 19, 4, 12, 5, 17, 43, 49, 31]


# @pytest.fixture
# def bst3():
#     """Return an bst with some nodes."""
#     new_bst = BinaryTree(TEST_BST1,autobalance=False)
#     return new_bst


# @pytest.fixture
# def bst4():
#     """Return an bst with some other nodes."""
#     new_bst = BinaryTree(TEST_BST2,autobalance=False)
#     return new_bst


# def test_in_order_on_empty(empty_bst):
#     """Test in order traversal of empty bst returns empty generator."""
#     assert list(empty_bst.in_order()) == []


# def test_pre_order_on_empty(empty_bst):
#     """Test pre order traversal of empty bst returns empty generator."""
#     assert list(empty_bst.pre_order()) == []


# def test_post_order_on_empty(empty_bst):
#     """Test post order traversal of empty bst returns empty generator."""
#     assert list(empty_bst.post_order()) == []


# def test_breadth_first_on_empty(empty_bst):
#     """Test breadth first traversal of empty bst returns empty generator."""
#     assert list(empty_bst.breadth_first()) == []


# # def test_in_order_returns_generator(bst3):
# #     """Test in order traversal returns a generator."""
# #     assert isinstance(bst3.in_order(), types.GeneratorType)


# # def test_pre_order_returns_generator(bst3):
# #     """Test pre order traversal returns a generator."""
# #     assert isinstance(bst3.pre_order(), types.GeneratorType)


# # def test_post_order_returns_generator(bst3):
# #     """Test post order traversal returns a generator."""
# #     assert isinstance(bst3.post_order(), types.GeneratorType)


# # def test_breadth_first_returns_generator(bst3):
# #     """Test breadth first traversal returns a generator."""
# #     assert isinstance(bst3.breadth_first(), types.GeneratorType)


# def test_in_order_bst3(bst3):
#     """Test in order traversal returns nodes in order."""
#     assert list(bst3.in_order()) == [1, 2, 3, 4, 5, 8, 9, 11, 12]


# def test_in_order_bst4(bst4):
#     """Test in order traversal returns nodes in order."""
#     assert list(bst4.in_order()) == [4, 5, 6, 8, 11, 12, 17, 19, 31, 43, 49]


# def test_pre_order_bst3(bst3):
#     """Test pre order traversal does a depth first traversal."""
#     assert list(bst3.pre_order()) == [2, 1, 3, 5, 4, 9, 8, 12, 11]


# def test_pre_order_bst4(bst4):
#     """Test pre order traversal does a depth first traversal on complex bst."""
#     assert list(bst4.pre_order()) == [11, 6, 4, 5, 8, 19, 12, 17, 43, 31, 49]


# def test_post_order_bst3(bst3):
#     """Test post order traversal does its thang."""
#     assert list(bst3.post_order()) == [1, 4, 8, 11, 12, 9, 5, 3, 2]


# def test_post_order_bst4(bst4):
#     """Test post order on more complex bst."""
#     assert list(bst4.post_order()) == [5, 4, 8, 6, 17, 12, 31, 49, 43, 19, 11]


# def test_breadth_first_bst3(bst3):
#     """Test breadth first traversal of bst."""
#     assert list(bst3.breadth_first()) == [2, 1, 3, 5, 4, 9, 8, 12, 11]


# def test_breadth_first_bst4(bst4):
#     """Test breadth first traversal of bst."""
#     assert list(bst4.breadth_first()) == [11, 6, 19, 4, 8, 12, 43, 5, 17, 31, 49]


# BALANCED = [50, 30, 70, 20, 40, 80, 60, 65, 75, 85, 34, 33, 36, 29, 41]
# TEST_DEEP = [19, 17, 24, 88, 25, 59, 49, 87, 79, 65, 74]
# PROBLEMATIC = [60, 34, 80, 12, 40, 73, 89, 5, 23, 38, 47, 65, 76, 86, 94, 3, 9, 13, 30, 37, 39, 42, 50, 62, 72, 75, 79, 83, 88, 91, 96, 2, 4, 18, 25, 41]
# BAD = [425, 314, 649, 244, 362, 593, 751, 216, 319, 369, 505, 615, 682, 816, 370, 572, 670, 739, 801, 891, 773, 881]


# @pytest.fixture
# def balanced_avl():
#     """Return balanced avl."""
#     new_avl = BinaryTree(BALANCED)
#     return new_avl


# @pytest.fixture(params=[BALANCED, TEST_DEEP, PROBLEMATIC, BAD])
# def diff_avl(request):
#     """Return balanced avl."""
#     new_avl = BinaryTree(request.param)
#     return new_avl, request.param


# @pytest.fixture
# def random_avl():
#     """Return large random avl."""
#     import random
#     rando_avl = BinaryTree()
#     for i in range(200):
#         rando_avl.insert(random.randint(0, 100))
#     return rando_avl


# RANDOM = random_avl()


# def test_init_non_iterable():
#     """If non iterable is passed to init, it should insert non iterable."""
#     avl = BinaryTree(5)
#     assert avl.root.val == 5


# def test_check_balance_balanced_returns_none(balanced_avl):
#     """Check balanced on balanced tree should return None."""
#     for node in balanced_avl:
#         assert balanced_avl._check_balance(node) is None


# def test_check_balance_unbalanced_returns_unbalanced_subtree_root(balanced_avl):
#     """Check balance should return root of unbalanced subtree."""
#     from bst import Node
#     node = balanced_avl.search(36)
#     node.left = Node(35, parent=node)
#     node.left.left = Node(34.4, parent=node.left)
#     assert balanced_avl._check_balance(node.left.left).val == 36


# def test_rebalance_left_rotation():
#     """Test all the connections after a left rotation rebalance."""
#     lefty = BinaryTree([1, 4, 8], autobalance=False)
#     lefty.rebalance(lefty.root)
#     assert lefty.root.val == 4
#     children = lefty.root.children()
#     assert [c.val for c in children] == [1, 8]
#     for child in children:
#         assert child.parent is lefty.root


# def test_rebalance_right_rotation():
#     """Test all the connections after a right rotation rebalance."""
#     righty = BinaryTree([8, 4, 1], autobalance=False)
#     righty.rebalance(righty.root)
#     assert righty.root.val == 4
#     children = righty.root.children()
#     assert [c.val for c in children] == [1, 8]
#     for child in children:
#         assert child.parent is righty.root


# def test_rebalance_right_left_rotation():
#     """Test all the connections after a right rotation rebalance."""
#     refty = BinaryTree([1, 8, 4], autobalance=False)
#     refty.rebalance(refty.root)
#     assert refty.root.val == 4
#     children = refty.root.children()
#     assert [c.val for c in children] == [1, 8]
#     for child in children:
#         assert child.parent is refty.root


# def test_rebalance_left_right_rotation():
#     """Test all the connections after a right rotation rebalance."""
#     lighty = BinaryTree([8, 1, 4], autobalance=False)
#     lighty.rebalance(lighty.root)
#     assert lighty.root.val == 4
#     children = lighty.root.children()
#     assert [c.val for c in children] == [1, 8]
#     for child in children:
#         assert child.parent is lighty.root


# def test_auto_balance_on_insertion(diff_avl):
#     """Test auto balancing on large random trees."""
#     avl, values = diff_avl
#     nodes = avl.pre_order()
#     for node in nodes:
#         assert abs(avl.balance(avl.search(node))) <= 1


# def test_auto_balance_on_insertion_random_tree(random_avl):
#     """Test auto balancing on large random trees."""
#     nodes = random_avl.pre_order()
#     for node in nodes:
#         assert abs(random_avl.balance(random_avl.search(node))) <= 1


# @pytest.mark.parametrize('value', list(RANDOM.pre_order()))
# def test_rebalance_after_delete_random_tree(value):
#     """Test avl rebalances after deletions."""
#     RANDOM.delete(value)
#     nodes = RANDOM.pre_order()
#     assert all(RANDOM.search(node).balance() <= 1 for node in nodes)
#     # for node in nodes:
#     #     actual_node = RANDOM.search(node)
#     #     assert abs(RANDOM.balance(actual_node)) <= 1


# def test_rebalance_after_delete_for_deep(diff_avl):
#     """Test avl rebalances after deletions."""
#     avl, values = diff_avl
#     nodes = avl.pre_order()
#     for node in nodes:
#         actual_node = avl.search(node)
#         for value in values:
#             if value != node:
#                 avl.delete(value)
#                 assert abs(avl.balance(actual_node)) <= 1
