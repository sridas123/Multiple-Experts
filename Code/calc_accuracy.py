# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:29:28 2017

@author: dishu
"""
from sklearn.metrics import accuracy_score,precision_score,recall_score
f = open('results_advisedBy.txt', 'r')
a_list=[]
for i in f.readlines():
    s=i.split(" ")
    a_list.append(s)
y_pred=[]
y_true=[]
#print a_list
for i in range(len(a_list)):
    if '!' in a_list[i][0]:
        y_true.append(0)
        a_list[i][1]=a_list[i][1][:-2]
        a_list[i][1]=1.0-float(a_list[i][1])
        #print a_list[i][1]
    else:
        y_true.append(1)
    if float(a_list[i][1])>=0.5:
        y_pred.append(1)
    else:
        y_pred.append(0)

accuracy=accuracy_score(y_true,y_pred)
precision=precision_score(y_true, y_pred)
recall=recall_score(y_true, y_pred)
f1_score=2*(precision*recall)/(precision+recall)
f3_score=10*(precision*recall)/((9*precision)+recall)
f5_score=26*(precision*recall)/((25*precision)+recall)
print("accuracy is",accuracy)
print("f3 score is",f3_score)
print("f5 score is",f5_score)