import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer


cancer = load_breast_cancer()


cancer.keys()


print(cancer.DESCR)


print(cancer.feature_names)


print(cancer.target_names)


print(cancer.target)


FeatureDF = pd.DataFrame(data = cancer['data'], columns = cancer['feature_names'])


FeatureDF


from sklearn.model_selection import train_test_split

X = FeatureDF
y = cancer['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


from sklearn.svm import SVC


SVM = SVC()


SVM.fit(X_train, y_train)


predictions = SVM.predict(X_test)


from sklearn.metrics import classification_report, confusion_matrix



print(confusion_matrix(y_test, predictions))



print(classification_report(y_test, predictions))



from sklearn.model_selection import GridSearchCV



ParamGrid = {'C' : [0.1, 1, 10, 100, 1000], 'gamma' : [1, 0.1, 0.01, 0.001, 0.0001]}


grid = GridSearchCV(SVC(), param_grid = ParamGrid, verbose = 3)



grid.fit(X_train, y_train)



grid.best_params_



grid.best_estimator_



GridPredictions = grid.predict(X_test)



print(classification_report(y_test, GridPredictions))



ConfusionMatrix = confusion_matrix(y_test, GridPredictions)
print(ConfusionMatrix)



NormalizedConfusionMatrix = ConfusionMatrix.astype('float') / (np.reshape(ConfusionMatrix.sum(axis=1), (2,1)))


sns.heatmap(NormalizedConfusionMatrix, annot = True, cmap = 'coolwarm')
plt.xlabel('True Labels')
plt.ylabel('Predicted Labels')

