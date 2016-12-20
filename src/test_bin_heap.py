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
