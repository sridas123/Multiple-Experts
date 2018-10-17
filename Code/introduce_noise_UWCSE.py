# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 19:53:52 2018

@author: Srijita
"""
from __future__ import division # floating point division
import numpy as np
#path="D:\\Grad Studies\\SRL\\Crowd_of_experts\\UWCSE_ILP2016\\Fold1\\train\\"
path="C:\\Users\\sxd170431\\Desktop\\Work\\Projects\\Crowd_of_experts\\UWCSE_ILP2016\\Fold1\\train\\"
pfile="train_pos.txt"
nfile="train_neg.txt"
noise_percent=10
#filename=path+'output_neg.txt'
pos_array=[]
neg_array=[]
pos_true_array=[];pos_false_array=[]
neg_true_array=[];neg_false_array=[]
pos_true_filename="pos_true_rule_groundings"
pos_false_filename="pos_false_rule_groundings"
neg_true_filename="neg_true_rule_groundings"
neg_false_filename="neg_false_rule_groundings"
#print filename
#satground=[]
#unsatground=[]
if __name__ == '__main__':
    
    """Read the required Input files"""
    fobj = open(path+pfile, "r")
    for line in fobj:
        pos_array.append(line.strip())
    fobj.close()
    
    fobj = open(path+nfile, "r")
    for line in fobj:
        neg_array.append(line.strip())
    fobj.close()  
    
    fobj = open(pos_true_filename, "r")
    for line in fobj:
        pos_true_array.append(line.strip())
    fobj.close()  
    
    fobj = open(pos_false_filename, "r")
    for line in fobj:
        pos_false_array.append(line.strip())
    fobj.close()  
    
    fobj = open(neg_true_filename, "r")
    for line in fobj:
        neg_true_array.append(line.strip())
    fobj.close()  
    
    fobj = open(neg_false_filename, "r")
    for line in fobj:
        neg_false_array.append(line.strip())
    fobj.close()  
        
    print "The size is", len(pos_array), len(neg_array),len(pos_true_array),len(pos_false_array),len(neg_true_array),len(neg_false_array)

    """Introduce noise"""
    
    pos_true_size=len(pos_true_array)
    noise_elem_size=(int)(noise_percent/100 * pos_true_size)
    list_random=np.random.choice(pos_true_size, noise_elem_size)
    print list_random
    for idx in list_random:
        if (pos_true_array[idx] not in neg_array):
           neg_array.append(pos_true_array[idx])
           print pos_true_array[idx]
           if (pos_true_array[idx] in pos_array):
           #if ("advisedBy(person212,person180)" in pos_array):
               print "Found in pos_array" 
               pos_array.remove(pos_true_array[idx])
           
    pos_false_size=len(pos_false_array)
    noise_elem_size=(int)(noise_percent/100 * pos_false_size)
    list_random=np.random.choice(pos_false_size, noise_elem_size)
    print list_random
    for idx in list_random:
        if pos_false_array[idx] not in pos_array:
           pos_array.append(pos_false_array[idx])
           if pos_false_array[idx] in neg_array:
              neg_array.remove(pos_false_array[idx])  
           
    neg_false_size=len(neg_false_array)
    print "neg_false_size", neg_false_size
    noise_elem_size=(int)(noise_percent/100 * neg_false_size)
    list_random=np.random.choice(neg_false_size, noise_elem_size)
    print list_random
    for idx in list_random:
        if neg_false_array[idx] not in pos_array:
           pos_array.append(neg_false_array[idx])
           if  neg_false_array[idx] in neg_array:
               neg_array.remove(neg_false_array[idx])
           
    fobj1 = open(pfile, "w")
    for line in pos_array:
        fobj1.write(line+"\n")
    fobj1.close()  
    
    fobj2 = open(nfile, "w")
    for line in neg_array:
        fobj2.write(line+"\n")
    fobj2.close() 
    
    
    
    
    