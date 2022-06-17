import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets



iris = datasets.load_iris()


iris.keys()


iris['data']


iris['target']



X = iris.data[:, :2]
y = iris.target



from sklearn.model_selection import train_test_split



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


KNN = neighbors.KNeighborsClassifier(n_neighbors=5)
KNN.fit(X_train, y_train)



predict = KNN.predict(X_test)
predict



from sklearn.metrics import classification_report, confusion_matrix



print(confusion_matrix(y_test, predict))



print(classification_report(y_test, predict))



ErrorRate = []

for i in range(1, 40):
    KNN = neighbors.KNeighborsClassifier(n_neighbors = i)
    KNN.fit(X_train, y_train)
    PredictI = KNN.predict(X_test)
    ErrorRate.append(np.mean(PredictI != y_test))
    




plt.plot(range(1, 40), ErrorRate, color = 'blue', linestyle = '--', marker = 'o', markerfacecolor = 'red', markersize = 10)
plt.title('Erro Rate Vs K Values')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()




KNN = neighbors.KNeighborsClassifier(n_neighbors=9, weights = 'uniform')
KNN.fit(X_train, y_train)
predict = KNN.predict(X_test)

print(confusion_matrix(y_test, predict))
print(classification_report(y_test, predict))

