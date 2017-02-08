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


def purity(splits, classes):
    g_val = 0.0
    for idx, split in enumerate(splits):
        h_val = 0
        for class_val in classes:
            proportion = [row[-1] for row in split].count(class_val) / len(split)
            h_vals[idx] += (proportion * (1.0 - proportion))
        g_val += len(split) / len(self.size)
    return g_val