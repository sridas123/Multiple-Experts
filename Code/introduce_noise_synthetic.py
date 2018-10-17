# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 18:02:05 2018

@author: sxd170431
"""
import random as rnd
import csv
import numpy as np
import convert_rdn_format as rdn
trainpath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Synthetic_data_noise\\train\\"
testpath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Synthetic_data_noise\\test\\"
npath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Synthetic_data_noise\\"
fdata=npath+"data.csv"
results=npath+"results.txt"
datanoise=npath+"data_noise.csv"
train_fact="train_facts.txt"
train_pos="train_pos.txt"
train_neg="train_neg.txt"

def loadcsv(filename):
    
    dataset = np.genfromtxt(filename, delimiter=',',skip_header=1)
    return dataset

def convert_train_label(data):
    data_train=data[:,0:data.shape[1]-1]
    data_label=data[:,data.shape[1]-1]
    return data_train, data_label

"""This is the main module for noise introduction"""
if __name__ == '__main__':
   data= loadcsv(fdata)
   data_train,data_label=convert_train_label(data)
   print "The shape of data_tain,data_label", data_train.shape,data_label.shape
   
   train_array=[];train_pos_label=[];train_neg_label=[]
   test_array=[];test_pos_label=[];test_neg_label=[] 
   """Convert the data into rdn predicates"""
   for i in range(0,data_train.shape[0]):
        data=data_train[i]
        #print data
        a=data[0].astype(np.int64)
        #print type(data[0].astype(np.int64))
        b=data[1].astype(np.int64)
        c=data[2].astype(np.int64)
        #print a,b,c
        pid="Patientid("+str(a)+")."
        bp= "BP("+str(a)+","+str(b)+")."
        chol= "chol("+str(a)+","+str(c)+")."
        #age= "age("+str(data[0])+","+str(data[3])+")."
        #stress= "stress("+str(data[0])+","+str(data[4])+")."
        train_array.extend([pid,bp,chol])
        #print "data_label",data_label[i]
        d=data_label[i].astype(np.int64)
        if d==1:
           train_pos_label.append("HA("+str(a)+").") 
        else:   
           train_neg_label.append("HA("+str(a)+").")   
    
   """Writing the examples into necessary files"""
   fobj1 = open(trainpath+train_fact, "w") 
   fobj2 = open(trainpath+train_pos,  "w") 
   fobj3 = open(trainpath+train_neg,  "w") 
       
#    fobj4 = open(testpath+test_fact, "w") 
#    fobj5 = open(testpath+test_pos, "w") 
#    fobj6 = open(testpath+test_neg, "w") 
#       
   for line in train_array:
       fobj1.write(line+"\n")
   for line in train_pos_label:
       fobj2.write(line+"\n")
   for line in train_neg_label:
       fobj3.write(line+"\n")
#    for line in test_array:
#       fobj4.write(line+"\n")
#    for line in test_pos_label:
#       fobj5.write(line+"\n")
#    for line in test_neg_label:
#       fobj6.write(line+"\n")
       
   
  
       
       
   
   