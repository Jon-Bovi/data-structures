"""AVL Binary Search Tree module."""

import math
import shutil


class BinaryTreeNode(object):
    """Node object with helper methods for use in a Binary Tree."""

    def __init__(self, val, left=None, right=None, parent=None):
        """Set attributes on node object."""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = 1

    @property
    def balance(self):
        """Balance from node."""
        right = self.right.depth if self.right else 0
        left = self.left.depth if self.left else 0
        return right - left

    def is_leaf(self):
        """Return whether node has no children."""
        return not (self.right or self.left)

    def children(self):
        """Return non-none children of node."""
        return [node for node in [self.left, self.right] if node]

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


class BinaryTree(object):
    """
    AVL Binary search tree.
    """

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

    def insert(self, val):
        """Insert a new node into the bst."""
        cur = self.root
        if cur is None:
            self.root = BinaryTreeNode(val)
            self._size += 1
        else:
            while True:
                if val == cur.val:
                    return
                child, left_or_right = cur.left_or_right(val)
                if child is None:
                    self._size += 1
                    new_node = BinaryTreeNode(val, parent=cur)
                    setattr(cur, left_or_right, new_node)
                    self._bubble_up_depth_from(cur)
                    if self.autobalance:
                        r_root = self._find_unbalanced(new_node)
                        if r_root:
                            self._rebalance(r_root)
                    break
                else:
                    cur = child

    def search(self, val):
        """Return node with value val if it exists, otherwise None."""
        cur_node = self.root
        while cur_node:
            if cur_node.val == val:
                return cur_node
            cur_node, trash = cur_node.left_or_right(val)

    def delete(self, val, error=False):
        """Delete a node and reorganize tree as needed."""
        to_d = self.search(val)
        if error and to_d is None:
            raise ValueError('Not in tree.')
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
                    lmost = self.node_furthest('left', from_=to_d.right)
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
                    if to_d.left:
                        to_d.left.parent = lmost
                    lmost.right = to_d.right
                    lmost.left = to_d.left

                    to_d.set_parents_child(lmost)
                    lmost.parent = to_d.parent
            if to_d.parent is None:
                self.root = replacement
            if check_from:
                self._bubble_up_depth_from(check_from)
            if self.autobalance:
                r_root = self._find_unbalanced(check_from)
                if r_root:
                    self._rebalance(r_root)

    def contains(self, val):
        """Return whether val in bst."""
        return bool(self.search(val))

    def balance(self, from_='root'):
        """Return left vs right balance from a node on the bst."""
        if from_ == 'root':
            from_ = self.root
        if from_ is None:
            return 0
        left_depth = from_.left.depth if from_.left else 0
        right_depth = from_.right.depth if from_.right else 0
        return left_depth - right_depth

    def pre_order(self, start='root', attr='val'):
        """Return a generator of pre-order traversal."""
        if start == 'root':
            start = self.root
        if start:
            yield getattr(start, attr) if attr else start
            for node in start.children():
                for child in self.pre_order(start=node, attr=attr):
                    yield child

    def post_order(self, start='root', attr='val'):
        """Return a generator of post-order traversal."""
        if start == 'root':
            start = self.root
        if start:
            for node in start.children():
                for child in self.post_order(start=node, attr=attr):
                    yield child
            yield getattr(start, attr) if attr else start

    def in_order(self, start='root', attr='val'):
        """Return a generator of tree's nodes in order."""
        if start == 'root':
            start = self.root
        if start:
            for child in self.in_order(start=start.left, attr=attr):
                yield child
            yield getattr(start, attr) if attr else start
            for child in self.in_order(start=start.right, attr=attr):
                yield child

    def breadth_first(self, start='root', attr='val'):
        """Return generator of breadth first traversal of tree rooted at root."""
        if start == 'root':
            start = self.root
        parent_queue = []
        if start:
            parent_queue.append(start)
        while parent_queue:
            parent = parent_queue.pop(0)
            yield getattr(parent, attr) if attr else parent
            left, right = parent.left, parent.right
            parent_queue.extend(parent.children())

    def _rebalance(self, node):
        """Rebalance a tree starting at node."""
        if self.balance(from_=node) < 0:
            if self.balance(from_=node.right) <= 0:
                r_root = self._lr(node)
            else:
                r_root = self._rlr(node)
        else:
            if self.balance(from_=node.left) >= 0:
                r_root = self._rr(node)
            else:
                r_root = self._lrr(node)
        self._reset_depths_from(r_root)
        self._bubble_up_depth_from(r_root)
        next_node = self._find_unbalanced(node)
        if next_node:
            self._rebalance(next_node)

    def _find_unbalanced(self, node):
        """Bubble up from a node and check for unbalanced trees."""
        while node:
            if abs(self.balance(from_=node)) > 1:
                return node
            node = node.parent

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
        return new_root

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
        return new_root

    def _lrr(self, old_root):
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
        return new_root

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
        return new_root

    def _bubble_up_depth_from(self, node):
        children = node.children()
        node.depth = 1
        if children:
            node.depth += max(c.depth for c in children)
        if node.parent:
            self._bubble_up_depth_from(node.parent)

    def _reset_depths_from(self, node):
        children = node.children()
        node.depth = 1
        if children:
            node.depth += max(self._reset_depths_from(c) for c in children)
        return node.depth

    def node_furthest(self, direction, from_='root'):
        """Traverse as far as possible in direction from from_."""
        if from_ == 'root':
            from_ = self.root
        while True:
            nxt = getattr(from_, direction)
            if nxt is None:
                break
            from_ = nxt
        return from_

    def size(self):
        """Return number of nodes in bst.."""
        return self._size

    def __len__(self):
        """Return number of nodes in bst."""
        return self.size()

    def __str__(self):
        if self.root is None:
            return 'Empty'
        node_func = attrs_func
        args = [['val']]
        head = display_rows_from(self.root, 5, node_func, args=args)
        if self.root.depth > 5:
            head += '\n\t...'
        return head


