# -*- coding: utf-8 -*-
"""ROCK VS MINE prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DTT6L2smZRq2z7_3FWB9e9_ykE1_GUAH

Importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""data collection and processing"""

#loading the dataset to a pandas dataframe
sonar_data = pd.read_csv('/content/ sonar data.csv', header=None)

sonar_data.head()

#number of rows and culums
sonar_data.shape

sonar_data.describe() #describe--->statistical measures of the data

sonar_data[60].value_counts()
