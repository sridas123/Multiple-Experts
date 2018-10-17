# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:00:29 2018

@author: sxd170431
"""
from sklearn.model_selection import train_test_split
def convert_format(data,label,trainpath, testpath, train_fact, train_pos, train_neg, test_fact, test_pos, test_neg):
    print label
    X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.10)
    print "The shape is", X_train.shape, X_test.shape,y_train.shape,y_test.shape
   
    train_array=[];train_pos_label=[];train_neg_label=[]
    test_array=[];test_pos_label=[];test_neg_label=[] 
    """Convert the data into rdn predicates"""
    for i in range(0,X_train.shape[0]):
        data=X_train[i]
        pid="Patientid("+str(data[0])+")."
        bp= "BP("+str(data[0])+","+str(data[1])+")."
        chol= "chol("+str(data[0])+","+str(data[2])+")."
        #age= "age("+str(data[0])+","+str(data[3])+")."
        #stress= "stress("+str(data[0])+","+str(data[4])+")."
        train_array.extend([pid,bp,chol])
        
        if y_train[i]==1:
           train_pos_label.append("HA("+str(data[0])+").") 
        else:   
           train_neg_label.append("HA("+str(data[0])+").")  
           
    for i in range(0,X_test.shape[0]):
        data=X_test[i]
        pid="Patientid("+str(data[0])+")."
        bp= "BP("+str(data[0])+","+str(data[1])+")."
        chol= "chol("+str(data[0])+","+str(data[2])+")."
        #age= "age("+str(data[0])+","+str(data[3])+")."
        #stress= "stress("+str(data[0])+","+str(data[4])+")."
        test_array.extend([pid,bp,chol])
        
        if y_test[i]==1:
           test_pos_label.append("HA("+str(data[0])+").") 
        else:   
           test_neg_label.append("HA("+str(data[0])+").")     
           
    print train_array[0:10]
    print test_array[0:10]     
    
    """Writing the examples into necessary files"""
    fobj1 = open(trainpath+train_fact, "w") 
    fobj2 = open(trainpath+train_pos, "w") 
    fobj3 = open(trainpath+train_neg, "w") 
   
    fobj4 = open(testpath+test_fact, "w") 
    fobj5 = open(testpath+test_pos, "w") 
    fobj6 = open(testpath+test_neg, "w") 
   
    for line in train_array:
       fobj1.write(line+"\n")
    for line in train_pos_label:
       fobj2.write(line+"\n")
    for line in train_neg_label:
       fobj3.write(line+"\n")
    for line in test_array:
       fobj4.write(line+"\n")
    for line in test_pos_label:
       fobj5.write(line+"\n")
    for line in test_neg_label:
       fobj6.write(line+"\n")
       
       
    