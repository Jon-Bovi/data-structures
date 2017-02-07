"""Implement a decision tree in python."""

import numpy as np


def convert_csv(filename):
    """Covert from csv."""
    data = np.loadtxt("housing.csv", delimiter=',', unpack=True)
    return data
