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

#%%
#plot the tags
x = all_array[:,0]
y = all_array[:,1]
plt.plot(x,y)

plt.show()