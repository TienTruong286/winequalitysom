# -*- coding: utf-8 -*-
"""Wine Quality Classification Using SOM

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dOLCXxqOInbRLDeqlMnfccVuOhSdQk-A
"""

pip install MiniSom

from minisom import MiniSom

import numpy as np
import pandas as pd

data["quality"] = data["quality"].apply(lambda x: 1 if x >= 7 else 0)

X = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0,1))
X = sc.fit_transform(X)

X.shape

som = MiniSom(x = 10, y=10, input_len = 11, sigma = 1.0, learning_rate = 0.5)

som.random_weights_init(X)
som.train_random(data = X, num_iteration = 120)

from pylab import bone,pcolor,colorbar,plot,show

bone()
T = np.transpose(som.distance_map())
pcolor(T)
colorbar()


marker = ['o', 's']
colors = ['r', 'g']

for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[1] + 0.5, w[0] + 0.5, marker[y[i]], markeredgecolor=colors[y[i]], markeredgewidth=2, markersize=10,markerfacecolor = None)

mappings = som.win_map(X)
quality = mappings[1,6]
quality = sc.inverse_transform(quality)


# Get the feature names
feature_names = list(data.columns)[:-1]

# Create the dataframe with feature names as columns
dataframe_not_quality_wine_features = pd.DataFrame(quality, columns=feature_names)

# Display the dataframe
dataframe_not_quality_wine_features

dataframe_not_quality_wine_features.describe()

data.describe()



