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
    for v in vectors:
        d = []
        # _d = {'dist': [], 'label': []}
        for c in centroids:
            _d = {'dist': None, 'label': None}
            _c = Vector.euclidean_distance(v, c)
            _d['dist'] = _c
            _d['label'] = c.label
            d.append(_d)
        # print d, 'd'
        # my_dict.iteritems(), key = itemgetter(1)
        c = min(d, key=lambda _x: _x['dist'])
        # print c, 'c'
        v.set_label(c['label'])
        clusters.append(c)
    return clusters

def gen_token(vectors):
    t = ''
    for v in vectors:
        t += str(v.label)
    return t

tt = {'dist' : [12,33.4], 'label': [0,1]}


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
points = zip(feat_1, feat_2, feat_3)
vectors = []
for i in points:
    _vec = Vector(i)
    vectors.append(_vec)
# print points
centroids = initialize_centroids(c_num, points)
new_centr = calculate_centroid(vectors)
print new_centr.features, 'new centr'
centr = new_centr.features
cluster_points(vectors, centroids)
print [x.label for x in vectors], ' before'
print gen_token(vectors), 'token', ' before'


tokens = []
for i in range(10):

    clusters = []
    new_centroids = []
    for c in range(c_num):
        cluster = []

        for v in vectors:

            # print c, v.label
            if v.label == c:
                cluster.append(v)
        _centr = calculate_centroid(cluster)
        _centr.set_label(c)
        new_centroids.append(_centr)
        # clusters.append(cluster)
    # print new_centroids, 'new centroids'
    cluster_points(vectors, new_centroids)
    # print [x.label for x in vectors], ' after'
    tokens = gen_token(vectors)
    # print token, 'token', ' after'
print tokens
# for vec in clusters:
#     calculate_centroid(vec)

# print len(clusters[0]), len(clusters[1])
# TODO normalizacja, drzewa z gh, petla i break gdy token sie nie zmienia, parallel processing, output
# TODO naprawic bledy z mierzeniem dystansu

