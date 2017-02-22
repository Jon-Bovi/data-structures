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

    def init(self, max_iter=3, min_step=1):
        """Initialize classifier instance."""
        self.max_iter = max_iter
        self.min_step = min_step

    def _distance(self, x, y):
        """Return distance between points x and y."""
        return np.sqrt(np.sum((x - y)**2))

    def fit(self, data, k=2):
        """Build classification scheme from given data."""
        if k < 1 or k > len(data):
            raise ValueError('k must be in range 1 - len(data)')
        datas = [[x, 0] for x in data]
        locations = random.sample(list(datas), k)
        for idx, centroid in enumerate(locations):
            centroid[1] = idx
        while True:
            import pdb; pdb.set_trace()
            for row in datas:
                closest = min(locations, key=lambda x: self._distance(x[0], row[0]))
                row[1] = closest[1]
            for centroid in locations:
                cluster = [x for x in datas if x[1] == centroid[1]]
                for idx, value in enumerate(centroid):
                    centroid[0][idx] = sum([x[0][idx] for x in cluster]) / len(cluster)
