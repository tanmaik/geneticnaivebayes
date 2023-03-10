from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np

X = np.loadtxt(open("credit_approved_headings_weka.csv", "rb"), delimiter=",", usecols=range(14), skiprows=1, dtype=int)
y = np.loadtxt(open("credit_approved_headings_weka.csv", "rb"), delimiter=",", usecols=range(14,15), skiprows=1, dtype=int)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, stratify=y, test_size=0.3)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)

print("\nTest accuracy " + str(round(accuracy_score(y_test, y_pred) * 100)) + "%")
print("\nConfusion matrix:")
print(confusion_matrix(y_test, y_pred))
print()