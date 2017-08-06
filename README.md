[![Build Status](https://travis-ci.org/fordf/data-structures.svg?branch=decision-tree)](https://travis-ci.org/fordf/data-structures)

# Machine Learning

### Supervised Classifiers

## Decision Tree Classifier

- Version: 0.0.0.0.1

#### Operations
 ```python
 from decision_tree import DecisionTree 
 
dtree = DecisionTree(min_leaf_size=1, max_depth=3)
 ```
 ```python
dtree.fit(dataset, classes)
```
Build a decision tree off of data.
```python
predict(dataset)
```
Predict class values for unclassified dataset, using prebuilt tree.
```python
cross_validate(dataset, classes)
```
Splits a classified dataset in two, one to build the decision tree, the other to predict with. Returns the percentage of predicted labels that match actual labels.


## K-Nearest Neighbors (Knn) Classifier:

The [K-Nearest Neigbours algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) seeks to categorize new data based on the known labels of the K closest data points.
The classifer needs not be fit, it directly compares the unlabeled data against the labeled training data.

Implemented with: numpy

#### Operations

```python
from knn import Knn
knn = Knn(dataset, k=5)
knn.predict(predict_data, labeled_data, k=5, label_col=-1)
```
Predict the classes of unlabeled data by comparison to labeled_data.
- predict_data: data to be labeled
- labeled_data
- k: how many neighbors to group with
- label_col: labeled_data, col index containing labels


### Unsupervised Classifiers

## K-Means Clustering

- Module: k_means

- Initialize:
    - ```python
    clf = KMeansClassifier(max_iter=None, min_step='auto')
    ```
        - max_iter: The number of iterations before the algorithm stops
        - min_step: The smallest difference in distance between an old centroid
                  and a new centroid before the algorithm stops. If 'auto',
                  min_step is calculated to be 1/1000th of largest first step.

- Methods:
    - ```python
    clf.fit(data, k=None, init_centroids=None)
    ```
    Find centroids of clusters.
        - data: 2d numpy array

        k or init_centroids required
        - k: number of centroids to randomly initialize
        - init_centroids: starting locations of centroids

clf.predict(data)
"""Return predicted classes for given data."""

clf.cross_validate(data, k=None, init_centroids=None, train_split=.7, label_col=-1):
"""
Split a labeled dataset in two, fit on one, predict the other.
    - data: 2d numpy array

    k or init_centroids required
    - k: number of centroids to randomly initialize
    - init_centroids: starting locations of centroids

    - train_split: fraction of data to fit on, 1-fraction to test on
    - label_col: column containing labels
"""
```

# Data Structures

Implementations of classic data structures implemented in Python, with tests!


## Hash Table

- Module: hashtable

- Initialize:
    - HashTable()
    - kwargs:
        - size: set fixed number of buckets in table (default = 1024)
        - hash_func: specify hashing function (default = 'additive')

- Hashing Functions:
    - 'additive': sum unicode number values of each character.
    - 'OAT'/'one-at-a-time': perform basic bitwise operations on individual characters
                             and total accumulator.
    - 'FNV': multiply everything by big prime numbers.

- Methods:
    - get(key): return value associated with key
    - set(key, value): add key, value pair to hash table
    - bracket notation supported

- Implementation:
Fixed size list of buckets(lists) where each bucket can contain multiple kv-pairs.

## Stack

- Can be initialized with (or without) iterable argument: Stack(iterable=None)

- Module: stack

- Attributes:

    - top: top/first node on stack

- Methods:

    - pop(): remove head and return its value

    - push(value): insert new node at head of list

    - size/len: return size of stack

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

## Priority Queue

- can be initialized with (or without) iterable argument: Queue(iterable=None)

- Module: priority_queue

- Methods:

    - insert(data, priority): enqueue data with priority (defaults to 0), lower is
                higher priority

    - pop(): remove and return item of highest priority. If multiple items of the same
                priority exist, pop item first inserted.

    - peek(): return value of next item to be popped

## Binary Heap

- Module: bin_heap

- Optional arguments:

    - an iterable

    - minheap or maxheap ('min' or 'max') defaulted to 'min'

- Methods:

    - push(value): add value to bottom of heap and sort as needed

    - pop(value): remove first/root node and return its value, move last node to root, sort as needed

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


## Graph

- Module: graph

- Methods:

    - add_node(n): add node to graph

    - del_node(n): delete node from graph along with edges it's part of

    - add_edge(n1, n2, weight=0): add a new edge to the graph connecting ‘n1’ to ‘n2’, if either
                n1 or n2 are not already present in the graph, they are added.

    - del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph,
                raises an error if no such edge exists

    - nodes(): return a list of all nodes in the graph

    - edges(): return a list of all edges in the graph

    - has_node(n): True if node ‘n’ is contained in the graph, False if not.

    - neighbors(n): returns the list of all nodes connected to ‘n’,
                raises an error if n is not in graph

    - adjacent(n1, n2): returns if there is an edge connecting n1 and n2,
                raises an error if either of the supplied nodes are not in graph

    - depth_first_traversal(start): Traverses graph depth first starting from 'start',
                returns path

    - breadth_first_traversal(start): Traverses graph breadth first starting from 'start',
                returns path

    - depth_first_traversal_iterative(start): Traverses graph depth first starting from 'start',
                returns path, slower than recursive version

    - dijkstra(start, end): return shortest path from start to end,
                implemented with dijkstra's algorithm.

    - floyd_warshall(): return path_dictionary, distance_dictionary for every
                possible path.

    - floyd_warshall_path(path, start, end): return shortest path from start
                to end.

### Authors:
- Ford Fowler
- Sera Smith
- Claire Gatenby
- Marc Kessler-Wenicker
- Casey O'Kane

### Testing:
