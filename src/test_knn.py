"""Test K-nearest neighbors classifier."""

import pytest
import numpy as np


DATASET = [
    np.array([2.77, 1.78, 5.7, 4.4, 0]),
    np.array([1.72, 1.16, 5.7, 4.4, 0]),
    np.array([3.67, 2.81, 5.7, 4.4, 0]),
    np.array([3.96, 2.61, 5.7, 4.4, 0]),
    np.array([2.99, 2.20, 5.7, 4.4, 0]),
    np.array([7.49, 3.16, 5.7, 4.4, 1]),
    np.array([9.00, 3.33, 5.7, 4.4, 1]),
    np.array([7.44, 0.47, 5.7, 4.4, 1]),
    np.array([10.12, 3.23, 5.7, 4.4, 1]),
    np.array([6.64, 3.319, 5.7, 4.4, 1])
]

CLASSES = [
    [[0, 1, 1, 0, 0], [0]],
    [[0, 1, 1, 0, 0, 1], [0, 1]],
    [['setosa', 'versicolor', 'versicolor', 'setosa', 'setosa', 'versicolor'], ['setosa', 'versicolor']],
    [['setosa', 'versicolor', 'setosa', 'setosa', 'versicolor'], ['setosa']],
]


@pytest.fixture
def flowers():
    """Convert flower data for testing from csv."""
    from decision_tree import convert_csv
    return convert_csv('flowers_data.csv')


@pytest.fixture
def knn(flowers):
    """Create a Knn to run tests on."""
    from knn import Knn
    return Knn(flowers)


def test_knn_predict_returns_a_class_label(knn):
    """Predict should return a zero or one."""
    assert knn.predict([x[:-1] for x in DATASET]) in (0, 1)


def test_knn_tries_again_if_equal_majority_classes_within_k(knn):
    """If there are equal numbers of classes within k, try again with k-1."""
    from knn import Knn
    knn = Knn(DATASET, k=2)
    assert knn.predict([np.array([5.5, 3, 5.7, 4.4])]) in (0, 1)


@pytest.mark.parametrize('k', [-1, 12, 'five'])
def test_knn_raises_error_if_k_invalid(k):
    """
    When initializing knn, error should raise if k is less than zero, greater
    than the length of the dataset, or not an integer.
    """
    from knn import Knn
    with pytest.raises(ValueError):
        Knn(DATASET, k=k)


@pytest.mark.parametrize('classes', CLASSES)
def test_get_majority_classes(classes, knn):
    """Should return a list of the majority class(es) in the k nearest neighbors."""
    assert sorted(knn._get_majority_class(classes[0])) == classes[1]
