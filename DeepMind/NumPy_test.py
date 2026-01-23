import numpy as np

a1 = np.array([1,2,3]) # 1D array
print(a1)
a2 = np.array([[1,2],[3,4]]) # 2D array
print(a2)
a3 = np.array([
    [  # Layer 1
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ],
    [  # Layer 2
        [13,14,15,16],
        [17,18,19,20],
        [21,22,23,24]
    ]
]) # 3D array is a list of 2D arrays
print(a3)
print(a3.shape)#output(2,3,4)=(depth, rows, columns)
print(a3[1][2][3])#output 24

a0 = np.zeros(5) # 1D array
a0 = np.zeros((3,3)) # creates a 2D array and filled with zeros
a0 = np.zeros((2,3,4))

a1 = np.ones((4,4), int) # 2D array filled with ones

ar = np.arange(0,10,2) # 1D np.arange(start, stop, step)
print(ar) # output(0,2,4,6,8)

ar = np.arange(5) # [0 1 2 3 4]
ar = np.arange(1, 6) # [0 1 2 3 4 5]
# ar = np.arange(0, 1, 0.1) # error
ar = np.linspace(0, 1, 10) # (start, stop, num) num = numbers of points to generate
print(ar)

ar = np.zeros((3,3)) + np.ones((3,3)) # Pure C-speed 
print(ar)

a1 = np.array([10,20,30,40,50])
print(a1[2])
print(a1[-1])

# NumPy Array Slicing
a2 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
print(a2[1,0])
print(a2[0:2:2]) # row slice
print(a2[:, 1]) # all rows, column 1

# Advanced Indexing
a = np.array([10,20,30,40,50,60])
ind = np.array([1,3,5])

print(a[ind])

cond = a > 30
print(a[cond])

#NumPy Basic Arithmetic Operations
x = np.array([1,2,3])
y = np.array([4,5,6])

print(np.c_[x,y])
print(x + y)
print(x - y)
print(x / y)
print(x * y)

#Unary Operation
a = np.array([-3, -1, 0, 1, 3])
print(np.absolute(a))#[3 1 0 1 3]

#Binary Operators
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

res = np.add(a1,a2)
print(res)

#NumPy Math
a = np.array([0, np.pi/2, np.pi])
print(np.sin(a))

b = np.array([0,1,2,3])
print(np.exp(b))
print(np.sqrt(b))

#NumPy Sorting Arrays
dtype = [('name', 'S10'), ('year', int), ('cgpa', float)]
vals = [('Hrithik', 2009, 8.5),
        ('Ajay', 2008, 8.6),
        ('Pankaj', 2005, 4.5),
        ('Akaja', 2007, 9.0)]

a = np.array(vals, dtype=dtype)
print(np.sort(a, order='name'))
print(np.sort(a, order=['year', 'cgpa']))


import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)
y = y.reshape(-1,1) # 1 column arrange the rows
m = X.shape[0] # number of training examples

X_b = np.c_[np.ones((m, 1)), X]

theta = np.array([[2.0], [3.0]])

plt.figure(figsize=(10,5))
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, X_b.dot(theta), color="green", label="Inital line (No GD)")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.title("Linear Regression Without Descent")
plt.legend()
plt.show()