# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:49:42 2018

@author: sxd170431
"""
import numpy as np
import matplotlib.pyplot as plt
sri=np.array([[1,2,3],[4,2,3],[1,3,4],[9,2,3]])
print sri
#print np.where(sri[sri[:,1]==2])
#print np.where((sri[:,1]==2))
cond= (sri[:,1]==2) & (sri[:,2]==3)
print cond
Idx= np.where(cond)
print Idx[0]
a=np.array([1,2,3,4,5,6,7,8,9,20])
print np.random.choice(a, size=3, replace=False, p=None)