"""AVL Binary Search Tree module."""
from queue import Queue


class BST(object):
    """AVL Binary search tree."""

    def __init__(self, iterable=None, autobalance=True):
        """Initialize bst with root and size."""
        self.root = None
        self._size = 0
        self.autobalance = autobalance
        if iterable:
            try:
                for val in iterable:
                    self.insert(val)
            except:
                raise Exception

    def size(self):
        """Return number of nodes in bst.."""
        return self._size

    def __len__(self):
        """Return number of nodes in bst."""
        return self.size()

    def __iter__(self):
        """Allow iteration through bst."""
        return self.root.__iter__()

    def _iterate_from(self, node):
        """Return a generator of all the children on the left of starting node."""
        while node is not None:
            yield node
            node = node.left

    def insert(self, val):
        """Insert a new node into the bst."""
        cur = self.root
        if cur is None:
            self.root = Node(val)
            self._size += 1
        else:
            while True:
                if val == cur.val:
                    return
                child, left_or_right = cur.left_or_right(val)
                if child is None:
                    setattr(cur, left_or_right, Node(val, parent=cur))
                    self._size += 1
                    r_root = self._check_balance(getattr(cur, left_or_right))
                    if r_root and self.autobalance:
                        self.rebalance(r_root)
                    break
                else:
                    cur = child

    def search(self, val, start='root'):
        """Return node with value val if it exists, otherwise None."""
        if start == 'root':
            return self.search(val, start=self.root)
        if start is None:
            return None
        if val == start.val:
            return start
        return self.search(val, start=start.left_or_right(val)[0])

    def contains(self, val):
        """Return whether val in bst."""
        return bool(self.search(val))

    def depth(self, start='root'):
        """Totally came up with this myself."""
        if start == 'root':
            start = self.root
        if start is None:
            return 0
        return max(self.depth(start=start.left), self.depth(start=start.right)) + 1

    def balance(self, start='root'):
        """Return left vs right balance from a node on the bst."""
        if start == 'root':
            start = self.root
        if start is None:
            return 0
        return self.depth(start=start.left) - self.depth(start=start.right)

    def pre_order(self, root='root'):
        """Return a generator of pre-order traversal."""
        if root == 'root':
            root = self.root
        if root:
            yield root.val
            for node in root.children():
                for child in self.pre_order(root=node):
                    yield child

    def post_order(self, root='root'):
        """Return a generator of post-order traversal."""
        if root == 'root':
            root = self.root
        if root:
            for node in root.children():
                for child in self.post_order(root=node):
                    yield child
            yield root.val

    def in_order(self, root='root'):
        """Return a generator of tree's nodes in order."""
        if root == 'root':
            root = self.root
        if root:
            for child in self.in_order(root=root.left):
                yield child
            yield root.val
            for child in self.in_order(root=root.right):
                yield child

    def breadth_first(self, start='root'):
        """Return a generator of breadth first traversal through tree."""
        if start == 'root':
            start = self.root
        q = Queue()
        visited = []
        if self._size > 0:
            visited = self._explore_bfs(start, q, visited)
        for node in visited:
            yield node.val

    def delete(self, val):
        """Delete a node and reorganize tree as needed."""
        to_d = self.search(val)
        if to_d:
            replacement = None
            check_from = to_d.parent
            self._size -= 1
            if to_d.is_leaf():
                to_d.set_parents_child(None)
            else:
                children = to_d.children()
                if len(children) == 1:
                    child = children[0]
                    child.parent = to_d.parent
                    to_d.set_parents_child(child)
                    replacement = child
                else:
                    lmost = self._get_leftmost(to_d)
                    replacement = lmost
                    if lmost.parent is to_d:
                        check_from = lmost
                    else:
                        check_from = lmost.parent
                    if lmost.right:
                        lmost.right.parent = lmost.parent
                    lmost.set_parents_child(lmost.right)
                    if to_d.right:
                        to_d.right.parent = lmost
                        lmost.right = to_d.right
                    lmost.left = to_d.left
                    to_d.left.parent = lmost

                    to_d.set_parents_child(lmost)
                    lmost.parent = to_d.parent
            if to_d.parent is None:
                self.root = replacement
            r_root = self._check_balance(check_from)
            if r_root and self.autobalance:
                self.rebalance(r_root)

    def _get_leftmost(self, node_to_delete):
        """Return the leftmost child of the right branch of the target node."""
        left_children = [node for node in self._iterate_from(self.search(node_to_delete.val).right)]
        return left_children[-1]

    def _explore_bfs(self, node, queue, visited):
        if node not in visited:
            visited.append(node)
        if node.children():
            for child in node.children():
                if child not in visited:
                    visited.append(child)
                    queue.enqueue(child)
            while len(queue):
                self._explore_bfs(queue.dequeue(), queue, visited)
        return visited

    def _check_balance(self, node):
        """Bubble up from a node and check for unbalanced trees."""
        while node:
            if abs(self.balance(start=node)) > 1:
                return node
            node = node.parent

    def rebalance(self, node):
        """Rebalance a tree starting at node."""
        if self.balance(node) < 0:
            if self.balance(node.right) <= 0:
                self._lr(node)
            else:
                self._rlr(node)
        elif self.balance(node) > 0:
            if self.balance(node.left) >= 0:
                self._rr(node)
            else:
                self._lrr(node)
        next_node = self._check_balance(node)
        if next_node:
            self.rebalance(next_node)

    def _lr(self, old_root):
        r"""
        Perform a left rotation (lr) around the old_root (old_root).

             3                      5
              \                    / \
               5        -->       3   9
              / \                  \
             4   9                  4
        """
        new_root = old_root.right
        old_root.right = new_root.left
        if new_root.left:
            new_root.left.parent = old_root
        if old_root.parent is None:
            self.root = new_root
        old_root.set_parents_child(new_root)
        new_root.parent = old_root.parent
        new_root.left = old_root
        old_root.parent = new_root

    def _rr(self, old_root):
        r"""
        Perform a right rotation (rl) around the rotation_root (r_root).

                  7              5
                 /              / \
                5      -->     1   7
               / \                /
              1   6              6
        """
        new_root = old_root.left
        old_root.left = new_root.right
        if new_root.right:
            new_root.right.parent = old_root
        if old_root.parent is None:
            self.root = new_root
        old_root.set_parents_child(new_root)
        new_root.right = old_root
        new_root.parent = old_root.parent
        old_root.parent = new_root

    def _lrr(self, old_root,):
        """
        Perform left-right rotation.

        Equivalent to left rotation on old_root.left then right rotation
        on old_root, but faster.
        """
        left_root = old_root.left
        new_root = left_root.right
        left_root.right = new_root.left
        old_root.left = new_root.right
        if new_root.left:
            new_root.left.parent = left_root
        if new_root.right:
            new_root.right.parent = old_root
        old_root.set_parents_child(new_root)
        if old_root.parent is None:
            self.root = new_root
        new_root.parent = old_root.parent
        new_root.right = old_root
        new_root.left = left_root
        old_root.parent = new_root
        left_root.parent = new_root

    def _rlr(self, old_root):
        """
        Perform right-left rotation.

        Equivalent to right rotation on old_root.right then left rotation
        on old_root, but faster.
        """
        right_root = old_root.right
        new_root = right_root.left
        right_root.left = new_root.right
        old_root.right = new_root.left
        if new_root.right:
            new_root.right.parent = right_root
        if new_root.left:
            new_root.left.parent = old_root
        old_root.set_parents_child(new_root)
        if old_root.parent is None:
            self.root = new_root
        new_root.parent = old_root.parent
        new_root.left = old_root
        new_root.right = right_root
        old_root.parent = new_root
        right_root.parent = new_root

    def __str__(self):
        from math import floor, ceil
        from decimal import Decimal
        fmt = ['                        {}',
               '           {}                      {}',
               '     {}        {}          {}        {}',
               '  {}  {}  {}  {}    {}  {}  {}  {}']

        def center(item):
            stritem = str(item)
            if len(stritem) < 5:
                split = (4 - len(stritem)) / 2
                return ' ' * floor(split) + stritem + ' ' * ceil(split)
            if isinstance(item, (int, float)):
                return center("{:.1E}".format(Decimal(item)).replace('+', ''))
            return item[:4]

        def children_of(nodes):
            res = []
            for node in nodes:
                if node:
                    res += [node.left, node.right]
                else:
                    res += [None, None]
            return res

        def get_input(prompt, options):
            while True:
                inp = input(prompt)
                if inp in options:
                    return inp

        top = 0
        root = self.root
        try:
            while True:
                four_rows = [[root]]
                for i in range(3):
                    four_rows.append(children_of(four_rows[i]))
                vals = []
                for row in four_rows:
                    row_vals = []
                    for item in row:
                        row_vals.append(item.val if item else '_')
                    vals.append([center(v) for v in row_vals])
                hunk = ''
                for i, row in enumerate(fmt):
                    hunk += row.format(*vals[i]) + '\n'
                print(hunk)
                valid = ''
                if root.left.depth() > 2:
                    valid += 'a'
                if top != 0:
                    valid += 'w'
                if root.right.depth() > 2:
                    valid += 'd'
                inp = get_input('q(uit) / ' + valid + ': ', set(valid + 'q'))
                if inp == 'q':
                    return ''
                top += {'a': 1, 'w': -1, 'd': 1}[inp]
                root = {'a': root.left,
                        'w': root.parent,
                        'd': root.right}[inp]
        except KeyboardInterrupt:
            return ''

    def balanced(self, frm='root'):
        """Return whether tree is balanced from every node."""
        pass


