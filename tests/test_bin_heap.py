"""Testing module for binary heap."""
import pytest
from random import sample, randint, choice
from collections import namedtuple
from data_structures import BinaryHeap


iters = [
    sample(range(100), randint(0, 100)) for _ in range(100)
]


Heap = namedtuple('Heap', (
    'heap',
    'iterable',
    'minmax')
)


@pytest.fixture
def empty_heap():
    """Return empty binary heap."""
    return BinaryHeap()


@pytest.fixture(params=iters)
def heap_fixture(request):
    """Return empty binary heap [1, 2, 4, 5, 3]."""
    iterable = request.param
    minmax = choice(['min', 'max'])
    heap = BinaryHeap(iterable, minmax)
    return Heap(heap, iterable, minmax)


def test_init_with_invalid_iterable():
    """Test Binary Heap init with invalid iterable."""
    with pytest.raises(TypeError, message="Optional binary heap argument must be iterable."):
        BinaryHeap(42)


def test_pop_from_empty_heap(empty_heap):
    """Test popping from empty heap."""
    with pytest.raises(IndexError, message='Cannot pop from an empty heap.'):
        empty_heap.pop()


def test_push_to_empty_heap(empty_heap):
    """Test pushing to empty heap."""
    num = randint(-100, 100)
    empty_heap.push(num)
    assert empty_heap._list == [num]


def test_push_pop_to_empty_heap_is_empty(empty_heap):
    """Test pushing to empty heap."""
    num = randint(-100, 100)
    empty_heap.push(num)
    empty_heap.pop()
    assert len(empty_heap._list) == 0


def test_pushes_all_values(heap_fixture):
    """Test Binary Heap pushes all items in the iterable."""
    assert sorted(heap_fixture.heap._list) == sorted(heap_fixture.iterable)


def test_pop_returns_minmax(heap_fixture):
    """Test popping from binary heap."""
    if len(heap_fixture.iterable) == 0:
        pytest.skip()
    minmax = {'min': min, 'max': max}[heap_fixture.minmax]
    assert heap_fixture.heap.pop() == minmax(heap_fixture.iterable)


def test_pop_removes_item(heap_fixture):
    """Test pop removes item from heap."""
    if len(heap_fixture.iterable) == 0:
        pytest.skip()
    popped = heap_fixture.heap.pop()
    assert popped not in heap_fixture.heap._list


def test_push_minmax_is_popped_first(heap_fixture):
    """Test pushing from binary heap."""
    new_root = {'min': -100, 'max': 100}[heap_fixture.minmax]
    heap_fixture.heap.push(new_root)
    assert heap_fixture.heap.pop() == new_root


def test_pops_in_order(heap_fixture):
    """Assert heap pops items in sorted order."""
    reverse = heap_fixture.minmax == 'max'
    heap = heap_fixture.heap
    popped = [heap.pop() for _ in range(len(heap._list))]
    assert popped == sorted(heap_fixture.iterable, reverse=reverse)


def test_swap_list():
    """Test the list after swap."""
    bin_hp = BinaryHeap([3, 1.5])
    assert bin_hp._list == [1.5, 3]
    bin_hp._swap(0, 1)
    assert bin_hp._list == [3, 1.5]
