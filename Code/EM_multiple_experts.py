from __future__ import division  # floating point division
import numpy as np
import utilities as utils
import math
#from numpy import linalg as LA
#from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
    
class EM_Logit():
    """ Logistic regression; need to complete the inherited learn and predict functions """

    def __init__( self,params=None):
        self.weights = None
        self.expwghts=None
        self.wghtgrad=None
        self.expgrad=None
        self.prob=None
        self.regwt=params['regwt']
        self.lrate=0.01
        self.threshold=0.1
        self.model = LogisticRegression()
                
    def learn(self, Xtrain, ytrain,yexp,exp_count):
        print "The shape is", Xtrain.shape,ytrain.shape,yexp.shape
        print "The main learning module begins"
        self.weights=np.zeros(Xtrain.shape[1])
        self.wghtgrad=np.zeros(Xtrain.shape[1])
        #print self.weights.T.shape
        self.expwghts=np.zeros(exp_count)
        self.expwghts[:]=(1/exp_count)
        self.expgrad=np.zeros(exp_count)
        print "The self.expgrad is", self.expgrad
        #print self.expwghts
        flag=False
        while(1):
            """Calculate the gradients with respect to the weights of the model"""
            for i in range(0,Xtrain.shape[0]):
                data=Xtrain[i]
                """Calculate the (Y-P) components of the gradient"""
                data_prob=np.dot(self.weights.T,data)
                print "data_prob is", data_prob
                self.prob=utils.sigmoid_val(data_prob)
                print "self.prob is", self.prob
                for j in range(0,Xtrain.shape[1]):
                    print "data[j]", data[j]
                    print "ytrain[i]-self.prob",ytrain[i]-self.prob
                    data_grad=data[j]*(ytrain[i]-self.prob)
                    """This is the advice gradient for every point in the training data"""
                    adv_grad=0
                    for k in range(0,exp_count):
                        if yexp[i][k]!=1000:
                           flag=True 
                           temp_grad=data[j]*(yexp[i][k]-self.prob)
                           print "temp_grad is", temp_grad
                        else:
                           temp_grad=0 
                           #print "***",np.exp(self.expwghts[0][k])*temp_grad
                        adv_grad=adv_grad + (np.exp(self.expwghts[k])*temp_grad) 
                        print "adv_grad is", adv_grad
                        #adv_grad=adv_grad + ((self.expwghts[k])*temp_grad)
                    print "Weight before update", self.weights   
                    self.wghtgrad[j]= self.wghtgrad[j] + (data_grad) + (adv_grad) 
                    print "Wghtgrad is", self.wghtgrad
                
                """These are for testing purpose"""
                if flag==True:
                   break 
            """Update the wghts by adding the gradients"""
            prev_weights=self.weights
            
            """Update the weights with the weight gradients"""
            #print "The weight gradients are", self.wghtgrad
            self.weights=np.add(self.weights,(self.lrate*self.wghtgrad))   
            print "The weight after update is", self.weights
            print "The value of i is", i
            break
            #print "The weights are",self.weights
            
            distance= np.linalg.norm(np.subtract(prev_weights,self.weights))
            #print("The distance between the weights is",distance)
            
            if distance <= self.threshold:
               break
            
            """Calculate the gradients with respect to each expert"""
            
            for i in range(0,Xtrain.shape[0]):
                data=Xtrain[i]
                for j in range(0,exp_count):
                    if yexp[i][j]!=1000:
                       data_prob=np.dot(self.weights.T,data) 
                       self.prob=utils.sigmoid_val(data_prob)
                       temp_grad= np.exp(self.expwghts[j])*((yexp[i][j]-1)*data_prob + math.log(self.prob))
                       #temp_grad= ((yexp[i][j]-1)*data_prob + math.log(self.prob))
                    else:
                       temp_grad=0 
                    self.expgrad[j]=self.expgrad[j] +temp_grad  
            #print "The expert weight gradients are", self.expgrad        
            self.expwghts=np.add(self.expwghts,(self.lrate*self.expgrad)) 
            #print self.expwghts
            
            """Printing the current value of the Objective function to see if EM is proceeding in the right direction"""
            obj=0
            for i in range(0,Xtrain.shape[0]):
                data=Xtrain[i]
                data_prob=np.dot(self.weights.T,data) 
                self.prob=utils.sigmoid_val(data_prob)
                data_obj=((ytrain[i]-1)*data_prob) + math.log(self.prob)
                adv_obj=0
                for j in range(0,exp_count):
                    if yexp[i][j]!=1000:
                       temp_adv_obj= np.exp(self.expwghts[j])*((yexp[i][j]-1)*data_prob + math.log(self.prob))
                       #temp_adv_obj= (self.expwghts[j])*((yexp[i][j]-1)*data_prob + math.log(self.prob))
                    else:
                       temp_adv_obj=0 
                       adv_obj=adv_obj+ temp_adv_obj
                       
                obj= obj+data_obj + adv_obj
                
                
                
            print "The value of the objective function is", obj           
                    
    def learn_noisy_wthout_advice(self, Xtrain, ytrain):
        self.model.fit(Xtrain,ytrain)
        coef = self.model.coef_[0]
        print "The weights on noisy data is", coef 
           
    def predict(self, Xtest):
        temp=self.weights[self.weights ==0]
        print("The shape of temp is",temp.shape)
        yvec = np.dot(Xtest, self.weights)
        ytest=utils.sigmoid(yvec)
        ytest[ytest >= 0.5] = 1     
        ytest[ytest < 0.5] = 0    
        return ytest




        
            
    
