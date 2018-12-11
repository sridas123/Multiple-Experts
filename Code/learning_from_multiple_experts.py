from __future__ import division 
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 06 00:38:31 2018

@author: Srijita
"""
"""This code is designed to learn from advice given by multiple experts on noisy regions"""
"""Parameters to infer are the weight vectors and the alpha values"""
import EM_multiple_experts as algs
import numpy as np
import csv
import random as rnd
import sys
number_of_experts=3

"""File locations"""
#datapath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Data\\"
#logpath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
"""Office Path Locations"""
datapath ="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Data\\"
logpath  ="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
"""Data set names"""
noisy_traindata="synthetic_data_noisy_expert_label.csv"
testdata="synthetic_data_test.csv"
traindata="synthetic_data_expert_label.csv"
"""This is the main program"""
def loadcsv(filename):
    dataset = np.genfromtxt(filename, delimiter=',')
    return dataset

def splitdataset(data):
    dataframe_len=data.shape[1]-number_of_experts
    Xtrain=data[:,0:dataframe_len-1]
    Xtrain_label=data[:,dataframe_len-1]
    Xtrain_label_expert=data[:,dataframe_len:data.shape[1]]
    return Xtrain,Xtrain_label,Xtrain_label_expert

def splitdataset1(data):
    #print "THe shape is", data.shape
    dataframe_len=data.shape[1]-number_of_experts
    Xtrain=data[:,0:dataframe_len-1]
    Xtrain_label=data[:,dataframe_len-1]
    return Xtrain,Xtrain_label

def getaccuracy(ytest, predictions):
    correct = 0
    for i in range(len(ytest)):
        if ytest[i] == predictions[i]:
            correct += 1
    return (correct/float(len(ytest))) * 100.0

if __name__ == '__main__':
    
    sys.stdout = open('log1_ME.txt', 'w')
    datatrain= loadcsv(datapath+noisy_traindata)
    datatest=loadcsv(datapath+testdata)
    datatrain_orig=loadcsv(datapath+traindata)
    dtrain,dtrain_label,dtrain_label_expert=splitdataset(datatrain)
    dtrain_orig,dtrain_label_orig=splitdataset1(datatrain_orig)
    #print "The shapes are",dtrain.shape,dtrain_label.shape, dtrain_label_expert.shape
    parms={'regwt':0,'type':"None"}
    learner=algs.EM_Logit(parms)    
    learner.learn(dtrain,dtrain_label, dtrain_label_expert,number_of_experts)
    sys.stdout.close()
    #learner1=algs.EM_Logit(parms)
    #learner1.learn(dtrain,dtrain_label)
    #learner2=algs.EM_Logit(parms)
    #learner2.learn(dtrain_orig,dtrain_label_orig)