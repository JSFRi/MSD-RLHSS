#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, sys, getopt, pdb

import numpy as np
import pandas as pd
import random

#for each tier
class env:
    
    def __init__(self,tier):
        ## tier info
        self.initial_tier=tier
        self.tier=tier
        self.actions=list(self.tier['No.'])
        ## wating time
        self.s3=0
        #self.return=0
    
    def reset(self):
        self.tier=self.initial_tier
        #self.return=0
    
    def action_space(self):
        return self.actions
            
    
    def step(self,requestsDF,beta=0.05):
        
        ## calculate reward
        requested=requestsDF.loc[requestsDF['request']==1].loc[requestsDF['No.'].isin(self.tier['No.'])]
        xn=len(requested)
        response_times=list(requested['response'])
        if xn==0:
            rewards=0
        else:
            time_diff=np.arange(0,1,1/xn)
            rewards=0
            for i in range(xn):
                rewards+=response_times[i]*np.exp(-beta*time_diff[i])
            rewards=rewards/xn
        
        ## calculate states s1,s2,s3
        if len(self.tier)==0:
            s1=0
            s2=0  ## set it to be large enough
            s3=0
        else:
            ### s1
            s1=self.tier['temp'].mean()
            ###s2
            s2=sum([self.tier['temp'][i]*self.tier['ints'][i] for i in self.tier.index])/len(self.tier)
            ### s3
            s3=sum(response_times)
        
        return s1,s2,s3,rewards
    
    def update_or_not(self, file, T_or_F):
        fileNo=int(file['No.'])
        if T_or_F==True:
            if fileNo in list(self.tier['No.']):
                self.tier=self.tier.drop(self.tier.loc[self.tier['No.']==fileNo].index).reset_index(drop=True)
            else:
                self.tier=pd.concat([self.tier,file],ignore_index=True)
        else:
            pass
        
    def add_file(self,file):
        # if already in, then pass
        '''if int(file['No.']) in self.tier['No.']:
            pass
        else:'''
        self.tier=pd.concat([self.tier,file],ignore_index=True)
        
    def remove_file(self,file):
        self.tier=self.tier.drop(self.tier.loc[self.tier['No.']==int(file['No.'])].index).reset_index(drop=True)


## Naturally decreasement of temp
def temp_decrease(tier1,tier2,tier3,Request,timestep):
    
    req_No=list(Request.loc[Request['request']==1,'No.'])
    
    for i in list(tier1['No.']):
        if i in req_No:
            tier1.loc[tier1['No.']==i,'time_untouched']=0
        else:
            ##increase untouched time by 1
            tier1.loc[tier1['No.']==i,'time_untouched']+=1
            ## decrease temp by 0.05 after $timestep times untorched
            if int(tier1.loc[tier1['No.']==i,'time_untouched'])%timestep==0:
                tier1.loc[tier1['No.']==i,'temp']-=0.05
            if float(tier1.loc[tier1['No.']==i,'temp'])<0.1:
                tier1.loc[tier1['No.']==i,'temp']=0.1
                
    for i in list(tier2['No.']):
        if i in req_No:
            tier2.loc[tier2['No.']==i,'time_untouched']=0
        else:
            ##increase untouched time by 1
            tier2.loc[tier2['No.']==i,'time_untouched']+=1
            ## decrease temp by 0.05 after $timestep times untorched
            if int(tier2.loc[tier2['No.']==i,'time_untouched'])%timestep==0:
                tier2.loc[tier2['No.']==i,'temp']-=0.05
            if float(tier2.loc[tier2['No.']==i,'temp'])<0.1:
                tier2.loc[tier2['No.']==i,'temp']=0.1

    for i in list(tier3['No.']):
        if i in req_No:
            tier3.loc[tier3['No.']==i,'time_untouched']=0
        else:
            ##increase untouched time by 1
            tier3.loc[tier3['No.']==i,'time_untouched']+=1
            ## decrease temp by 0.05 after $timestep times untorched
            if int(tier3.loc[tier3['No.']==i,'time_untouched'])%timestep==0:
                tier3.loc[tier3['No.']==i,'temp']-=0.05
            if float(tier3.loc[tier3['No.']==i,'temp'])<0.1:
                tier3.loc[tier3['No.']==i,'temp']=0.1


def hot_cold(tier,file):
    tier.loc[tier['No.']==int(file['No.']),'req_time']+=1
    file=tier.loc[tier['No.']==int(file['No.'])]
    ## weight/request_time as probability ratio
    ratio=1-1/(1+np.exp(5000*7.33/10000)*np.exp(-(7.33/10000)*float(file['size']/file['req_time'])))
    
    ##if file is cold, change it to hot according to the weight/req_time ratio
    if float(file['temp'])<0.5:
        if random.random()<0.5*ratio:
            temp=1-0.5/np.exp(0.02*file['req_time'].item())
            file['temp']=temp
            tier.loc[tier['No.']==int(file['No.'])]=file
        else:
            pass
     ##if the file is hot, increase temperatue by requests time
    else:
        temp=1-0.5/np.exp(0.02*file['req_time'].item())
        file['temp']=temp
        tier.loc[tier['No.']==int(file['No.'])]=file
