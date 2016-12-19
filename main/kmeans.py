import math
import random

centroid_x = []
centroid_y = []
for c in range(c_num):
    centroid_x.append(random.random())
    centroid_y.append(random.random())

# print centroid_x
# print centroid_y
dist_x_1 = []
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
    for i, f in enumerate(v1):
        sub.append(math.pow((v1[i] - v2[i]), 2))
    dist = math.sqrt(sum(sub))
    return dist


def generate_centroids(c_shape):
    """
    generate number od centroid vectors in c_dim-dimensional space of features
    :param c_shape: (number of centroids, dimensions number)
    :return: centroid vectors
    """
    centroids = []
    for n in range(c_shape[0]):
        _c = []
        for r in range(c_shape[1]):
            _c.append(random.random())
        _cc = {'c': _c, 'label': n }
        centroids.append(_cc)
    return centroids

def cluster_points(points, centroids):
    _c = []
    for p in points:

        _d = {'v': None, 'd': []}
        for c in centroids:
            _d['d'].append(euclidean_distance(p, c))
        _c.append(min(pp['d'] for pp in _d))
    return _c
print generate_centroids([2, 2]), 'centroids'
centroids = generate_centroids([2, len(points[0])])
print cluster_points(points, centroids)

for p in points:
    _dist = []
    for c in generate_centroids([2, len(p)]):
        _d = euclidean_distance(p, c['c'])
        _dist.append(_d)



a = []
dist1 = []
dist2 = []
# for p in points:
#     min(euclidean_distance(p, [0.25, 0.77])
# for i, p in enumerate(points):
#     a.append(euclidean_distance(p, [0.25, 0.77]))
# print euclidean_distance([0.1,0.3], [0.23, 0.55])