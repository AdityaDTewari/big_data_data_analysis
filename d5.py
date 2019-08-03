# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:47:01 2019

@author: Aditya
"""
# using numpy and arrays

import numpy as np
mylist = [1, 2, 3]
x = np.array(mylist)
x

y = np.array([4, 5, 6])
y

m = np.array([[7, 8, 9], [10, 11, 12]])
m

m.shape

n = np.arange(0, 30, 2)
n

n = n.reshape(3, 5)
n

o = np.linspace(0, 4, 9)
o

o.resize(3, 3)
o

np.ones((3, 2))
np.zeros((2,3))
np.eye(3)
np.diag(y)

np.array([1, 2, 3]*3)
np.repeat([1, 2, 3], 3)

p=np.ones([2, 3], int)
p

np.vstack([p, 2*p])
np.hstack([p, 2*p])

#operations

x+y
x*y
x**2
x.dot(y)

z = np.array([y, y**2])
z

z.T

z.dtype
z = z.astype('f')
z.dtype

a = np.array([-4, -2, 1, 3, 5])
a.sum()
a.max()
a.min()
a.mean()
a.std()
a.argmax()
a.argmin()

#indexing and slicing

s = np.arange(13)**2
s
s[0], s[4], s[0:3]
s[-4:]
s[-5::-2]

r = np.arange(36)
r.resize((6,6))
r
r[2,2]
r[3,3:6]
r[:2, :-1]
r[-1, ::2]

r[r > 30]
r[r > 30] = 30
r


r2 = r[:3,:3]
r2
r2[:] = 0
r2
r

r_copy = r.copy()
r_copy

#iterate over arrays

test = np.random.randint(0, 10, (4,3))
test
for row in test:
    print(row)

for i in range(len(test)):
    print(test[i])

for i, row in enumerate(test):
    print('row', i, 'is', row)

test2 = test**2
test2

for i, j in zip(test, test2):
    print(i, '+', j, '=', i+j)