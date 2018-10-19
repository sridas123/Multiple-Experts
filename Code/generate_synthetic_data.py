# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:36:17 2018

@author: sxd170431
"""
import numpy as np
import random as rand
import csv
import math
import sys
#datapath="C:\\Users\\sxd170431\\Desktop\\Work\\Git\\Multiple-Experts\\Data\\"
datapath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Data\\"
logpath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
data_size=1000
no_of_feat=8
var_details_dict={'v1':0.5, 'v2': 0.4, 'v3': 0.5, 'v4': 0.5, 'v5': 0.5, 'v6': 0.2, 'v7': 0.6, 'v8':0.5}
fdata="synthetic_data.csv"

def calculate_sigmoid(weight, data):
    weightcrossdata=np.dot(weight,data)
    #print weightcrossdata
    prob=math.exp(weightcrossdata)/(1+math.exp(weightcrossdata))
    return prob
    
    return prob
if __name__ == '__main__':
    sys.stdout = open(logpath+'log_generate_synthetic_data.txt', 'w')
    """Generate the weight vector from a Gaussian Distribution"""
    mu=2;sigma=1
    weight=np.random.normal(mu, sigma, 8)
    weight=(np.expand_dims(np.asarray(weight),1)).T
    #print "Weight shape", weight.shape
    print "The true weight vector to be estimated is", weight
    data_all=[]
    for key, value in var_details_dict.iteritems():
        #print key,value
        sample_feat=np.random.binomial(1, value,data_size)  
        #print sample_feat
        data_all.append(sample_feat)
    data_all=np.asarray(data_all)
    data_all=data_all.T
    #print data_all
    
    """Generate the labels"""
    label=[]
    for i in range(0,data_all.shape[0]):
        data=np.expand_dims(data_all[i],1)
        prob=calculate_sigmoid(weight,data)
        if prob > 0.85:
           prob=1
        else:
           prob=0 
        label.append(prob)    
    label=np.expand_dims(np.asarray(label),1)   
    data_all=np.hstack((data_all,label))
    
    """Writing file to .csv"""
    with open(datapath+fdata, 'wb') as csvfile:         
        csvwriter = csv.writer(csvfile, delimiter=',')
        for i in range(0,len(data_all)):
            csvwriter.writerow(data_all[i])
       
    