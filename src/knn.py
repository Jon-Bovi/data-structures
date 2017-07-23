"""Implement K Nearest Neighbour Classifier in Python."""


class Knn(object):
    """K Nearest Neigbour Classifier.

    Knn.predict(self, data): returns labels for your test data.
    """

    def __init__(self, dataset, k=5):
        """Initialize classifier."""
        if type(k) is not int or k > len(dataset) or k < 0:
            raise ValueError("k must be an integer value between 1 and the length of the dataset")
        self.dataset = dataset
        self.k = k

    def predict(self, data, k=None):
        """Given a data point, predict the class of that data, based on dataset."""
        if not k:
            k = self.k
        for p in data:
            d_list = []
            for q in self.dataset:
                d_list.append((self._distance(p, q[:-1]), q[-1]))
            neighbors = sorted(d_list)[:k]
            label = self._get_majority_class([x[1] for x in neighbors])
            if len(label) > 1:
                return self.predict(data, k=k - 1)
            return label[0]

    def _get_majority_class(self, classes):
        """Find and return the majority class of a dataset."""
        classes_set = set(classes)
        count = {c: classes.count(c) for c in classes_set}
        highest = max(count.values())
        return [k for k, v in count.items() if v == highest]

    def _distance(self, p, q):
        """Calculate the distance between two points."""
        import numpy as np
        return np.sqrt(np.sum((p - q)**2))
