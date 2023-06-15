#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import linalg

A= np.array([[1,2], [3,4]])
b= np.array([5,7])
x= linalg.inv(A).dot(b)
print(x)
print(A.dot(x))


# In[2]:


linalg.solve(A, b)



# In[3]:


m = 4; n=2
A = np.random.randint(100, size=(m,n))
b = np.random.randint(100, size=(m,1))
print("A=\n{}".format(A))
print("b=\n{}".format(b))


# In[4]:


Ainv = linalg.pinv(A)
x = Ainv.dot(b)
print(x)
print(A.dot(x) - b)


# In[ ]:




