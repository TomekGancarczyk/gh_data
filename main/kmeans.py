import math
import random

centroid_x = []
centroid_y = []
for c in range(c_num):
    centroid_x.append(random.random())
    centroid_y.append(random.random())

# print centroid_x
# print centroid_y
dist_x = []
dist_y = []
for c in centroid_x:
    pass
for f in feat_1:
    dist_x.append(abs(f - centroid_x[0]))
    dist_y.append(abs(f - centroid_x[1]))
# print dist_x
points = zip(feat_1, feat_2)
# print points


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


def generate_centroids(c_number, vectors=None):
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
        _cc = {'centroid': _c, 'name': n}
        centroids.append(_cc)
    return centroids

def cluster_points(points, centroids):
    _c = []
    for p in points:

        _d = {'v': None, 'd': []}
        for c in centroids:
            _d['d'].append(euclidean_distance(p, c))
        _c.append(min(x['d'] for x in _d))
    return _c

# dla dazdego pkt sprawdz dystans od centroidu
# przypisz pkt do grupy o nazwie centroidu
# dla grupy wygeneruj na nowo centroid
# sprawdz dystans pkt od nowych centroidow
# przypisz na nowo


print generate_centroids(2, points), 'centroids'
centroids = generate_centroids(2, points)
# print cluster_points(points, centroids)

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