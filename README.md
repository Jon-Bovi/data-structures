# data-structures

Sample code (with tests) for classic data structures implemented in Python.

## Linked List

- Can be initialized with (or without) iterable argument: LinkedList(iterable=None)

- Attributes:

    - head: first node in linked list

- Methods:

    - pop(): remove head and return its value

    - push(value): insert new node at head of list

    - remove(node): find and remove node from list

    - search(value): find and return first node with value equal to argument

    - display(): print list in pseudo-tuple format

## Stack

- Can be initialized with (or without) iterable argument: Stack(iterable=None)

- Attributes:

    - top: top/first node on stack

- Methods:

    - pop(): remove head and return its value

    - push(value): insert new node at head of list

    - size/len: return size of stack

## Doubly-Linked List

- Can be initialized with (or without) iterable argument: DoublyLinkedList(iterable=None)

- Methods:

    - push(value): insert value at head of list

    - append(value): add value to tail of list

    - pop(): remove head and return its value

    - shift(): remove tail and return its value

    - remove(val): remove first instance of value in list, or raise exception if no matches

Doubly-linked lists vs Singly-linked Lists:

    Singly-linked lists and doubly-linked lists each have their own unique advantages and 
    disadvantages. Singly-linked lists require less code and less memory as each node only
    has a value and a single pointer. This also makes them faster for both removing and inserting
    near the head node. Doubly-linked lists, however, allow more efficient reverse searches/traversal
    and for quicker appending/removal of new nodes near the tail of the list. And if you ever need
    to look back as you're traversing along the list, doubly-linked lists are easy while,
    with a singly-linked list, you either have to keep track of the node behind as you traverse,
    or you have to traverse all the way up to it from the head.

## Queue

- can be initialized with (or without) iterable argument: Queue(iterable=None)

- Methods:

    - enqueue(value): add value to end of queue

    - dequeue(): remove head of queue and return its value

    - peek(): return value of head of queue

    - len()/size(): return size of queue
    
## Deque (Double-Ended Queue)

- can be initialized with or without iterable argument

- Attributes:

    - head
    
    - tail

- Methods:
    
    - append(value): add value to end of deque
    
    - appendleft(value): add value to front of deque
    
    - pop(): remove last item in deque and return its value
    
    - popleft(): remove first item in deque and return its value
    
    - peek(): return value of last item in deque
    
    - peekleft(): return value of first item in deque
    
    - len(deque) / deque.size(): return size of deque
    
## Binary Heap

- Optional arguments:
    
    - an iterable
    
    - minheap or maxheap ('min' or 'max') defaulted to 'min'

- Methods:
    
    - push(value): add value to bottom of heap and sort as needed
    
    - pop(value): remove first/root node and return its value, move last node to root, sort as needed
    
### Authors:
- Ford Fowler
- Sera Smith

### Coverage:

```

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
src/bin_heap.py              44      0   100%
src/deque.py                 30      0   100%
src/dll.py                   73      0   100%
src/linked_list.py           58      0   100%
src/queue.py                 26      5    81%   12-13, 37-39
src/stack.py                 21      0   100%
src/test_bin_heap.py         73      0   100%
src/test_deque.py            53      0   100%
src/test_dll.py             103      0   100%
src/test_linked_list.py      57      0   100%
src/test_queue.py            49      0   100%
src/test_stack.py            32      0   100%
-------------------------------------------------------
TOTAL                       619      5    99%

```
