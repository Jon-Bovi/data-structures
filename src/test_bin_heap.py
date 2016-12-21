"""Testing module for binary heap."""
import pytest


@pytest.fixture
def empty_bin_heap():
    """Return empty binary heap."""
    from bin_heap import Binary_Heap
    return Binary_Heap()


@pytest.fixture
def non_empty_bin_heap():
    """Return empty binary heap."""
    from bin_heap import Binary_Heap
    return Binary_Heap([5, 1, 4, 2, 3])


def test_empty_init(empty_bin_heap):
    """Test Binary Heap init without iterable."""
    assert len(empty_bin_heap._list) == 0


def test_non_empty_init(non_empty_bin_heap):
    """Test Binary Heap init without iterable."""
    assert len(non_empty_bin_heap._list) == 5


def test_non_empty_init_values(non_empty_bin_heap):
    """Test Binary Heap init without iterable."""
    for idx, el in enumerate(non_empty_bin_heap._list):
        assert el == idx + 1


def test_init_with_invalid_iterable():
    """Test Binary Heap init with invalid iterable."""
    from bin_heap import Binary_Heap
    with pytest.raises(TypeError, message="Optional binary heap argument must be iterable."):
        Binary_Heap(42)


def test_pop_from_non_empty_heap(non_empty_bin_heap):
    """Test popping from binary heap."""
    assert non_empty_bin_heap.pop.val == 1


def test_push_from_non_empty_heap(non_empty_bin_heap):
    """Test pushing from binary heap."""
    non_empty_bin_heap.push(5)
    assert non_empty_bin_heap._list == [1, 2, 3, 4, 5, 5]


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
    assert non_empty_bin_heap._list == [1, 2, 3, 4, 5]


def test_valid_heap_non_basic():
    """Test heap from more complex heap list."""
    from bin_heap import Binary_Heap
    bin_hp = Binary_Heap([1, 1.5, 3, 4, 2, 2.5, 6, 2, 8, 5.5, 3.5])
    assert bin_hp._list == [1, 1.5, 2.5, 2, 2, 3, 6, 4, 8, 5.5, 3.5]


def test_pop_heap_():
    """Test heap function orders value correctly after pop."""
    from bin_heap import Binary_Heap
    bin_hp = Binary_Heap([1, 1.5, 3, 4, 2, 2.5, 6, 2, 8, 5.5, 3.5])
    bin_hp._list.pop()
    assert bin_hp._list == [1.5, 2, 2.5, 3.5, 2, 3, 6, 4, 8, 5.5]


def test_push_heap_():
    """Test heap function orders value correctly after pop."""
    from bin_heap import Binary_Heap
    bin_hp = Binary_Heap([1.5, 1, 3, 4, 2, 2.5, 6, 2, 8, 5.5])
    bin_hp._list.push(3.5)
    assert bin_hp._list == [1, 1.5, 2.5, 2, 2, 3, 6, 4, 8, 5.5, 3.5]
