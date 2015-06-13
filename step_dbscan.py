# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 08:39:58 2015

@author: kader
"""


from time import time
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.cluster import DBSCAN

filename = 'C:\\Users\\kader\\Documents\\GitHub\\python-projet\\a_array.txt'
f = open(filename, 'r')
a_array = np.loadtxt(f, dtype='<i4', delimiter=',')
a_edge=a_array[:,0].reshape(-1,1)

#%%
# plot the time step data
plt.axis([0,7000,0,24])
[plt.axvline(x=xi,ymin=0,ymax=float(yi)/24) for xi, yi in a_array]

plt.show()

#%%
# section for running clustering algorithm

t0 = time()         
db_scan = DBSCAN(eps=90, min_samples=1)
db_scan.fit(a_edge)
a_label = db_scan.labels_
print (time() - t0)

#%%
# plotting the results

plt.clf()
plt.axis([0,7000,0,24])
c = ['r', 'g', 'b', 'k', 'm']
result = sorted([(a_edge[a_label==x].min(),x,a_array[a_label==x])
 for x in np.unique(a_label)])
for i, x in enumerate(result):
    [plt.axvline(xi,0,float(yi)/24,color=c[i%5]) for xi, yi in x[2]]

plt.show()
print "transition steps found at ", [x[0] for x in result]
for x in result:
    print x[0], x[1], [y for yi, y in x[2]] 

#%%

#print a_array
f.close()