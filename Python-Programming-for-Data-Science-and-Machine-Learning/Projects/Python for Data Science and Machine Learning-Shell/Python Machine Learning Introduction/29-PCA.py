import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer


cancer = load_breast_cancer()


cancer.keys()


df = pd.DataFrame(data = cancer.data, columns = cancer.feature_names)



df.head()



from sklearn.preprocessing import StandardScaler



scaler = StandardScaler()



scaler.fit(df)


ScaledData = scaler.transform(df)


ScaledData



from sklearn.decomposition import PCA



pca = PCA(n_components = 2)



pca.fit(ScaledData)



XPCA = pca.transform(ScaledData)
x = pca.transform(cancer.data)



ScaledData.shape



XPCA.shape



plt.figure(figsize = (8,6))

plt.scatter(XPCA[:,0], XPCA[:,1], c = cancer.target)
plt.xlabel('First Priciple Component')
plt.ylabel('Second Priciple Component')

plt.show()



plt.figure(figsize = (8,6))

plt.scatter(x[:,0], x[:,1], c = cancer.target)
plt.xlabel('First Priciple Component')
plt.ylabel('Second Priciple Component')

plt.show()





