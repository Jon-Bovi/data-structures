"""Test decision tree classifier implementation."""

import pytest


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


@pytest.fixture
def flowers():
    """Convert flower data for testing from csv."""
    from decision_tree import convert_csv
    return convert_csv('flowers_data.csv')


@pytest.fixture
def tree_sepal(clf, flowers):
    """Create a fixture for the last column which contains overlap."""
    sepal = [row[3:] for row in flowers]
    clf.fit(sepal, (0, 1))
    return clf


@pytest.fixture
def clf():
    """Create a clf to run tests on."""
    from decision_tree import Clf
    return Clf()


@pytest.fixture
def tree(clf, flowers):
    """Create a tree from flowers data."""
    clf.fit(flowers, (0, 1))
    return clf


def test_find_best_split(clf):
    """Test find_best_split on small dataset."""
    assert clf._find_best_split(DATASET) == BEST_SPLIT


def test_find_best_split_value(clf, flowers):
    """Test find_best_split_gets_best_value."""
    assert clf._find_best_split(flowers)[1] == 3.0


def test_clf_fit_has_root(tree):
    """Test fit method creates a tree."""
    assert tree.root


def test_clf_fit(tree):
    """Test fit method creates a split."""
    assert tree.root.split_value == 3.0


def test_clf_fit_chilrend(tree):
    """Test class on the left is 1."""
    assert tree.root.left == 0.0
    assert tree.root.right == 1.0
