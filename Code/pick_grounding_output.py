# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 19:53:52 2018

@author: Srijita
"""
path="D:\\Grad Studies\\SRL\\Crowd_of_experts\\Code\\GroundingSAT-master\\data\\"
filename=path+'output_neg.txt'
ofilename1="neg_true_rule_groundings"
ofilename2="neg_false_rule_groundings"
print filename
satground=[]
unsatground=[]
if __name__ == '__main__':
    
    fobj = open(filename, "r")
    groundedpd=[]
    firstlinebrack=False
    seclineafterbrack=False
    groundedpd=" "
    for line in fobj:
        
        if "Ex" in line:
           pieces=line.split(" ") 
           groundedpd=pieces[1]
           #print pieces[1]
        if "[" in line:
           firstlinebrack=True
           continue 
        if firstlinebrack==True:
           firstlinebrack=False
           seclineafterbrack=True
           continue
        if seclineafterbrack==True:
           seclineafterbrack=False
           if(line.strip()):
              print "No blank" 
              print groundedpd
              satground.append(groundedpd)
           else:
              print "blank"
              print groundedpd
              unsatground.append(groundedpd)

    fobj1 = open(ofilename1, "w")
    for line in satground:
        fobj1.write(line+"\n")
    fobj1.close()  
    
    fobj2 = open(ofilename2, "w")
    for line in unsatground:
        fobj2.write(line+"\n")
    fobj2.close() 
    
    
    
    
    