import math
import random


def initialize_centroids(c_number, vectors=None):
    """
    generate number od centroid vectors in c_dim-dimensional space of features
    :param c_shape: (number of centroids, dimensions number)
    :return: centroid vectors
    """
    c_shape = (c_number, len(vectors[0]))
    centroids = []
    for n in range(c_shape[0]):
        _c = []
        for r in range(c_shape[1]):
            _c.append(random.random())
        _c_vec = Vector(_c)
        _c_vec.set_label(n)
        centroids.append(_c_vec)
    return centroids


def calculate_centroid(vectors=None):
    """
    generate number od centroid vectors in c_dim-dimensional space of features
    :param c_shape: (number of centroids, dimensions number)
    :return: centroid vectors
    """
    features = [x.features for x in vectors]

    v_f = map(sum, zip(*features))
    centroid = Vector([y / len(vectors) for y in v_f])
    return centroid


def cluster_points(vectors, centroids):
    clusters = []
    for p in vectors:
        _d = []
        for c in centroids:
            _c = {'label': c['name'], 'dist': Vector.euclidean_distance(p, c['centroid']), 'points': p}
            _d.append(_c)
        c = min(_d, key=lambda d: d['dist'])
        clusters.append(c)
    return clusters


class Vector(object):

    def __init__(self, features):
        self.features = features
        self.label = None
        self.dimension = len(features)

    def set_label(self, label):
        self.label = label

    @classmethod
    def euclidean_distance(cls, v1, v2):
        """
        calculates distance between two vectors in n-dimensional space of features (vector parameters)
        :param v1: vector object
        :param v2: vector object
        :return: euclidean distance
        """
        sub = []
        feat1 = v1.features
        feat2 = v2.features
        for i, feat in enumerate(feat1):
            sub.append(math.pow((feat1[i] - feat2[i]), 2))
        dist = math.sqrt(sum(sub))
        return dist


# dla dazdego pkt sprawdz dystans od centroidu
# przypisz pkt do grupy o nazwie centroidu
# dla grupy wygeneruj na nowo centroid
# sprawdz dystans pkt od nowych centroidow
# przypisz na nowo

dist_x = []
dist_y = []
points = zip(feat_1, feat_2)
vectors = []
for i in points:
    _vec = Vector(i)
    vectors.append(_vec)
# print points
# centroids = initialize_centroids(c_num, points)
new_centr = calculate_centroid(vectors)
print new_centr.features, 'new centr'
centr = new_centr.features
