# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:23:13 2018

@author: sxd170431
"""
path="C:\\Users\\sxd170431\\eclipse-workspace\\Boostr-multiple_experts\\UWCSE_ILP2016_advice\\Fold1\\test\\"
filename="test_facts.txt"
factfile=[]
predicatename="courseLevel"
if __name__ == '__main__':
   fobj = open(path+filename, "r") 
   for line in fobj:
       line=line.strip()
       if predicatename in line:
          res_level=line.split(",")
          res_course=res_level[0].split("(")
          course=res_course[1]
          if "level_100" not in res_level[1]:
             out="notCourselevel_100("+course+")."
             factfile.append(out)
       else:
        factfile.append(line)
   print factfile     
   fobj1 = open("test_facts.txt", "w")
   for line in factfile:
        fobj1.write(line+"\n")
   fobj1.close()      
    

