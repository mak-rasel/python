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
tag_edge = np.array([1, 2, 3, 4, 5, 7, 8, 17, 18,
 19, 20, 21, 22, 27, 28, 29, 30, 31, 43, 45, 46, 47, 48, 49])

f = open(file_step, 'r')
a_array = np.loadtxt(f, dtype='<i4', delimiter=',')
a_edge=a_array[:,0].reshape(-1,1)
sec = all_array[:,0]

time_step = [x[0] for x in result]
time_step.append(sec[-1])
time_step.insert(0,sec[0])
#%%
#plot the tags
index = 24
y = all_array[:,tag_edge[index-1]]
fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlim(sec[0],sec[-1])
ax.plot(sec,y)
ax.hold(True)
#plt.show()

# data selection
# divide the transition step span and monitor
x=[]
edge=a_edge[a_array[:,1]==index]
init_time = 1
end_time = 0
data=[]
for ii,e in enumerate(edge):
    if edge[ii] < sec[end_time]: continue
    for i,x in enumerate(time_step[init_time:],init_time):
        if x>e and time_step[i-1]<=e:
            #the time span has transition response
            print "transition step %i from %i to %i" %(i,e, x) 
            ax.axvline(e,0,1)
            ax.axvline(x,0,1)
            #get the data
            start_time= np.argwhere(sec==e)
            end_time = np.argwhere(sec==x)
            data.append([i,all_array[start_time:end_time,tag_edge[index-1]]])
            init_time=i+1
            if edge[ii]==edge[-1]:
                continue
            else:
                break
        else:
            #time span is in steady state monitoring
            print "steady state from %i to %i" %(time_step[i-1],x) 

            
#plt.draw()
