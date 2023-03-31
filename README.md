# Normalized Geometric Mean Distance NGMD
Normalized Geometric Mean Distance (NGMD) - Unique Clustering Metric

The NGMD metric provides a measure of the quality of clustering by calculating the geometric mean of the pairwise distances between the centroids of the clusters, 
normalized by the distance between the two farthest points in the dataset. This metric is useful in determining 
how well the clustering algorithm has grouped similar data points together while keeping the clusters well separated from each other. 
A lower NGMD value indicates that the clustering algorithm has produced a better clustering solution. 
Therefore, NGMD can be an important tool in evaluating clustering algorithms and comparing different clustering solutions.

Proof:\\
\\
Let X be a dataset of n points in d-dimensional space and let $C = {C_1, C_2, \ldots C_k}$ be a clustering of X into k clusters. The NGMD metric is defined as follows:\\
\\
First, the centroids of the k clusters are computed:\\
$c_i = (1 / |C_i|) * \sum(x \in C_i) x$,\\
where $|C_i|$ is the number of points in cluster $C_i$ and $sum(x \in C_i)$ x is the sum of all points in cluster $C_i$.\\
\\
Next, the pairwise distances between the centroids are calculated:\\
$d_ij = ||c_i - c_j||$\\
where $||.||$ denotes the Euclidean distance between two points.\\
\\
The geometric mean of these pairwise distances is then computed:\\
$G = (\prod_{i<j} d_ij)^{1 / {k \choose 2}}$,\\
where $k \choose 2$ is the binomial coefficient that counts the number of pairwise distances between the k centroids.\\
\\
Finally, the NGMD metric is obtained by normalizing the geometric mean by the distance between the two farthest points in $X$:\\
$NGMD = G / max_{x,y \in X} ||x - y||$,\\
where $max_{x,y \in X} ||x - y||$ is the maximum pairwise distance between any two points in X.\\
\\
This normalization step ensures that the NGMD metric is always between 0 and 1, where a value of 1 indicates perfect clustering and a value of 0 indicates random clustering.
