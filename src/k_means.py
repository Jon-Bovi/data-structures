import random
import numpy as np


def convert_csv(filename, cols=(0, 1, 2, 3)):
    """Covert from csv."""
    import numpy as np
    data = np.loadtxt(filename,
                      delimiter=',',
                      unpack=True,
                      skiprows=1,
                      usecols=cols)
    return data.transpose()


class KMeansClassifier(object):
    """."""

    def __init__(self, max_iter=3, min_step=1):
        """Initialize classifier instance."""
        self.max_iter = max_iter
        self.min_step = min_step
        self.centroids = []
        self.fitted = False

    def _distance(self, x, y):
        """Return distance between points x and y."""
        return np.sqrt(np.sum((x - y)**2))

    def fit(self, data, k=2):
        """Build classification scheme from given data."""
        if k < 1 or k > len(data):
            raise ValueError('k must be in range 1 - len(data)')
        self.fitted = True
        datas = [[x, 0] for x in data]
        self.centroids = random.sample(list(datas), k)
        for idx, centroid in enumerate(self.centroids):
            centroid[1] = idx + 1

        iterations = 0
        while iterations < self.max_iter:
            for row in datas:
                closest = min(self.centroids, key=lambda x: self._distance(x[0], row[0]))
                row[1] = closest[1]
            for centroid in self.centroids:
                cluster = [x for x in datas if x[1] == centroid[1]]
                for idx, value in enumerate(centroid):
                    centroid[0][idx] = sum([x[0][idx] for x in cluster]) / len(cluster)
            iterations += 1

    def predict(self, data):
        """Return predicted classes for given data."""
        if not self.fitted:
            raise Exception("Classifier must be fit before using to predict.")
        classes = []
        for row in data:
            classes.append(min(self.centroids, key=lambda c: self._distance(c[0], row))[1])
        return classes

    def cross_validate(self, data):
        """Split a classified dataset in two, fit on one, predict the other."""
        fitter, tester, test_labels = [], [], []
        for i, d in enumerate(data):
            if i % 2:
                fitter.append(d[:-1])
            else:
                tester.append(d[:-1])
                test_labels.append(d[-1] + 1)
        self.fit(fitter)
        res_labels = self.predict(tester)
        count = 0
        for i, label in enumerate(test_labels):
            if label == res_labels[i]:
                count += 1
        return count / len(test_labels)