"""Test decision tree classifier implementation."""

import pytest


# @pytest.fixture
# def flowers():
#     """Convert flower data for testing from csv."""
#     from decision_tree import convert_csv
#     return convert_csv('flowers_data.csv')


DATASET = [
    [2.771244718, 1.784783929, 0],
    [1.728571309, 1.169761413, 0],
    [3.678319846, 2.81281357, 0],
    [3.961043357, 2.61995032, 0],
    [2.999208922, 2.209014212, 0],
    [7.497545867, 3.162953546, 1],
    [9.00220326, 3.339047188, 1],
    [7.444542326, 0.476683375, 1],
    [10.12493903, 3.234550982, 1],
    [6.642287351, 3.319983761, 1]
]

BEST_SPLIT = (
    0,
    6.642287351,
    [[2.771244718, 1.784783929, 0],
     [1.728571309, 1.169761413, 0],
     [3.678319846, 2.81281357, 0],
     [3.961043357, 2.61995032, 0],
     [2.999208922, 2.209014212, 0]],
    [[7.497545867, 3.162953546, 1],
     [9.00220326, 3.339047188, 1],
     [7.444542326, 0.476683375, 1],
     [10.12493903, 3.234550982, 1],
     [6.642287351, 3.319983761, 1]])


def test_find_best_split():
    """Test find_best_split."""
    from decision_tree import Clf
    clf = Clf()
    print(clf._find_best_split(DATASET))
    assert clf._find_best_split(DATASET) == BEST_SPLIT
