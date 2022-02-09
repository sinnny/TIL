import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

data = pd.read_csv('weather.csv')
data

from sklearn.naive_bayes import MultinomialNB

multinomial_model = MultinomialNB()
multinomial_model

outlook_dic = {'overcast':0, 'rainy':1, 'sunny':2}
temperature_dic = {'cool':0, 'hot':1, 'mild':2}
humidity_dic = {'high':0, 'normal':1}
windy_dic = {False:0, True:1}

data['outlook'] = data['outlook'].map(outlook_dic)
data['temperature'] = data['temperature'].map(temperature_dic)
data['humidity'] = data['humidity'].map(humidity_dic)
data['windy'] = data['windy'].map(windy_dic)

data

multinomial_model.fit(data.iloc[:,:4], data['play'])

multinomial_model.predict([[1, 2, 0, 1]])

multinomial_model.predict_proba([[2, 2, 0, 1]])

from sklearn.datasets import load_iris
iris = load_iris()

iris_df = pd.DataFrame(iris.data, columns = iris.feature_names)
iris_df['species'] = iris.target
iris_df

from sklearn.naive_bayes import GaussianNB
gaussian_model = GaussianNB()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris_df.iloc[:, :4],
                                                    iris_df['species'],
                                                    test_size = 0.33)

gaussian_model.fit(X_train, y_train)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, gaussian_model.predict(X_test)))

print(confusion_matrix(y_test, gaussian_model.predict(X_test)))

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf

clf.fit(data.iloc[:, :4], data['play'])

clf.predict([[2, 2, 0, 1]])

clf.predict([[1, 2, 0, 1]])