# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:36:17 2018

@author: sxd170431
"""
import numpy as np
import random as rand
import csv
#import sys
datapath="C:\\Users\\sxd170431\\Desktop\\Work\\Git\\Multiple-Experts\\Data\\"
data_size=1000
no_of_feat=8
var_details_dict={v1:0.5, v2: 0.4, v3: 0.5, v4: 0.5, v5: 0.5, v6: 0.2, v7: 0.6, v8:0.5}
if __name__ == '__main__':
    """Generate the weight vector from a Gaussian Distribution"""
    mu=2, sigma=1
    weight=np.random.normal(mu, sigma, 8)
    print "The true weight vector is", weight
    data_all=[]
    for key, value in var_details_dict.iteritems():
    sample_feat=np.random.binomial(data_size, value)    
    data_all.append(sample_feat)
    data_all
     
    