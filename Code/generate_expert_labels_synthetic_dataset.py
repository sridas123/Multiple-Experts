# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:04:51 2018

@author: sxd170431
"""
"""This code generates the labels given by multiple experts according to their expertise in certain regions of the feature space"""
import numpy as np
import csv
import random as rnd

#datapath ="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Data\\"
#logpath  ="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
datapath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Data\\"
logpath="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Multiple-Experts\\Logfiles\\"
data=datapath+"synthetic_data.csv"
outdata=datapath+"synthetic_data_noisy_expert_label.csv"
noisy_data=datapath+"synthetic_data_noisy.csv"
#E1 is more expert than E3 E1> E2 > E3
expert_dict={'E1':0.7, 'E2': 0.2, 'E3': 0.1}
no_of_pnts_correctly_labelled=[]

def loadcsv(filename):
    dataset = np.genfromtxt(filename, delimiter=',',skip_header=1)
    return dataset

def generate_label_acc_expertise(alldata,Idx_R1):
    #This logic needs to be checked again, not correct
    all_expert_generated_label_each_rule=[]
    for key,value in expert_dict.iteritems():
       label_each_expert=[]
       print key,value
       """No. of labels to be correctly labelled by each expert"""
       size_labels= (int)((value) * Idx_R1[0].shape[0])
       print "Total labels to be generated in this space",Idx_R1[0].shape[0]
       print "The number of labels to be labelled correctly by expert", size_labels,key
       #no_of_pnts_correctly_labelled.append(size_labels)
       #for i in Idx_R1[0]:
       """Randomly pick indices from that feature region to be labelled correctly"""
       picked_ind_to_label_correctly=np.random.choice(Idx_R1[0], size=size_labels, replace=False, p=None)
       for j in range(0,alldata.shape[0]):
           if j in picked_ind_to_label_correctly:
              label=alldata[j][4]
           elif j in Idx_R1[0]: 
              if alldata[j][4]==0:
                 label=1
              else:
                 label=0 
           else: 
              continue      
           label_each_expert.append((j,label))
       print "Label each expert", len(label_each_expert)        
       all_expert_generated_label_each_rule.append(label_each_expert) 
       
    return all_expert_generated_label_each_rule

if __name__ == '__main__':
   alldata=loadcsv(data)  
   noisydata=loadcsv(noisy_data) 
   all_rule_data=[]
   consolidate_expert_labels={'F1':{},'F2':{},'F3':{}}
   
   #indices of data points satisfying rule 1
   cond_R1=(alldata[:,0] ==0) & (alldata[:,1] ==1) & (alldata[:,3] ==0) & (alldata[:,4] ==1)
   Idx_R1=np.where(cond_R1)
   print Idx_R1[0][0:10]
   #for i in Idx_R1[0][0:10]:
   #    print alldata[i]
   #print alldata[Idx_R1[0][1]]
   label_R1_crowd=generate_label_acc_expertise(alldata,Idx_R1)
   all_rule_data.append(label_R1_crowd)
         
   #indices of data points satisfying rule 2
   cond_R2=(alldata[:,0] ==1) & (alldata[:,2] ==1) & (alldata[:,4] ==1)
   Idx_R2=np.where(cond_R2)
   label_R2_crowd=generate_label_acc_expertise(alldata,Idx_R2)
   all_rule_data.append(label_R2_crowd)
   
   #indices of data points satisfying rule 3
   cond_R3=(alldata[:,0] ==0) & (alldata[:,3] ==1) & (alldata[:,4] ==1)
   Idx_R3=np.where(cond_R3)
   label_R3_crowd=generate_label_acc_expertise(alldata,Idx_R3)
   all_rule_data.append(label_R3_crowd)
   #print 'The length are',  len(all_rule_data[0]), len(all_rule_data[1]), len(all_rule_data[2])
   #print "Length choice", Idx_R1[0].shape, len(all_rule_data[0][0]),len(all_rule_data[0][1]),len(all_rule_data[0][2])
   """Consolidate all the expert labels generated"""
   for i in range(0,len(all_rule_data)):
       label_dict={}
       each_feature_region_labels=all_rule_data[i]
       each_feat_reg_E1=each_feature_region_labels[0]
       each_feat_reg_E3=each_feature_region_labels[1]
       each_feat_reg_E2=each_feature_region_labels[2]
       for j in range(0,len(each_feat_reg_E1)):
           label_array=[] 
           idx=each_feat_reg_E1[j][0]
           #print idx
           label=each_feat_reg_E1[j][1]
           #print label
           if ((idx== each_feat_reg_E2[j][0]) and (idx==each_feat_reg_E3[j][0])):
              label_array.extend((each_feat_reg_E1[j][1],each_feat_reg_E2[j][1],each_feat_reg_E3[j][1])) 
              label_dict[idx]=label_array
           else: print '*******************************ERROR'   
       consolidate_expert_labels['F'+str(i+1)]=label_dict   
          
   print consolidate_expert_labels['F1']
   """Write all the multiple expert generated data in a file to be used by multiple expert algorithm"""
   #fobj = open(outdata, "w") 
   #for i in range(0:noisydata.shape[0]):
   #    record=noisydata
       
   