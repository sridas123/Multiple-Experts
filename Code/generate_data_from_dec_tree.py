# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:35:30 2018

@author: sxd170431
"""
"""This is a code to generate a synthetic dataset for the crowd of experts problem"""
import random as rnd
import csv
import sys
import numpy as np
data_size=(int)(sys.argv[1])
no_of_feat=4
var_details_dict={'v1':0.5,'v2':0.5,'v3':0.5,'v4':0.5}
datapath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Data\\"
logpath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
#datapath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Data\\"
#logpath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
fdata="synthetic_data.csv"

if __name__ == '__main__':
   data_all=[]
   for key, value in var_details_dict.iteritems():
        sample_feat=np.random.binomial(1, value,data_size)  
        data_all.append(sample_feat)
   data_all=np.asarray(data_all)
   data_all=data_all.T
   print "The shape of data_all is", data_all.shape
   
   #3 rules are induced in this code
   #R1: V1=0 ^ V2=1 -> P(y=1|Pa(y))=0.75
   #R2: V1=1 ^ V3=1 -> P(y=1|Pa(y))=0.6
   #R3: V1=0 ^ V2=0 ^ v4=1 -> P(y=1|Pa(y))=0.9
   # Rest all rules have 0.3 probability of being true
   
   R1_prob=0.8; R2_prob=0.6; R3_prob=0.9
   ylabel=[]
   
   """Generate the labels of the data according to the underlying rules"""
   for i in range(0, data_all.shape[0]):
       data=data_all[i]
       if (data[0]==0 and data[1]==1):
          y_label= np.random.binomial(1, R1_prob,1)
       elif   (data[0]==1 and data[2]==1):
              y_label= np.random.binomial(1, R2_prob,1)
       elif    (data[0]==0 and data[1]==0  and data[3]==1):     
              y_label= np.random.binomial(1, R3_prob,1) 
       else:
           y_label=np.random.binomial(1, 0.3,1)
       ylabel.append(y_label)    
   ylabel=np.asarray(ylabel)
   final_data=np.hstack((data_all,ylabel))
   print "final_data shape", final_data.shape
    
   """Writing file to .csv"""
   with open(datapath+fdata, 'wb') as csvfile:         
        csvwriter = csv.writer(csvfile, delimiter=',')
        for i in range(0,len(final_data)):
            csvwriter.writerow(final_data[i])
       
       
       
       
       
       
       
       
       
       
       
      