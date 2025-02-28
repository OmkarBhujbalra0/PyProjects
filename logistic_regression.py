# -*- coding: utf-8 -*-
"""Logistic Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/142dDGb3ZiMRbDcCW5577xwKgk2OVp9t-
"""

from sklearn.datasets import load_iris

iris = load_iris()
print("Feature Names:",iris.feature_names)
print("Target Names",iris.target_names)

import pandas as pd

df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['species'] = iris.target
df.head()

from sklearn.model_selection import train_test_split

X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

from sklearn.metrics import classification_report,confusion_matrix

y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test,y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test,y_pred))