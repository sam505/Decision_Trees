# -*- coding: utf-8 -*-
"""Decision_Trees.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nZBa9MHToC1hHKIaPMBBIXDtOEv0XUhR

## Importing necessary packages

The required packages for this task will be pandas that has been used for loading the csv dataset, numpy to perform matrix operations and scikit-learn to define out training algorithm, split the dataset, and test the performance of the decision tree algorithm
"""

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

"""## Loading Dataset

We start by importing the csv file from an online database using pandas. The dataset has been downloaded from the University of California Irvine (UCI) Machine Learning (ML) Repository which contains numerous data generators, domain theories and dababases to be used by machine mearning practioners to test their machine learning algorithms.
"""


def import_data():
    data = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-' +
        'databases/balance-scale/balance-scale.data',
        sep=',', header=None)

    # Printing the shape of the dataset
    print("Dataset Length: ", len(data))
    print("Dataset Shape: ", data.shape)

    # Printing the obseravtions of the dataset 
    print("Dataset Head: ", data.head())
    return data


"""## Splitting Dataset

The next step after loading the dataset is to split it into data and labels. The data and labels are also split into the train and test sets. The train set is specifically for training the decision tree classifier for our data and later the test set will be used to test the accuracy of out decision tree algorithm.
"""


def split_dataset(balance_data):
    # Separating the target variable
    X = balance_data.values[:, 1:5]
    Y = balance_data.values[:, 0]

    # Splitting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.3, random_state=100)

    return X, Y, X_train, X_test, y_train, y_test


"""## Training our algorithms

For this task, I decided to train and test two different decision tree approaches, that is, train using entropy and train using gini. For both approaches there are contant configurations that I have set such as: the random state is 100, max depth will be 3, minimum sample leafs are 5. The different thing is the criterion used to train the decision tree  classifier. When usig entropy, I used the criterion variable as "entropy" and "gini" when training the classifier using Gini Index. The purpose of these two is to calculate the information gain useful when splitting a node. The both measure the impurity of a node in the essence that if a node has multiple classes it is classified as impure while that having only one class is pure. Below are the formulas used to caculate the impurity of a node for each of the two approches.

$$
\begin{aligned}
\text { Gini }=1 &-\sum_{i=1}^{n} p^{2}\left(c_{i}\right) 
\end{aligned}
$$

$$
\begin{aligned}
\text { Entropy } &=\sum_{i=1}^{n}-p\left(c_{i}\right) \log _{2}\left(p\left(c_{i}\right)\right)
\end{aligned}
$$

Defining the function for training with the Decision Tree algorithm using the entropy criterion.
"""


def train_using_entropy(X_train, X_test, y_train):
    """
    Function to perform training with entropy
    """
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy", random_state=100,
        max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy


"""Defining the function for training the Decision Tree algorithm using the Gini Index criterion."""


def train_using_gini(X_train, X_test, y_train):
    """
    Function to perform training with giniIndex
    """
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion="gini",
                                      random_state=100, max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini


"""Created a function to take in the classifier algorithm and also the test dataset and make predictions."""


def prediction(X_test, clf_object):
    """
    Function to make predictions
    """
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)

    return y_pred


"""This function takes the test labels and the predictions made by the decision tree model and compares them to get the values for the accuracy, confusion matrix and the general report."""


def calculate_accuracy(y_test, y_pred):
    """
    Function to calculate accuracy
    """
    print("Accuracy : {}\n".format(accuracy_score(y_test, y_pred) * 100))
    print("Confusion Matrix: {}\n".format(confusion_matrix(y_test, y_pred)))
    print("Report : {}\n".format(classification_report(y_test, y_pred)))


"""Calling the funtions for loading the dataset and splitting it into train and test sets."""

data = import_data()
X, Y, X_train, X_test, y_train, y_test = split_dataset(data)

"""### Entropy Approach"""

entropy_classifier = train_using_entropy(X_train, X_test, y_train)

print("Results Using Entropy Approach\n")

# Getting predictions using the entropy approach
entropy_y_pred = prediction(X_test, entropy_classifier)
calculate_accuracy(y_test, entropy_y_pred)

"""### Gini Index Approach"""

gini_classifier = train_using_gini(X_train, X_test, y_train)

print("Results Using Gini Index Approach\n")

# Getting prediction using Gini Index approach
gini_y_pred = prediction(X_test, gini_classifier)
calculate_accuracy(y_test, gini_y_pred)

"""## Results

Using the dataset obtained from UCI database, the decisin tree agorithm tained using the entropy approach had an accuracy of $\text{70.74%}$ while the on etrained with the Gini Index approach it had an accuracy of $\text{73.40%}$. For this case scenario I would train the classifier using the Gini Index approach because it has better accuracy results. The Gini Index approach also achieve better results whe it comes to the recall and precision. This makes it bes suited for this dataset. 

For better utilization of the code and to avoid rewritting the code for each trainig approach done, I defined functions that will be called when training, running predictions and also when calculating the results for each traiing approach. This is a best coding practice to reuse code for each scenario in the program. It also makes the code neater and easy to follow and understand the flow.
"""
