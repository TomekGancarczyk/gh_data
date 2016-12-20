import math
import random


def euclidean_distance(v1, v2):
    """
    calculates distance between two vectors in n-dimensional space of features (vector parameters)
    :param v1:
    :param v2:
    :return: euclidean distance
    """
    sub = []
    for i, feat in enumerate(v1):
        sub.append(math.pow((v1[i] - v2[i]), 2))
    dist = math.sqrt(sum(sub))
    return dist


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


def cluster_points(points, centroids):
    clusters = []
    for p in points:
        _d = []
        for c in centroids:
            _c = {'label': c['name'], 'dist': euclidean_distance(p, c['centroid']), 'points': p}
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
centroid_x = []
centroid_y = []
for c in range(c_num):
    centroid_x.append(random.random())
    centroid_y.append(random.random())

# print centroid_x
# print centroid_y
dist_x = []
dist_y = []
# print dist_x
points = zip(feat_1, feat_2)
vectors = []
for i in points:
    _vec = Vector(i)
    vectors.append(_vec)
# print points
cluster_num = 2
# print generate_centroids(cluster_num, points), 'centroids'
centroids = initialize_centroids(c_num, points)
new_centr = calculate_centroid(vectors)
print new_centr.features, 'new centr'
centr = new_centr.features
# clusters = cluster_points(points, centr)
# print clusters, 'clusters'
# c_points = [x['points'] for x in clusters]
# labels = [y['label'] for y in clusters]
# for j in range(cluster_num):
#     for c in clusters:
#         if c['label'] == j:
#             pass
# centr_labels = []
# centroids = []
# for c in centr:
#     print c['centroid'][0]
#     print c['centroid'][1]
#     print c['name']




# for p in points:
#     _dist = []
#     for c in generate_centroids([2, len(p)]):
#         _d = euclidean_distance(p, c['centroid'])
#         _dist.append(_d)



a = []
dist1 = []
dist2 = []
# for p in points:
#     min(euclidean_distance(p, [0.25, 0.77])
# for i, p in enumerate(points):
#     a.append(euclidean_distance(p, [0.25, 0.77]))
# print euclidean_distance([0.1,0.3], [0.23, 0.55])