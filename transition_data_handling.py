# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 15:33:18 2015

@author: kader
"""

import numpy as np
import matplotlib.pyplot as plt 

file_data = 'C:\\Users\\kader\\Documents\\GitHub\\python-projet\\All_array.txt'
file_step = 'C:\\Users\\kader\\Documents\\GitHub\\python-projet\\a_array.txt'
f_data = open(file_data, 'r')
all_array = np.loadtxt(f_data, delimiter=',')

f = open(file_step, 'r')
a_array = np.loadtxt(f, dtype='<i4', delimiter=',')
a_edge=a_array[:,0].reshape(-1,1)
time = all_array[:,0]

result = result
#%%
#plot the tags
index = 2
y = all_array[:,index]
plt.plot(time,y)

plt.show()