"""Implement a decision tree in python."""

import numpy as np


def convert_csv(filename):
    """Covert from csv."""
    data = np.loadtxt(filename,
                      delimiter=',',
                      unpack=True,
                      skiprows=1,
                      usecols=(0, 1, 2, 3, 4))
    return data.transpose()


class Node(object):
    """Node."""

    def __init__(self, split_value, col, left=None, right=None, label=None, parent=None):
        """Initailize Node."""
        self.split_value = split_value
        self.col = col
        self.left = left
        self.right = right
        self.label = label
        self.parent = parent

    def depth(self):
        """Return the depth of the node."""
        if self.parent:
            return 1 + self.parent.depth()
        return 1

    def children(self):
        """Return non-none children of node."""
        return [n for n in [self.left, self.right] if n is not None]


class Clf(object):
    """Classifier decision tree.

    clf.fit(self, data): construct a decision tree based on some incoming data
        set; returns nothing
    clf.predict(self, data): returns labels for your test data.
    """

    def __init__(self, min_leaf_size=1, max_depth=3):
        """Initialize clf."""
        self.min_leaf_size = min_leaf_size
        self.max_depth = max_depth
        self.root = None

    def depth(self, start='root'):
        """Return the depth of the tree."""
        if start == 'root':
            start = self.root
        if start > -1 or start is None:
            return 0
        return max(self.depth(start=start.left), self.depth(start=start.right)) + 1

    def _h_val(self, dataset, classes):
        h_val = 0
        for class_val in classes:
            if len(dataset) != 0:
                proportion = [row[-1] for row in dataset].count(class_val) / len(dataset)
                h_val += (proportion * (1.0 - proportion))
        return h_val

    def _purity(self, splits, classes):
        """Determine the purity."""
        g_val = 0.0
        for split in splits:
            h_val = self._h_val(split, classes)
            g_val += len(split) / sum([len(n) for n in splits]) * h_val
        return g_val

    def _split(self, dataset, col_idx, boundary_val):
        """Split column data based on a boundary (data coordinate)."""
        left, right = [], []
        for row in dataset:
            if row[col_idx] < boundary_val:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def _find_best_split(self, dataset):
        """Return the decision boundary where the total purity of both sides is best."""
        best_split = None
        best_purity = 1

        for col_idx in range(len(dataset[0]) - 1):
            for row_idx, row in enumerate(dataset):
                boundary_val = dataset[row_idx][col_idx]
                left, right = self._split(dataset, col_idx, boundary_val)
                purity = self._purity((left, right), (0, 1))
                if purity < best_purity:
                    best_purity = purity
                    best_split = (col_idx, boundary_val, left, right)
        return best_split

    def _get_majority_class(self, dataset):
        """Find and return the majority class of a dataset."""
        classes = [row[-1] for row in dataset]
        return max(set(classes), key=classes.count)

    def fit(self, dataset, classes, parent=None):
        """Construct a decision tree based on a dataset; returns nothing."""
        col_idx, split_value, left, right = self._find_best_split(dataset)
        new_node = Node(split_value, col_idx, parent=parent)

        if not left or not right:
            label = self._get_majority_class(left + right)
            return label

        if new_node.depth() >= self.max_depth:
            new_node.left = self._get_majority_class(left)
            new_node.right = self._get_majority_class(right)
            return new_node

        if self._h_val(left, classes) != 0 and len(left) > self.min_leaf_size:
            new_node.left = self.fit(left, classes, parent=new_node)
        else:
            label = self._get_majority_class(left)
            new_node.left = label

        if self._h_val(right, classes) != 0 and len(right) > self.min_leaf_size:
            new_node.right = self.fit(right, classes, parent=new_node)
        else:
            label = self._get_majority_class(right)
            new_node.right = label

        if new_node.parent:
            return new_node
        else:
            self.root = new_node

    def predict(self, dataset):
        """Return labels for test data."""
        return [self._find_terminal(row) for row in dataset]

    def _find_terminal(self, row):
        """Traverse down a branch to label a data point."""
        cur_node = self.root
        while type(cur_node) is Node:
            if row[cur_node.col] < cur_node.split_value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return cur_node

    def cross_validate(self, dataset, classes):
        """Split a classified dataset in two, fit on one, predict the other."""
        fitter, tester, test_labels = [], [], []
        for i, d in enumerate(dataset):
            if i % 2:
                fitter.append(d)
            else:
                tester.append(d[:-1])
                test_labels.append(d[-1])
        self.fit(fitter, classes)
        res_labels = self.predict(tester)
        count = 0
        for i, n in enumerate(test_labels):
            if n == res_labels[i]:
                count += 1
        return count / len(test_labels)
