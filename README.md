pip install bayesKMeans==0.2.0

from bayeskmeans.bayes_kmeans import BayesKMeans
from bayeskmeans.bayes_visualize import BayesKMeansVisualize
from sklearn.datasets import make_blobs

data = make_blobs(n_samples=1000, n_features=2, centers=21, cluster_std=5, center_box=(-300, 300))
data = data[0]

bayesKMeans = BayesKMeans(data)

bayesKMeans.find_k()

print(bayesKMeans.found_k)

visual = BayesKMeansVisualize(bayesKMeans)
visual.show_bayesian_plot()
