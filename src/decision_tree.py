"""Implement a decision tree in python."""

import numpy as np


def convert_csv(filename):
    """Covert from csv."""
    data = np.loadtxt(filename,
                      delimiter=',',
                      unpack=True,
                      skiprows=1,
                      usecols=(0, 1, 2, 3, 4))
    return data


class Clf(object):
    """."""

    def __init__(self, iterable):
        """Initialize clf."""
        self._size = len(iterable)

    def _purity(self, splits, classes):
        """Determine the purity."""
        g_val = 0.0
        for split in splits:
            h_val = 0
            for class_val in classes:
                proportion = [row[-1] for row in split].count(class_val) / len(split)
                h_val += (proportion * (1.0 - proportion))
            g_val += len(split) / len(self._size) * h_val
        return g_val

    def _split(self, col, boundary):
        """Split column data based on a boundary (data coordinate)."""
        left, right = [], []
        for row in col:
            if row <= boundary:
                left.append(row)
            else:
                right.append(row)
        return left, right
