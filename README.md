# data-structures

Sample code (with tests) for classic data structures implemented in Python.

## Linked List

- Can be initialized with (or without) iterable argument: LinkedList(iterable=None)

- Module: linked_list

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

- Module: stack

- Attributes:

    - top: top/first node on stack

- Methods:

    - pop(): remove head and return its value

    - push(value): insert new node at head of list

    - size/len: return size of stack

## Doubly-Linked List

- Can be initialized with (or without) iterable argument: DoublyLinkedList(iterable=None)

- Module: dll

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

- Module: queue

- Methods:

    - enqueue(value): add value to end of queue

    - dequeue(): remove head of queue and return its value

    - peek(): return value of head of queue

    - len()/size(): return size of queue
    
## Deque (Double-Ended Queue)

- can be initialized with or without iterable argument

- Module: deque

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

- Module: bin_heap

- Optional arguments:
    
    - an iterable
    
    - minheap or maxheap ('min' or 'max') defaulted to 'min'

- Methods:
    
    - push(value): add value to bottom of heap and sort as needed
    
    - pop(value): remove first/root node and return its value, move last node to root, sort as needed


## Graph

- Module: graph

- Methods:

    - add_node(n): add node to graph

    - del_node(n): delete node from graph along with edges it's part of

    - add_edge(n1, n2): add a new edge to the graph connecting ‘n1’ to ‘n2’, if either
                n1 or n2 are not already present in the graph, they are added.

    - del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph,
                raises an error if no such edge exists

    - g.nodes(): return a list of all nodes in the graph

    - g.edges(): return a list of all edges in the graph

    - g.has_node(n): True if node ‘n’ is contained in the graph, False if not.

    - g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges,
                raises an error if n is not in graph

    - g.adjacent(n1, n2): returns if there is an edge connecting n1 and n2,
                raises an error if either of the supplied nodes are not in graph

    - g.depth_first_traversal(start): Traverses graph depth first starting from 'start',
                returns path

    - g.breadth_first_traversal(start): Traverses graph breadth first starting from 'start',
                returns path

    - g.depth_first_traversal_iterative(start): Traverses graph depth first starting from 'start',
                returns path, slower than recursive version

### Weighted Graph

- Module: weighted_graph

- Methods:

    - same as graph

    - g.add_edge(n1, n2, weight)


### Authors:
- Ford Fowler
- Sera Smith

### Coverage:

```

============================= test session starts ==============================
platform darwin -- Python 3.5.2, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
plugins: cov-2.4.0
collected 192 items

test_bin_heap.py ..................
test_deque.py .................
test_dll.py ........................
test_graph_traversal.py .............................
test_linked_list.py ...............
test_priority_queue.py .......
test_queue.py ..................
test_simple_graph.py .....................
test_stack.py .............
test_weighted_graph.py ..............................

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
bin_heap.py                  43      0   100%
deque.py                     30      0   100%
dll.py                       73      0   100%
graph.py                      0      0   100%
graph_traversal.py           81      0   100%
linked_list.py               64      0   100%
priority_queue.py            19      0   100%
queue.py                     28      0   100%
simple_graph.py              56      0   100%
stack.py                     21      0   100%
test_bin_heap.py             73      0   100%
test_deque.py                53      0   100%
test_dll.py                 103      0   100%
test_graph_traversal.py     118      0   100%
test_grph.py                  0      0   100%
test_linked_list.py          68      0   100%
test_priority_queue.py       32      0   100%
test_queue.py                64      0   100%
test_simple_graph.py         79      0   100%
test_stack.py                32      0   100%
test_weighted_graph.py      127      0   100%
weighted_graph.py            87      0   100%
-------------------------------------------------------
TOTAL                      1251      0   100%


========================== 192 passed in 0.85 seconds ==========================

```
