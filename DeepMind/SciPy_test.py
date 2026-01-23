import numpy as np
import scipy as sp
from scipy import stats
import random


data = np.array([], dtype=int)
for _ in range(1000):
    # each time creates a new array
    data = np.append(data, np.random.randint(0,1e9)) 
    
print(sorted(data, reverse=True))
mean_val = np.mean(data)
print(mean_val)

std_dev = np.std(data)
print(std_dev)

#t_stat, p_value = stats.ttest_ind(group1, group2)
t_stat, p_value = stats.ttest_1samp(data, popmean=5)
print("t_stat>...", t_stat)
print("p_value>...", p_value)

####################
print('\n\n\n\n\n\n')
####################

from scipy import linalg
# more efficient way
A = np.random.randint(0, 1e9, size=(4,4))
# print(A)
print(A, end="\n")
# convert to 3D array 
A = A.reshape(1,4,4)
print(A, end="\n")
# !In statistics, determinants measure the overall 
# spread, validity, and probability scaling of multivariate data.
print(linalg.det(A)) 
# A matrix is invertible if and only if
# it is square and det(A) ≠ 0

P, L, U = linalg.lu(A)
print(P)
print(L)
print(U)
print("L X U:", np.dot(L,U))

# Eigen values and Eigen vectors of this matrix


# Sparse Linear Algebra
from scipy import sparse
A = sparse.lil_matrix((1000,1000)) #create an empty sparse matrix
print(A) #1000X1000 matrix
A[0, :100] = np.random.rand(100) #0. row 0-99 columns are filled out by characters between [0, 1)
A[1, 100:200] = A[0, :100] #coppies the same 100 values
A.setdiag(np.random.rand(1000)) #adds non-zero diagonal elements
print(A) #total added elements ~1200 Matrix still 98.88% zeros

# Linear Algebra for Sparse Matrices
from scipy.sparse import linalg
A.tocsr()
A = A.tocsr()
b = np.random.rand(1000)
ans = linalg.spsolve(A, b)
print(ans)
# This code efficiently solves a large sparse linear system 
# system 𝐴𝑥=𝑏 using CSR format and sparse numerical methods.

from scipy import integrate
f = lambda y, x: x * y**2
# integrate.dblquad(func, x_min, x_max, y_min(x), y_max(x))
i = integrate.dblquad(f, 0, 2, lambda x: 0, lambda x: 1)
# output first value-> numerical result
# second value-> estimated numerical error
# dblquad computes a double integral by integrating over 
# y first, then x, and the function must be written as f(y, x).