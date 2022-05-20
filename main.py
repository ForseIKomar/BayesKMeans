from BayesKMeans import BayesKMeans
from BayesKMeansVisualize import BayesKMeansVisualize

from sklearn.datasets import make_blobs


if __name__ == '__main__':
    data = make_blobs(n_samples=5000, n_features=2, centers=127, cluster_std=4, center_box=(-300, 300))
    data = data[0]
    bayesKMeans = BayesKMeans(data)
    bayesKMeans.findK()
    print(bayesKMeans.foundK)

    visual = BayesKMeansVisualize(bayesKMeans)
    visual.showBayesianPlot()
