# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 13:14:57 2018

@author: sxd170431
"""
import numpy as np
import csv
import math
#datapath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Data\\"
#logpath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
datapath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Data\\"
logpath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
data=datapath+"synthetic_data.csv"

# This code induces some percentage of noise in the feature spaces that are learnt by the data based on the rules
noise_dict={'R1': 0.2,'R2': 0.3, 'R3': 0.4}
fdata="synthetic_data_noisy.csv"
def loadcsv(filename):
    dataset = np.genfromtxt(filename, delimiter=',',skip_header=1)
    return dataset

if __name__ == '__main__':
    
   alldata = loadcsv(data)
   print "The shape of alldata is",alldata.shape   
   
   # data points satisfying Rule1
   cond_R1=((alldata[:,0] ==0) & (alldata[:,1] ==1) & (alldata[:,3] ==0) & (alldata[:,4] ==1))
   Idx_R1=np.where(cond_R1)
   print Idx_R1[0][0:10]
   print "No. of points to be considered for noise", Idx_R1[0].shape[0]
   size=(int)(noise_dict['R1']*Idx_R1[0].shape[0])
   print "No. of noisy labels created",size
   randindices = np.random.choice(Idx_R1[0], size=size, replace=False, p=None)
   for i in randindices:
       alldata[i][4]=0
   
   #data points satisfying Rule2
   cond_R2=(alldata[:,0] ==1) & (alldata[:,2] ==1) & (alldata[:,4] ==1)
   Idx_R2=np.where(cond_R2)
   print "No. of points to be considered for noise", Idx_R2[0].shape[0]
   size=(int)(noise_dict['R2']*Idx_R2[0].shape[0])   
   print "No. of noisy labels created",size
   randindices = np.random.choice(Idx_R2[0], size=size, replace=False, p=None)
   for i in randindices:
       alldata[i][4]=0
       
   #data points satisfying Rule3
   cond_R3=cond_R3=(alldata[:,0] ==0) & (alldata[:,3] ==1) & (alldata[:,4] ==1)
   Idx_R3=np.where(cond_R3)
   print "No. of points to be considered for noise", Idx_R3[0].shape[0]
   size=(int)(noise_dict['R3']*Idx_R3[0].shape[0])   
   print "No. of noisy labels created",size
   randindices = np.random.choice(Idx_R3[0], size=size, replace=False, p=None)
   for i in randindices:
       alldata[i][4]=0
       
   """Writing file to .csv"""
   with open(datapath+fdata, 'wb') as csvfile:         
        csvwriter = csv.writer(csvfile, delimiter=',')
        for i in range(0,len(alldata)):
            csvwriter.writerow(alldata[i])