class Node(object):
    """BST's Node object."""

    def __init__(self, val, left=None, right=None, parent=None):
        """Set attributes on node object."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        """Return whether node has no children."""
        return not (self.right or self.left)

    def children(self):
        """Return non-none children of node."""
        return [n for n in [self.left, self.right] if n is not None]

    def left_or_right(self, val):
        """Compare node to a value and return which path to take."""
        if val < self.val:
            return self.left, 'left'
        return self.right, 'right'

    def set_parents_child(self, new_child):
        """Reassign parent's pointer to this node to new_child node."""
        if self.parent:
            if self.parent.left is self:
                self.parent.left = new_child
            else:
                self.parent.right = new_child

    def __iter__(self):
        if self:
            if self.left:
                for n in self.left:
                    yield n
            yield self
            if self.right:
                for n in self.right:
                    yield n

    def depth(self):
        dep = 1
        children = [x for x in [self.left, self.right] if x]
        if children:
            dep += max([x.depth() for x in children])
        return dep

    def balance(self):
        """Balance from node."""
        right = self.right.depth() if self.right else 0
        left = self.left.depth() if self.left else 0
        return right - left

    def __str__(self, level=0):
        """Display a strange sideways tree with values and balance at each node."""
        ret = "\t"*level+repr(self.val)+': '+repr(self.balance())+"\n"
        for child in [x for x in [self.left, self.right] if x]:
            ret += child.__str__(level+1)
        return ret

"""
def delete(self, val):
        ""Delete a node and reorganize tree as needed.""
        to_d = self.search(val)
        if to_d:
            replacement = None
            check_from = to_d.parent
            self._size -= 1
            if to_d.is_leaf():
                to_d.set_parents_child(None)
            else:
                children = to_d.children()
                if len(children) == 1:
                    child = children[0]
                    child.parent = to_d.parent
                    to_d.set_parents_child(child)
                    replacement = child
                else:
                    lmost = self._get_leftmost(to_d)
                    replacement = lmost
                    check_from = lmost
                    if lmost.parent is not to_d:
                        check_from = lmost.parent
                    if lmost.right:
                        lmost.right.parent = lmost.parent
                    lmost.set_parents_child(lmost.right)
                    if to_d.right:
                        to_d.right.parent = lmost
                    lmost.right = to_d.right
                    lmost.left = to_d.left
                    to_d.left.parent = lmost

                    to_d.set_parents_child(lmost)
                    lmost.parent = to_d.parent
            if to_d.parent is None:
                self.root = replacement
            return check_from
            r_root = self._check_balance(check_from)
            if r_root:
                self.rebalance(r_root)
"""
