# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 23:12:13 2018

@author: Srijita
"""
import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import Log_Reg as lmodel

datapath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Data\\"
logpath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"

def loadcsv(filename):
    dataset = np.genfromtxt(filename, delimiter=',',skip_header=1)
    return dataset

def return_train_label(data,start,end):
    
    train= data[:,start:end]
    label= data[:,data.shape[1]-1]
       
    return train,label

if __name__ == '__main__':
   weights=np.array([[ -93.443, 137.3618,  -231.492, 185.4486, -292.1066, -109.0404,  76.7217,  -152.6353]]) 
   intercept=162.5131
   alldata   =  loadcsv(datapath+"synthetic_data.csv")
   
   """Converting Obs data to train and label"""
   start=1;end=alldata.shape[1]
   train,label=return_train_label(alldata,start,end)
   learner=lmodel.Logit(0)
   learner.model.fit(train,label)
   print learner.model.coef_[0], learner.model.intercept_[0]
   
   