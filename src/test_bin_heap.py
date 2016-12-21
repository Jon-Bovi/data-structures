"""Testing module for binary heap."""
import pytest


@pytest.fixture
def empty_bin_heap():
    """Return empty binary heap."""
    from bin_heap import BinaryHeap
    return BinaryHeap()


@pytest.fixture
def non_empty_bin_heap():
    """Return empty binary heap [1, 2, 4, 5, 3]."""
    from bin_heap import BinaryHeap
    return BinaryHeap([5, 1, 4, 2, 3])


def test_empty_init(empty_bin_heap):
    """Test Binary Heap init without iterable."""
    assert len(empty_bin_heap._list) == 0


def test_non_empty_init(non_empty_bin_heap):
    """Test Binary Heap init without iterable."""
    assert len(non_empty_bin_heap._list) == 5


def test_non_empty_init_values(non_empty_bin_heap):
    """Test Binary Heap init without iterable."""
    assert non_empty_bin_heap._list == [1, 2, 4, 5, 3]


def test_init_with_invalid_iterable():
    """Test Binary Heap init with invalid iterable."""
    from bin_heap import BinaryHeap
    with pytest.raises(TypeError, message="Optional binary heap argument must be iterable."):
        BinaryHeap(42)


def test_pop_from_non_empty_heap(non_empty_bin_heap):
    """Test popping from binary heap."""
    assert non_empty_bin_heap.pop() == 1


def test_push_from_non_empty_heap(non_empty_bin_heap):
    """Test pushing from binary heap."""
    non_empty_bin_heap.push(5)
    assert non_empty_bin_heap._list == [1, 2, 4, 5, 3, 5]


def test_pop_from_empty_heap(empty_bin_heap):
    """Test popping from empty heap."""
    with pytest.raises(IndexError, message='Cannot pop from an empty heap.'):
        empty_bin_heap.pop()


def test_push_to_empty_heap(empty_bin_heap):
    """Test pushing to empty heap."""
    empty_bin_heap.push(7)
    assert empty_bin_heap._list == [7]


def test_valid_heap_basic(non_empty_bin_heap):
    """Test heap function is ordering values correctly."""
    assert non_empty_bin_heap._list == [1, 2, 4, 5, 3]


def test_valid_heap_non_basic():
    """Test heap from more complex heap list."""
    from bin_heap import BinaryHeap
    bin_hp = BinaryHeap([1, 1.5, 3, 4, 2, 2.5, 6, 2, 8, 5.5, 3.5])
    assert bin_hp._list == [1, 1.5, 2.5, 2, 2, 3, 6, 4, 8, 5.5, 3.5]


def test_pop_heap():
    """Test heap function orders value correctly after pop."""
    from bin_heap import BinaryHeap
    bin_hp = BinaryHeap([1, 1.5, 3, 4, 2, 2.5, 6, 2, 8, 5.5, 3.5])
    bin_hp.pop()
    assert bin_hp._list == [1.5, 2, 2.5, 3.5, 2, 3, 6, 4, 8, 5.5]


def test_push_heap():
    """Test heap function orders value correctly after pop."""
    from bin_heap import BinaryHeap
    bin_hp = BinaryHeap([1.5, 1, 3, 4, 2, 2.5, 6, 2, 8, 5.5])
    bin_hp.push(3.5)
    assert bin_hp._list == [1, 1.5, 2.5, 2, 2, 3, 6, 4, 8, 5.5, 3.5]


def test_swap_parent_child():
    """Test the parent and child values after swap."""
    from bin_heap import BinaryHeap
    bin_hp = BinaryHeap([3, 1.5])
    assert bin_hp._list[0] == 1.5 and bin_hp._list[1] == 3
    bin_hp._swap(0, 1)
    assert bin_hp._list[1] == 1.5 and bin_hp._list[0] == 3


def test_swap_list():
    """Test the list after swap."""
    from bin_heap import BinaryHeap
    bin_hp = BinaryHeap([3, 1.5])
    assert bin_hp._list == [1.5, 3]
    bin_hp._swap(0, 1)
    assert bin_hp._list == [3, 1.5]


def test_max_option():
    """Test BinaryHeap with max heap option."""
    from bin_heap import BinaryHeap
    maxheap = BinaryHeap([1, 2, 3], 'max')
    assert maxheap._list == [3, 1, 2]


def test_max_pop():
    """Test pop on max heap."""
    from bin_heap import Binary_Heap
    maxheap = Binary_Heap([1, 2, 3], 'max')
    assert maxheap.pop() == 3


def test_organize_right():
    """Test organize right after pop."""
    from bin_heap import BinaryHeap
    bin_hp = BinaryHeap([12, 13, 9, 15, 16, 3, 5])
    bin_hp.pop()
    bin_hp._list == [5, 13, 3, 15, 16, 9]


def test_init_no_minmax():
    """Test for when optional paramater is not 'min' or 'max'."""
    from bin_heap import BinaryHeap
    with pytest.raises(ValueError, message="min/max optional parameter must be 'min' or 'max'"):
        BinaryHeap(1.5, "apple")
