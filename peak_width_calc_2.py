# -*- coding: utf-8 -*-
"""
Created on Wed May 30 21:08:08 2018

@author: Mike
"""

import numpy as np

(v,m) = np.genfromtxt('sample.csv',skip_header=1,delimiter=';',unpack=True)

#%%
m_total = np.sum(m)
iters = int(len(m)*(len(m)-1)/2)

sums = np.zeros((iters,4))

#%%
i=0
for end in range(len(m)):
    for start in range(end):
        
        sums[i,0]=start
        sums[i,1]=end
        sums[i,2]=end-start
        sums[i,3]=np.sum(m[start:end])/m_total
        i+=1


#%%
r_crit = 0.8

s=sums[sums[:,3]>r_crit]