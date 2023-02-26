import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score


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
    
    def get_centroids(self):
        num_clusters = len(set(self.labels))
        centroids = []
        for i in range(num_clusters):
            cluster_points = self.X[self.labels == i]
            centroids.append(np.mean(cluster_points, axis=0))
        return centroids
    
    def get_cluster_sizes(self):
        cluster_sizes = []
        for i in range(len(set(self.labels))):
            cluster_sizes.append(len(self.X[self.labels == i]))
        return cluster_sizes
    
    def plot_clusters(self):
        fig, ax = plt.subplots(figsize=(8, 6))
        for i in range(len(set(self.labels))):
            cluster_points = self.X[self.labels == i]
            ax.scatter(cluster_points[:, 0], cluster_points[:, 1], s=50, alpha=0.5)
        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.set_title('Cluster plot')
        plt.show()

    def find_optimal_k(self):
        ngmd_scores = []
        for k in range(2, 11):
            labels = KMeans(n_clusters=k).fit_predict(self.X)
            ngmd = NGMD(self.X, self.labels).calculate()
            ngmd_scores.append(ngmd)

        # plot NGMD scores for different values of k
        plt.plot(range(2, 11), ngmd_scores, marker='o')
        plt.xlabel('Number of clusters')
        plt.ylabel('NGMD score')
        plt.title('Elbow method for determining optimal k')
        plt.show()

    def evaluate(self, metric='silhouette_score'):

        if metric == 'silhouette_score':
            score = silhouette_score(self.X, self.labels)
        elif metric == 'davies_bouldin_score':
            score = davies_bouldin_score(self.X, self.labels)
        elif metric == 'calinski_harabasz_score':
            score = calinski_harabasz_score(self.X, self.labels)
        else:
            raise ValueError('Invalid metric specified.')
        
        return score

    def predict(self, X_new):        
        kmeans = KMeans(n_clusters=len(set(self.labels)))
        kmeans.fit(self.X)
        labels_new = kmeans.predict(X_new)
        
        return labels_new