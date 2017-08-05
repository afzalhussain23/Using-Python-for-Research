# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:02:04 2017

@author: illusory_time
"""

numeric_data = (numeric_data - np.mean(numeric_data)) / np.std(numeric_data)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)