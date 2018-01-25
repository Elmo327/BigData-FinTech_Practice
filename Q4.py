# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:47:32 2018

@author: User
"""
from scipy import linalg
import numpy as np
import pandas as pd



## Q4

# 예시 행렬과 백터 

vector1 = np.array([1,2,2])
vector2 = np.array([1,2]) 

matrix1 = np.array([[1,2,3],[4,7,4],[2,4,1]])
matrix2 = np.array([[1,3],[4,7]])


# 초기작업. 어떤 A와 b를 넣을지 정해줌( 이경우엔 3X3의 계산만 일단 넣었음)
A = matrix1
b = vector1

m , n = len(A), len(A[0])
P, L, U = linalg.lu(A)

#Forward elimination to solve L*y = Pb=c

y = np.zeros(m)
c = P.T.dot(b)

#print(L)
for j in range(m):
    y[j] = c[j] - np.inner( L[j,0:m-1] , y[0:m-1])
   
    
    
# Back substitution to solve U*x = y
    
x= np.zeros(n)


for j in range(n-1, -1, -1):
    x[j] = (y[j] - np.inner( U[j,0:n], x[0:n]))/U[j,j]
    inner = np.inner( U[j,j+1:n], x[j+1:n])
    
          
print(x)
