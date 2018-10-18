# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:49:42 2018

@author: sxd170431
"""
import numpy as np
import matplotlib.pyplot as plt
mu=2.5
sigma=1
s = np.random.normal(mu, sigma, 8)
print s
count, bins, ignored = plt.hist(s, 8, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()