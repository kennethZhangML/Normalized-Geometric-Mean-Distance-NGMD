import numpy as np

class NGMD:

    '''
    "Normalized Geometric Mean Distance" (NGMD) is a distance-based metric used for evaluating clustering algorithms. 
    The NGMD metric measures the geometric mean of the pairwise distances between the centroids of the clusters, 
    normalized by the distance between the two farthest points in the dataset.
    '''
    def __init__(self, X, labels):
        self.X = X
        self.labels = labels
    
    def distance(self, a, b):
        return np.sqrt(np.sum((a - b)**2))
    
    def farthest_distance(self):
        farthest_dist = 0
        for i in range(len(self.X)):
            for j in range(i+1, len(self.X)):
                dist = self.distance(self.X[i], self.X[j])
                if dist > farthest_dist:
                    farthest_dist = dist
        return farthest_dist
    
    def calculate(self):
        num_clusters = len(set(self.labels))
        centroids = []
        for i in range(num_clusters):
            cluster_points = self.X[self.labels == i]
            centroids.append(np.mean(cluster_points, axis=0))
        centroid_distances = []
        for i in range(num_clusters):
            for j in range(i+1, num_clusters):
                dist = self.distance(centroids[i], centroids[j])
                centroid_distances.append(dist)
        geo_mean = np.prod(centroid_distances) ** (1.0 / len(centroid_distances))
        max_dist = self.farthest_distance()
        ngmd = geo_mean / max_dist
        return ngmd
