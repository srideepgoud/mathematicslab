#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import linalg
m = 4
n = 4
A = np.random.standard_exponential(size=(m,n))
A=np.array([[1,2],[2,3]])
print(A)
lam, V = linalg.eig(A)
print(lam)
print(V)


# In[2]:


ainv=linalg.inv(A)
lam1,V1=linalg.eig(ainv)
print(lam1)
print(V1)
if (lam==lam1).all():
 print(" equal")
else:
 print("not Equal")


# In[3]:


print(A.dot(V))
print(lam * V )


# In[4]:


print(linalg.norm(A.dot(V) - lam*V))


# In[5]:


m=n=2
lambdaMatrix = np.zeros((m, n) , dtype=complex)
lambdaInvMatrix = np.zeros((m, n), dtype=complex)
for i in range(min(m, n)):
 lambdaMatrix[i, i] = lam[i]
 lambdaInvMatrix[i, i] = 1/lam[i]
Vinv = linalg.inv(V)
print( (V.dot(lambdaMatrix)).dot(Vinv) )
print(A)


# In[6]:


Vinv = linalg.inv(V)
Ainv = V.dot(lambdaInvMatrix).dot(Vinv)
print(Ainv)
Ainvd = linalg.inv(A)
print(Ainvd)
print(linalg.norm(Ainv - Ainvd))


# In[7]:


print("Det:\n{}".format(linalg.det(A)))
print(lam)
print(lam[0]*lam[1])
print("lambda Cumulative product:\n{}".format(lam.cumprod()) )


# In[8]:


print("Trace:\n{}".format(np.trace(A)))
print("lambda Cumulative sum:\n{}".format(lam.cumsum()) )


# In[9]:


D = np.array( [(1,1), (0,1)] )
print(D)
lamn, Vn = linalg.eig(D)
print(lamn)
print(Vn)
print(linalg.norm(D.dot(Vn) - lamn*Vn))


# In[10]:


arr=np.array([[1,1],[2,2]])
print(linalg.norm(arr))
import math
print(math.sqrt(10))


# In[ ]:




