"""Implement K Nearest Neighbour Classifier in Python."""


class Knn(object):
    """K Nearest Neigbour Classifier.

    Knn.predict(self, data): returns labels for your test data.
    """

    def __init__(self, k=5, dataset=None):
        """Initialize classifier."""
        self.dataset = dataset
        self.k = 5

    def predict(self, data, k=None):
        """Given a data point, predict the class of that data, based on dataset."""
        if not k:
            k = self.k
        for p in data:
            d_list = []
            for q in self.dataset:
                d_list.append((self._distance(p, q), q[-1]))
            neighbors = sorted(d_list)[:k]
            label = self._get_majority_class([x[1] for x in neighbors])
            if len(label) > 1:
                return self.predict(data, k=k - 1)
            return label[0]

    def _get_majority_class(self, classes):
        """Find and return the majority class of a dataset."""
        count = {c: classes.count(c) for c in classes}
        highest = max(count.values())
        return [k for k, v in count.items() if v == highest]

    def _distance(self, p, q):
        """Calculate the distance between two points."""
        import numpy as np
        return np.sqrt(np.sum((p - q)**2))
