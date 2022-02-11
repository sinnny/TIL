import matplotlib.pyplot as plt
import seaborn as sns ; sns.set()
import numpy as np
import pandas as pd
[ ]
from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples = 300, centers = 4, cluster_std = 0.60, random_state = 0)
plt.scatter(X[:, 0], X[:, 1], s = 50)

[ ]
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4)
kmeans.fit(X)
KMeans(n_clusters=4)
[ ]
y_kmeans = kmeans.predict(X)
[ ]
print(y_kmeans)
[2 1 3 1 2 2 0 3 1 1 0 1 3 1 2 3 3 2 0 0 2 2 3 0 0 3 2 3 0 3 1 1 3 1 1 1 1
 1 0 2 3 0 3 3 0 0 1 0 1 2 0 2 1 2 2 0 1 0 1 2 1 3 1 0 0 0 1 2 1 0 3 0 1 0
 0 1 0 3 2 1 2 3 2 2 1 3 2 3 1 1 3 2 1 0 0 3 2 2 3 0 1 2 1 2 3 2 2 3 1 3 0
 0 2 1 2 3 1 2 2 3 0 2 0 2 2 2 2 0 2 0 1 0 0 2 1 0 0 1 3 1 1 0 3 0 3 0 1 3
 1 1 1 3 1 3 2 0 1 0 2 3 1 3 3 2 3 0 0 3 2 3 3 1 2 3 0 1 2 2 3 0 2 3 0 0 3
 3 3 3 2 1 3 0 3 3 0 0 0 3 0 1 3 0 2 0 3 1 0 1 3 1 3 0 3 3 1 0 0 2 2 3 1 2
 2 0 2 0 3 1 1 3 3 1 3 2 0 3 2 0 1 0 2 3 2 1 1 1 1 0 0 1 3 0 2 3 0 0 0 2 2
 1 3 3 0 2 1 0 3 1 3 2 2 0 0 3 2 2 2 3 1 1 2 2 3 2 2 2 1 0 1 3 2 2 1 1 1 2
 2 3 1 0]
[ ]
plt.scatter(X[:,0], X[:,1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='black', s=200, alpha=0.5)

[ ]
from sklearn.datasets import make_moons
X, y = make_moons(200, noise=0.05, random_state = 0)
[ ]
labels = KMeans(2, random_state = 0).fit_predict(X)
plt.scatter(X[:,0], X[:,1], c=labels, s=50, cmap='viridis')

[ ]
from sklearn.datasets import load_digits
digits = load_digits()
digits.data.shape
(1797, 64)
[ ]
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 10, random_state=0)
clusters = kmeans.fit_predict(digits.data)
[ ]
kmeans.cluster_centers_.shape
(10, 64)
[ ]
fig, ax = plt.subplots(2, 5, figsize=(8, 3))
centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(ax.flat, centers):
  axi.set(xticks=[], yticks=[])
  axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)

[ ]
rng = np.random.RandomState(1)
X = np.dot(rng.rand(2,2), rng.randn(2, 200)).T
plt.scatter(X[:,0], X[:,1])
plt.axis('equal')


[ ]
from sklearn.decomposition import PCA
[ ]
mypca = PCA(n_components = 2)
mypca.fit(X)
PCA(n_components=2)
[ ]
print(mypca.components_)
[[-0.94446029 -0.32862557]
 [-0.32862557  0.94446029]]
[ ]
print(mypca.explained_variance_)
[0.7625315 0.0184779]
[ ]
def draw_vector(v0, v1, ax=None):
  ax = ax or plt.gca()
  arrowprops = dict(color='red',
                    arrowstyle = 'simple',
                    linewidth = 2,
                    shrinkA=0, shrinkB=0)
  ax.annotate('', v1, v0, arrowprops=arrowprops)

plt.scatter(X[:, 0], X[:,1], alpha=0.2)
for length, vector in zip(mypca.explained_variance_, mypca.components_):
  v = vector *3 * np.sqrt(length)
  draw_vector(mypca.mean_, mypca.mean_ + v)
plt.axis('equal')

[ ]
dimpca = PCA(n_components = 1)
dimpca.fit(X)
X_pca = dimpca.transform(X)
print('original shape: ', X.shape)
print('transfoemd shape: ', X_pca.shape)
original shape:  (200, 2)
transfoemd shape:  (200, 1)
[ ]
X_new = dimpca.inverse_transform(X_pca)
plt.scatter(X[:, 0], X[:, 1], alpha = 0.2)
plt.scatter(X_new[:, 0], X_new[:,1], alpha=0.8)
plt.axis('equal')

[ ]
from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people(min_faces_per_person=60)
print(faces.target_names)
print(faces.images.shape)
['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush'
 'Gerhard Schroeder' 'Hugo Chavez' 'Junichiro Koizumi' 'Tony Blair']
(1348, 62, 47)
[ ]
a
[1]
0초
from sklearn.decomposition import PCA
face_pca = PCA(150)
face_pca.fit(faces.data)

[ ]
fig, axes = plt.subplots(3, 8, figsize = (9, 4),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw = dict(hspace=0.1, wspace=0.1))

for i, ax in enumerate(axes.flat):
  ax.imshow(face_pca.components_[i].reshape(62, 47), cmap='bone')

[ ]
[ ]

