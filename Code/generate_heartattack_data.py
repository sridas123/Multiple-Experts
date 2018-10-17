# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 18:35:30 2018

@author: sxd170431
"""
"""This is a code to generate a syntehtic dataset for the crowd of experts problem"""
import random as rnd
import csv
import numpy as np
import convert_rdn_format as rdn
data=[]
no_of_points=100
rule1_pat=[]
rule2_pat=[]
rule3_pat=[]
label_data=[]
trainpath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Synthetic_data\\train\\"
testpath="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Synthetic_data\\test\\"
fdata="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Synthetic_data\\data.csv"
train_fact="train_facts.txt"
train_pos="train_pos.txt"
train_neg="train_neg.txt"
test_fact="test_facts.txt"
test_pos="test_pos.txt"
test_neg="test_neg.txt"

if __name__ == '__main__':
   print "I am starting" 
   data_skeleton={'BP':[1,2],'Chol':[1,2]}
   for i in range(0,no_of_points):
       data.append([(i+1)])
   
   """Generate random 100 data points with different values"""
   for i in range(0,100):
       data_feat=data[i]
       data_feat.extend([rnd.randint(1,2),rnd.randint(1,2)])
   
   """Define the probabilities of the rules""" 
   rule1_prob=0.1
   rule2_prob=0.4
   rule3_prob=0.7
   rule4_prob=0.9
    
   for i in range(0,100):
       data_feat=data[i]
       print data_feat
       if (data_feat[1]==2 and data_feat[2]==2):
          label=np.random.binomial(1,   rule1_prob)
       elif (data_feat[1]==2 and data_feat[2]==1):  
            label=np.random.binomial(1, rule2_prob)
       elif (data_feat[1]==1 and data_feat[2]==2):  
            label=np.random.binomial(1, rule3_prob)
       elif (data_feat[1]==1 and data_feat[2]==1): 
            label=np.random.binomial(1,  rule4_prob)
       label_data.append(label)
            
   pos=0;neg=0    
   for i in range(0,len(label_data)):
       if label_data[i]==1:
          pos=pos+1
       else:
          neg=neg+1 
          
   print "The number of pos and neg are", pos,neg   
   #print data[0:10]
   data=np.asarray(data)
   label_data=np.asarray(label_data)
   print label_data
   print data
   print data.shape,label_data.shape
   label_data1=np.expand_dims(label_data, axis=1)
   print data.shape,label_data.shape
   final_data=np.hstack((data,label_data1))
   print "The shape of final data is", final_data.shape
   
   with open(fdata, 'wb') as csvfile:         
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["Pid","BP","Cho","HA"])
        for i in range(0,len(final_data)):
            csvwriter.writerow(final_data[i])
            
   rdn.convert_format(data,label_data,trainpath, testpath, train_fact, train_pos, train_neg, test_fact, test_pos, test_neg)   
   
   
       
       
       
       
       
       
       
       
       
       
       
       
       
       
      