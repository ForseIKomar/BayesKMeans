Дипломный магистерский проект в университете ИТМО, 2022 год.

Суть - использование метода байесовской оптимизации для нахождения количества кластеров.

Итоговая библиотека позволяет найти оптимальное количество кластеров.

Пример получения числа кластеров:
```
    data = make_blobs(n_samples=5000, n_features=2, centers=127, cluster_std=4, center_box=(-300, 300))
    data = data[0]

from bayeskmeans.bayes_kmeans import BayesKMeans
    bayesKMeans = BayesKMeans(data)
    bayesKMeans.findK()
    print(bayesKMeans.foundK)
```

Пример визуализации:
```
from bayeskmeans.bayes_visualize import BayesKMeansVisualize
    visual = BayesKMeansVisualize(bayesKMeans)
    visual.showBayesianPlot()
```