def display_rows_from(root, num_rows, node_func, max_len=4, args=()):
    """Return printable tree."""
    width = shutil.get_terminal_size((96, 20)).columns
    rows = [[root]]

    for i in range(num_rows - 1):
        rows.append(children_of(rows[i]))
        if not any(rows[-1]):
            break

    vals = []
    for row in rows:
        vals.append([node_func(node, *args) if node else '_' for node in row])

    return stringify_rows(vals, width, max_len)


def display(binary_tree, num_rows=5, node_func=None, args=(), attrs=None):
    """Interactive print loop."""

    if binary_tree.root is None:
        print('Empty')
    if node_func is None:
        if attrs is None:
            attrs = ['val']
        elif isinstance(attrs, str):
            attrs = [attrs]
        node_func = attrs_func
        args = [attrs]
    furthest_right = binary_tree.node_furthest('right')
    root = binary_tree.root
    top = 0

    try:
        while True:
            max_len = len(str(node_func(furthest_right, *args)))
            hunk = display_rows_from(root,
                                     num_rows,
                                     node_func,
                                     max_len=max_len,
                                     args=args)
            print(hunk)

            valid_moves = ''
            if root.left and root.left.depth > (num_rows - 2):
                valid_moves += 'a'
            if root.right and root.right.depth > (num_rows - 2):
                valid_moves += 'd'
            if top != 0:
                valid_moves += 'w'
            quits = {'q', 'quit', 'exit'}

            while True:
                inp = input('q(uit)/attr/' + valid_moves + ': ').strip()
                if inp in set(valid_moves) | quits:
                    break
                else:
                    try:
                        for attr in inp.split(':'):
                            getr(root, attr)
                        break
                    except AttributeError:
                        pass

            if inp in quits:
                return
            if inp in valid_moves:
                top += {'a': 1, 'w': -1, 'd': 1}[inp]
                root = {'a': root.left,
                        'w': root.parent,
                        'd': root.right}[inp]
            else:
                inp_list = inp.split(':')
                node_func = attrs_func
                args = [inp_list]

    except KeyboardInterrupt:
        return


def stringify_rows(rows, width, max_len):
    """Create tree string."""
    funcs = [math.floor, math.ceil]
    width += width % 2
    num_per = 1
    res = []
    for row in rows:
        rowstr = ''
        each_gets = width / num_per
        split_len = (width - (max_len * num_per)) / (num_per * 2)
        for x in range(num_per):
            rowstr += str(row[x]).center(max_len).join(' ' * funcs[x % 2](split_len) for x in range(2))
            each_currently_getting = len(rowstr) / (x + 1)
            if each_gets < each_currently_getting:
                rowstr = rowstr[:-1]
            elif each_gets > each_currently_getting:
                rowstr += ' '
        res.append(rowstr)
        num_per *= 2
    res = '\n'.join(res)
    return res


def children_of(nodes):
        res = []
        for node in nodes:
            if node:
                res += [node.left, node.right]
            else:
                res += [None, None]
        return res


def attrs_func(node, attrs):
    res = ('{}:' * len(attrs)).format(*[getr(node, a) for a in attrs])[:-1]
    return res


def getr(obj, toget, safe=True):
    res = obj
    for attr in toget.split('.'):
        res = getattr(res, attr)
        if res is None:
            break
    return res