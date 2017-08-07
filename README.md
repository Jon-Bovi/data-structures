[![Build Status](https://travis-ci.org/fordf/data-structures.svg?branch=master)](https://travis-ci.org/fordf/data-structures)

# Data Structures

Implementations of classic data structures implemented in Python, with tests!


## Binary Tree

#### Module: `bst`

```python
BinaryTree(iterable=None, autobalance=True)
```
- iterable: iterable of items to insert
- autobalance: if True, tree will reorganize itself when needed to stay balance

#### Methods:

##### `insert(val)`
insert val into tree; if val already in tree, ignore

##### `search(val)`
return the node with a value of val; if not in tree return None

##### `contains(val)`
return whether val is in the tree

##### `delete(val)`
if val in tree, delete corresponding node; otherwise raise ValueError

##### `print(btree)`
print first five rows of tree formatted like ex_tree below

##### `display(btree)`
interactively move around and display tree


#### Traversals:

All traversal methods return generators,
and have the kwargs:

- start: traverse subtree starting at this node, defaults to root node.
- attr: attribute to yield from each node, defaults to 'val'.
        set to None to yield nodes themselves.

ex_tree:
```python
ex_tree = BinaryTree([17, 11, 24, 7, 14, 18, 25, 3, 8, 26])
print(ex_tree)

                                                 17
                        11                                                24
           7                        14                       18                       25
     3           8            _           _            _           _            _           26
```


##### `pre_order`
current -> left -> right (yields root first)
```python
list(ex_tree.pre_order())
[17, 11, 7, 3, 8, 14, 24, 18, 25, 26]
```

##### `post_order`
left -> right -> current (yields leftmost first)
```python
list(ex_tree.post_order())
[3, 8, 7, 14, 11, 18, 26, 25, 24, 17]
```

##### `in_order`
left -> current -> right (yields leftmost first)
```python
list(ex_tree.in_order())
[3, 7, 8, 11, 14, 17, 18, 24, 25, 26]
```

##### `breadth_first`
row by row, left to right
```python
list(ex_tree.breadth_first())
[17, 11, 24, 7, 14, 18, 25, 3, 8, 26]
```


## Trie

#### Module: `trie`

#### Operations:

```python
trie = Trie()

trie.insert('some string')

trie.contains('some string')
> True

trie.contains('other string')
> False

trie.size
> 1

trie.remove('some string')

trie.remove('some string')
> KeyError "some string" not in trie
```

```python
trie = Trie(['able', 'rough', 'robot', 'rogue', 'abrupt', 'aardvark', 'rodeo', 'rope', 'roost'])

trie.autocomplete('')
> ['able', 'abrupt', 'aardvark', 'rough', 'robot']

trie.autocomplete('ro', n=4)
> ['rough', 'robot', 'rogue', 'rodeo']
```


## Graph

#### Module: `graph`

```python
Graph()
```

#### Methods:

##### `add_node(n)`
add node to graph

##### `del_node(n)`
delete node from graph along with edges it's part of

##### `add_edge(n1, n2, weight=0)`
add a new edge to the graph connecting ‘n1’ to ‘n2’, if either
        n1 or n2 are not already present in the graph, they are added.

##### `del_edge(n1, n2)`
deletes the edge connecting ‘n1’ and ‘n2’ from the graph,
        raises an error if no such edge exists

##### `nodes()`
return a list of all nodes in the graph

##### `edges()`
return a list of all edges in the graph

##### `has_node(n)`
True if node ‘n’ is contained in the graph, False if not.

##### `neighbors(n)`
returns the list of all nodes connected to ‘n’,
        raises an error if n is not in graph

##### `adjacent(n1, n2)`
returns if there is an edge connecting n1 and n2,
        raises an error if either of the supplied nodes are not in graph

##### `depth_first_traversal(start)`
Traverses graph depth first starting from 'start',
        returns path

##### `breadth_first_traversal(start)`
Traverses graph breadth first starting from 'start',
        returns path

##### `depth_first_traversal_iterative(start)`
Traverses graph depth first starting from 'start',
        returns path, slower than recursive version

##### `dijkstra(start, end)`
return shortest path from start to end,
        implemented with dijkstra's algorithm.

##### `floyd_warshall()`
return path_dictionary, distance_dictionary for every
        possible path.

##### `floyd_warshall_path(path, start, end)`
return shortest path from start
        to end.


## Hash Table

#### Module: `hashtable`

```python
HashTable(size=1024, hash_func='additive')
```
- size: set fixed number of buckets in table
- hash_func:
        - 'additive': sum unicode number values of each character.
        - 'OAT'/'one-at-a-time': perform basic bitwise operations on individual characters and total accumulator.
        - 'FNV': multiply everything by big prime numbers.

#### Operations:

```python
htable = HashTable()

htable['key'] = 'value'

htable['key']
> 'value'

htable['key'] = 'diffvalue'

htable['key']
> 'diffvalue'

len(htable)
> 1

htable['notakey']
> KeyError
```

## Binary Heap

#### Module: `bin_heap`

```python
heap = BinaryHeap(iterable=None, minmax='min')
```

#### Methods:

##### `push(value)`
Add value to bottom of heap and sort as needed

##### `pop(value)`
Remove first/root node and return its value, move last node to root, sort as needed


## Stack

Can be initialized with (or without) iterable argument: Stack(iterable=None)

#### Module: `stack`

#### Methods:

##### `push(item)`
Add item to top of stack

##### `pop()`
Remove and return last pushed item


```python
stack = Stack()

stack.pop()
> Index Error 'Cannot pop from empty stack'

stack.push(4)
stack.push(2)

stack.pop()
> 2

len(stack)
> 1

stack = Stack([5, 4, 2, 99])
stack.pop()
> 99
```

## Queue

#### Module: `queue`

```python
Queue(iterable=None)
```

#### Methods:

##### `enqueue(value)`
add value to end of queue

##### `dequeue()`
remove head of queue and return its value

##### `peek()`
return value of head of queue

##### `len()/size()`
return size of queue


## Deque (Double-Ended Queue)

#### Module: `deque`

```python
Deque(iterable=None)
```

#### Methods:

##### `append(value)`
add value to end of deque

##### `appendleft(value)`
add value to front of deque

##### `pop()`
remove last item in deque and return its value

##### `popleft()`
remove first item in deque and return its value

##### `peek()`
return value of last item in deque

##### `peekleft()`
return value of first item in deque

##### `len(deque)`
return size of deque


## Priority Queue

#### Module: `priority_queue`

```python
PriorityQueue(iterable=None)
```

#### Methods:

##### `insert(data, priority=0)`
Enqueue data with priority (defaults to 0), lower is higher priority

##### `pop()`
Remove and return item of highest priority.
If multiple items of the same priority exist, pop item first inserted.

##### `peek()`
return value of next item to be popped

## Linked List

#### Module: `linked_list`

```python
LinkedList(iterable=None)
```

Attributes:

head: first node in linked list

Methods:

##### `pop()`
remove head and return its value

##### `push(value)`
insert new node at head of list

##### `remove(node)`
find and remove node from list

##### `search(value)`
find and return first node with value equal to argument

##### `display()`
print list in pseudo-tuple format

## Doubly-Linked List

#### Module: `dll`

```python
DoublyLinkedList(iterable=None)
```

Methods:

##### `push(value)`
insert value at head of list

##### `append(value)`
add value to tail of list

##### `pop()`
remove head and return its value

##### `shift()`
remove tail and return its value

##### `remove(val)`
remove first instance of value in list, or raise exception if no matches

Doubly-linked lists vs Singly-linked Lists:

    Singly-linked lists and doubly-linked lists each have their own unique advantages and 
    disadvantages. Singly-linked lists require less code and less memory as each node only
    has a value and a single pointer. This also makes them faster for both removing and inserting
    near the head node. Doubly-linked lists, however, allow more efficient reverse searches/traversal
    and for quicker appending/removal of new nodes near the tail of the list. And if you ever need
    to look back as you're traversing along the list, doubly-linked lists are easy while,
    with a singly-linked list, you either have to keep track of the node behind as you traverse,
    or you have to traverse all the way up to it from the head.



### Authors:
- Ford Fowler
- Sera Smith
- Claire Gatenby
- Marc Kessler-Wenicker
- Casey O'Kane

