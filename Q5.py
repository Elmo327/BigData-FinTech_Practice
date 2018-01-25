# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:39:04 2018

@author: User
"""

#Q5


import numpy as np
import matplotlib as mpl







#original condition to solve (a)
A1 = np.array([[0,0],[0,.27]])
A2 = np.array([[-.139,.263],[.246, .224]])
A3 = np.array([[.17, -.215],[.222, .176]])
A4 = np.array([[.781, 0.034], [-.032, .739]])
A_original = np.array([A1,A2,A3,A4])

d_original = [[.5,0], [.57, -.036], [.408, .0893], [.1075, .27] ]
p_original = [.02, .15, .13, .7]

#changed condition to solve (b)
A1 = np.array([[0,0],[0,.27]])
A2 = np.array([[-.139,.263],[.246, .224]])
A3 = np.array([[.17, -.215],[.222, .176]])
A4 = np.array([[.781, 0.034], [-.032, .739]])
A5 = np.array([[.234, .062], [.193, -.72]])
A_changed = np.array([A1,A2,A3,A4,A5])

d_changed = [[.5,0], [.57, -.036], [.408, .0893], [.1075, .27], [.34, .092] ]
p_changed = [.02, .15, .13, .3, .4]



def plotting(A, d, p):
    
    m= len(A)
    n= 10000
    z = np.zeros(2*n).reshape([n,2])
    z[0] = [0.5,0]
    
    for k in range(n):
        if k == n -1:
            break
        i = np.random.choice(np.arange(1,m+1), p= p )
        z[k+1] = A[i-1].dot(z[k]) + d[i-1]
    mpl.pyplot.show()    
    mpl.pyplot.scatter(z[:,0],z[:,1])
    


plotting(A_original, d_original, p_original)
plotting(A_changed,d_changed,p_changed)
