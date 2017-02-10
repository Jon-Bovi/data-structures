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

    def __init__(self, split_value, col, left=None, right=None, label=None):
        """Initailize Node."""
        self.split_value = split_value
        self.col = col
        self.left = left
        self.right = right
        self.label = label

        def depth(self):
            if self.parent:
                return 1 + self.parent.depth()
            return 1


class Clf(object):
    """."""

    def __init__(self, iterable, min_leaf_size=1, max_depth=5):
        """Initialize clf."""
        self._size = len(iterable)
        self.num_cols = len(iterable[0])
        self.min_leaf_size = min_leaf_size
        self.max_depth = max_depth

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
            g_val += len(split) / self._size * h_val
        return g_val

    def _split(self, dataset, col_idx, boundary_val):
        """Split column data based on a boundary (data coordinate)."""
        left, right = [], []
        for row in dataset:
            if row[col_idx] <= boundary_val:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def _find_best_split(self, dataset):
        """Return the decision boundary where the total purity of both sides is best."""
        best_split = None
        best_purity = 1
        for col_idx in range(len(dataset[0])):
            for row_idx, row in enumerate(dataset):
                boundary_val = dataset[row_idx][col_idx]
                left, right = self._split(dataset, col_idx, boundary_val)
                purity = self._purity((left, right), (0, 1))
                if purity < best_purity:
                    best_purity = purity
                    best_split = (col_idx, boundary_val)
        return best_split[0], best_split[1], left, right

    def fit(self, dataset, classes, parent=None):
        """Construct a decision tree based on some incoming dataset; returns nothing."""
        col_idx, split_value, left, right = self._find_best_split(dataset)
        new_node = Node(split_value, col_idx)

        if self._h_val(left, classes) != 0 and len(left) > self.min_leaf_size:
            new_node.left = self.fit(left, classes, parent=new_node)
        else:
            label = left[0][0]
            new_node.left = Node(0, 0, label=label)

        if self._h_val(right, classes) != 0 and len(right) > self.min_leaf_size:
            new_node.right = self.fit(right, classes, parent=new_node)
        else:
            label = right[0][0]
            new_node.right = Node(0, 0, label=label)

        return new_node
