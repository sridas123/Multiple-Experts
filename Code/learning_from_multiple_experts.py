# -*- coding: utf-8 -*-
"""
Created on Thu Dec 06 00:38:31 2018

@author: Srijita
"""
"""This code is designed to learn from advice given by multiple experts on noisy regions"""
"""Parameters to infer are the weight vectors and the alpha values"""
import numpy as np
import csv
import random as rnd
number_of_experts=3
"""File locations"""
datapath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Data\\"
logpath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
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

if __name__ == '__main__':
    datatrain= loadcsv(datapath+noisy_traindata)
    datatest=loadcsv(datapath+testdata)
    datatrain_orig=loadcsv(datapath+traindata)
    dtrain,dtrain_label,dtrain_label_expert=splitdataset(datatrain)
    print "The shapes are",dtrain.shape,dtrain_label.shape, dtrain_label_expert.shape
    print dtrain_label_expert[0:10]