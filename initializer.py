from Gradient import WeightedNB
from sklearn import datasets
import sys
import numpy as np
breast = datasets.load_breast_cancer()
X = breast.data
y = breast.target

X = np.loadtxt(open("undiscretized.csv", "rb"), delimiter=",", usecols=range(14), skiprows=1, dtype=float)
y = np.loadtxt(open("undiscretized.csv", "rb"), delimiter=",", usecols=range(14,15), skiprows=1, dtype=int)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)
wnb = WeightedNB(step_size=1e-2, max_iter=25)
wnb.fit(X_train, y_train)
y_pred = wnb.predict(X_test)
from sklearn import metrics
print("Weighted Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
c_matrix = metrics.confusion_matrix(y_test, y_pred)
print(c_matrix)