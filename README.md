Дипломный магистерский проект в университете ИТМО, 2022 год.

Суть - использование метода байесовской оптимизации для нахождения количества кластеров.

Итоговая библиотека позволяет найти оптимальное количество кластеров.

Пример получения числа кластеров:
```python
from bayeskmeans.bayes_kmeans import BayesKMeans
    bayesKMeans = BayesKMeans(data)
    bayesKMeans.findK()
    print(bayesKMeans.foundK)
```

Пример визуализации:
```python
from bayeskmeans.bayes_visualize import BayesKMeansVisualize
    visual = BayesKMeansVisualize(bayesKMeans)
    visual.showBayesianPlot()
```

https://pypi.org/project/bayesKMeans/
