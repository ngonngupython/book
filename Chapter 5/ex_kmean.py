from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
X, y = make_blobs(
    n_samples=250, n_features=2,
    centers=4, cluster_std=1,
    shuffle=True, random_state=15
)
plt.scatter(
    X[:,0], X[:,1],
    c=y, marker='o',
    edgecolors='blue', s = 10
)

plt.scatter(
    X[:,0], X[:,1],
    c=y, marker='o',
    edgecolors='blue', s = 10
)

kmeans = KMeans(n_clusters=4)
y_pred = kmeans.fit_predict(X)

print(kmeans.cluster_centers_)

plt.scatter(
    X[:,0], X[:,1],
    c=y_pred, marker='o',
    edgecolors='black', s = 10
)
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=100,       # Set centroid size
            c='red')     # Set centroid color

plt.show()

#---------
import numpy as np

kmeans = KMeans(n_clusters=3)
y_pred = kmeans.fit_predict(X)
h = 0.02  # point in the mesh [x_min, x_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    cmap=plt.cm.Paired,
    aspect="auto",
    origin="lower",
)

plt.plot(X[:,0], X[:,1], "k.", markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="x",
    s=169,
    linewidths=10,
    color="blue",
    zorder=10,
)
plt.title(
    "K-means clustering with k=3\n"
)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()

from sklearn.metrics import silhouette_score
import pandas as pd
print(silhouette_score(X,y_pred))

k_values = []
silhouette_score_values = []
for i in range(3,10):
   kmeans = KMeans(n_clusters=i)
   y_pred = kmeans.fit_predict(X)
   k_values.append(i)
   silhouette_score_values.append(silhouette_score(X,y_pred))

result = pd.DataFrame({'k':k_values, 'silhouette score':silhouette_score_values})
result.plot.line(x='k', y='silhouette score')
plt.show()

