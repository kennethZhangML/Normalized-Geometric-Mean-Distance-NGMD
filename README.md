# Normalized-Geometric-Mean-Distance-NGMD
Normalized Geometric Mean Distance (NGMD) - Unique Clustering Metric

The NGMD metric provides a measure of the quality of clustering by calculating the geometric mean of the pairwise distances between the centroids of the clusters, 
normalized by the distance between the two farthest points in the dataset. This metric is useful in determining 
how well the clustering algorithm has grouped similar data points together while keeping the clusters well separated from each other. 
A lower NGMD value indicates that the clustering algorithm has produced a better clustering solution. 
Therefore, NGMD can be an important tool in evaluating clustering algorithms and comparing different clustering solutions.

# Mathematical Intuition
Let $X$ be a dataset with n data points, and let $C$ be a clustering of $X$ into $k$ clusters. Let ci be the centroid of cluster i, and let $d(ci, cj)$ be the Euclidean distance between centroids $ci$ and $cj$.

The normalized geometric mean distance (NGMD) is defined as:

NGMD = $(1/max_dist) * (prod(d(ci, cj))^(1/((k*(k-1))/2)))$

where max_dist is the maximum pairwise distance between data points in X, and the product is taken over all pairs of distinct clusters $(i, j)$ such 
that $i < j$.

Proof:

Normalization: The NGMD metric is normalized by the maximum pairwise distance between data points in $X$, denoted by $max_dist$. This ensures that the metric is independent of the scale of the data, and allows for comparison of clustering results across datasets with different ranges of values.

Geometric mean: The NGMD metric takes the geometric mean of pairwise distances between cluster centroids. This measure of central tendency is more robust to outliers than the arithmetic mean, and gives equal weight to all pairwise distances, ensuring that each cluster contributes equally to the metric.

Pairwise distances: The NGMD metric considers pairwise distances between all distinct pairs of cluster centroids, denoted by $d(ci, cj)$, where $i < j$. This ensures that the metric captures the overall structure of the clustering, rather than just the distances between adjacent clusters.

Product over all pairs: The NGMD metric takes the product of all pairwise distances between cluster centroids, raised to the power of $1/((k*(k-1))/2)$. This normalization factor ensures that the metric is invariant to the number of clusters $k$, and adjusts for the fact that the number of pairwise distances grows quadratically with $k$.

Overall interpretation: The NGMD metric can be interpreted as the average distance between pairs of cluster centroids, normalized by the maximum pairwise distance between data points in $X$. A lower NGMD score indicates tighter and more well-separated clusters, while a higher NGMD score indicates more spread-out or overlapping clusters.
