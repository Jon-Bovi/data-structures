# data-structures

Sample code (with tests) for classic data structures implemented in Python.

## Linked List

- Can be initialized with (or without) iterable argument.

- Attributes:

    - head: first node in linked list

- Methods:

    - pop(): remove head and return its value

    - push(value): insert new node at head of list

    - remove(node): find and remove node from list

    - search(value): find and return first node with value equal to argument

    - display(): print list in pseudo-tuple format

## Stack

- Can be initialized with (or without) iterable argument.

- Attributes:

    - top: top/first node on stack

- Methods:

    - pop(): remove head and return its value

    - push(value): insert new node at head of list

    - size/len: return size of stack

## Doubly-Linked List

- Can be initialized with (or without) iterable argument.

- Methods:

    - push(value): insert value at head of list

    - append(value): add value to tail of list

    - pop(): remove head and return its value

    - shift(): remove tail and return its value

    - remove(val): remove first instance of value in list, or raise exception if no matches

Doubly-linked lists vs Singly-linked Lists:

    Singly-linked lists and doubly-linked lists each have their own unique advantages and disadvantages. Singly-linked lists require less code and less memory as each node only has a value and a single pointer. This also makes them faster for both removing and inserting near the head node. Doubly-linked lists, however, allow more efficient reverse searches/traversal and for quicker appending/removal of new nodes near the tail of the list. And if you ever want to look back as you're traversing along the list, doubly-linked lists are easy while, with a singly-linked list, you either have to keep track of the node behind as you traverse, or you have to traverse all the way up to it from the head.
