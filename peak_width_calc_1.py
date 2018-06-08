# -*- coding: utf-8 -*-
"""
Created on Wed May 30 19:16:10 2018

@author: Mike
"""

import csv



def get_v_m(filename,skip=True):
    with open(filename, 'r') as f:
        reader = csv.reader(f,delimiter=';')
        if skip:
            next(reader, None)
              
        v = []
        m = []
        for row in reader:
            vt,mt = row
            v.append(float(vt))
            m.append(float(mt))
        return (v,m)
#%%
(v,m) = get_v_m('sample.csv')

#%%
r_level = 0.8 # 80% recovery from total_m

peak = m.index(max(m))

cut = [peak,peak]

peak_to_right = len(m)-peak

max_range = max(peak,peak_to_right)

for step in range(max_range):
    #step left
    left = peak-step
    if left<0:
        left = 0
    print (left)
    right = peak + step
    if right>len(m):
        right = len(m)
    print (right)
























#%%