import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs




data = make_blobs(n_samples = 200, n_features = 2, centers = 4, cluster_std = 1.8, random_state = 101)



data[0]



data[1]



data[0].shape



plt.scatter(data[0][:,0], data[0][:,1], c = data[1], cmap = 'rainbow')
plt.show()



from sklearn.cluster import KMeans


kmeans = KMeans(n_clusters = 4)


kmeans.fit(data[0])



kmeans.cluster_centers_



labels = kmeans.labels_
labels



plt.figure(figsize=(15,8))

plt.subplot(1, 2, 1).scatter(data[0][:,0], data[0][:,1], c = data[1], cmap = 'rainbow')
plt.title('Original')


plt.subplot(1, 2, 2).scatter(data[0][:,0], data[0][:,1], c = labels, cmap = 'rainbow')
plt.title('K Means')


plt.show()

