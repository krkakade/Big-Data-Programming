#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:55:15 2019

@author: komal
"""

# Exercise 1 : How to replace items that satisfy a condition with another value in numpy array?
# Replace all odd numbers in array with -1

import numpy as np
#1st way
a=np.arange(10)       #d=np.array([0,1,2,3,4,5,6,7,8,9]) the same thing
output=a%2
j=0
print(type(a)) #initial

for i in output:
    if output[i]==1:
        a[j]=-1
    j=j+1    

print(type(a),a)  #final

#2nd way
b=np.arange(10)
print(b)
b= np.array([i if i % 2!=1 else -1 for i in b])
print(type(b), b)

#3rd way
c=np.arange(10)
print(c)
print(type(np.where((c%2)==1, -1, c)),np.where((c%2)==1, -1, c))


#Exercise 2 : How to reshape an array?
# Convert a 1D array with 2D array with 2 rows.

import numpy as np
#1st way
a=np.arange(10)         
output = a.reshape(2,5)

print(output)

#2nd way
b=np.arange(10)
new=np.reshape(b,(-1,int(len(b)/2)))  #reshape create a new reshaped instance of the array
print(new)

#3rd way
c=np.arange(10)
new1=np.resize(c, 10).reshape(2,5)  # resize will affect the original array 
print(new1)


# Exercise 3 : How to generate custom sequences in numpy without hardcoding?

# create a pattern with given input array

import numpy as np
a=np.array([1,2,3])    #1st way
a1=a.repeat(3)
a2=np.tile(a,3)
a3=np.append(a1,a2)
print(a3)


# same thing in one line
a4=np.append(a.repeat(3),np.tile(a,3))  #2nd way
print(a4)

#another way using hstack
result = np.hstack([
    np.repeat(a, 3),
    np.tile(a,3)
])
print(result)


# Exercise 4 : How to get common items between two python numpy arrays?

# get the common items between a and b

import numpy as np

a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])


c=np.intersect1d(a,b)  #1st way
#print(c)

#for loop method :  2nd way

emptylist=[]  
for i in b:
    for j in a:
        if i==j:
            emptylist.append(i)  
            
#result=np.array(list(set(emptylist)))    # either use set to keep uniue values in the list 
#print(result)            
            
result=np.array(emptylist)  # use numpy.uniue to return only unique values in array            
print(np.unique(result))


#Exercise 5 : How to get the positions where elements of two arrays match??
#Get the positions where elements of a and b match

import numpy as np

a=np.array([1,2,3,2,3,4,3,4,5,6])
b=np.array([7,2,10,2,7,4,9,4,9,8])

print(np.nonzero(np.in1d(b,a)))  # 1st way

  

d=np.intersect1d(b,a)
#print(d)
wanted = set(d)
#print(type(wanted))
indices =[idx for (idx, value) in enumerate(a) if value in wanted]
print(indices)          # 2nd way


#3rd way
c = np.in1d(b,a)         ## so when true return the index  #FYI tis gives true false
result = np.where(c)
print(result)


e = np.in1d(b,a)         ## similar
res = np.argwhere(e)
print(res)

#Exercise 6 : How to create a 2D array containing random floats between 5 and 10?

# Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.

import numpy as np

a= 5* np.random.random_sample((5,3)) + 5  #1st way
print(a)

b=5*np.random.rand(5,3)+5   #2nd way
print(b)

c=5 * np.random.ranf((5, 3)) + 5    #3rd way
print(c)

#Exercise 7 : How to limit the number of items printed in output of numpy array to 6
#Limit the number of items printed in python numpy array a to a maximum of 6 elements

import numpy as np
c= np.arange(15)
#np.set_printoptions(threshold=6)
print(c)


#Exercise 8 : How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?
# limit the number of items printed in python numpy array a to a maximum of 6 elements

import numpy as np

np.random.seed(100)
a=np.random.random([3,3])/1e3
np.set_printoptions(suppress=True)
print(a)


#Exercise 9: How to swap two columns in a 2d numpy array?
#Swap columns 1 and 2 in the array arr
import numpy as np
#1st way
a = np.arange(9).reshape(3,3)
print(a)
a[:,[0,1]] = a[:,[1,0]]
print(a)

#2nd way
x = np.arange(9).reshape(3,3)
print (x)
y = np.arange(9).reshape(3,3)
y[:,0], y[:,1], y[:,2] = x[:,1], x[:,0], x[:,2]
print (y)

#3rd way
b=np.arange(9).reshape(3,3)
z=b[:, [1,0,2]]
print(b)




#Exercise 10: How to swap two rows in a 2d numpy array?

# Swap rows 1 and 2 in the array arr
import numpy as np

a = np.arange(9).reshape(3,3)
b=a[[1,0,2], :]
print(b)