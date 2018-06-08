# -*- coding: utf-8 -*-
"""
Created on Wed May 30 22:22:12 2018

@author: Mike
"""

import pandas as pd

data=pd.read_csv('sample.csv',delimiter=';')

#%%

m_total = sum(m)

sums_list =[]

for end in range(len(m)):
    for start in range(end):
        row = {'start'  :start,
               'end'    :end,
               'length' :end-start,
               'sum'    :sum(m[start:end])/m_total}
        sums_list.append(row)
        
sums = pd.DataFrame(sums_list)

#%%
r_crit = 0.8
good_rows=sums[sums['sum']>r_crit]

best=good_rows.sort_values(by='length')