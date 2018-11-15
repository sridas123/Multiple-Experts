# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:04:51 2018

@author: sxd170431
"""
import numpy as np
import csv

datapath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Data\\"
logpath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
data=datapath+"synthetic_data.csv"
#datapath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Data\\"
#logpath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
noisy_data=datapath+"synthetic_data_noisy.csv"
#E1 is more expert than E3 E1> E2 > E3
expert_dict={'E1':0.6, 'E2': 0.3, 'E3': 0.1}

def loadcsv(filename):
    dataset = np.genfromtxt(filename, delimiter=',',skip_header=1)
    return dataset

if __name__ == '__main__':
   alldata=loadcsv(data)  
   noisydata=loadcsv(noisy_data) 
   
   #indices of data points satisfying rule 1
   cond_R1=(alldata[:,0] ==0) & (alldata[:,1] ==1) & (alldata[:,3] ==0) & (alldata[:,4] ==1)
   Idx_R1=np.where(cond_R1)
   
   
   #indices of data points satisfying rule 2
   cond_R2=(alldata[:,0] ==1) & (alldata[:,2] ==1) & (alldata[:,4] ==1)
   Idx_R2=np.where(cond_R2)
   
   #indices of data points satisfying rule 3
   cond_R3=(alldata[:,0] ==0) & (alldata[:,3] ==1) & (alldata[:,4] ==1)
   Idx_R3=np.where(cond_R3)
   
    