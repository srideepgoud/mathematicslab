#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import linalg
m = 4
n = 4
A = np.random.randint(100, size=(m,n))
print(A)
lam, V = linalg.eig(A)
print(lam)
print(V)


# In[9]:


A=np.array([[2,2],[1,1]])

U, s, V = linalg.svd(A)
print(U)
print(s)
print(V)
print("multi U",U.shape, U.dot(U))
print("s=",s.shape,s)
print("multi V",V.shape, V.dot(V))
print("A=", U.dot(s).dot(V))


# In[10]:


sigma = np.zeros((m, n))
sigmainv = np.zeros((m, n))
for i in range(min(m, n)):
    sigma[i, i] = s[i]
    sigmainv[i,i] = 1/s[i]

A1 = np.dot(U, np.dot(sigma, V))
print(A)
print(A1)
print(sigma)
print(sigmainv)


# In[6]:


print("U(U.transpose)=\n{}".format(U.dot(U.transpose())))
print("V(V.transpose)=\n{}".format(V.dot(V.transpose())))


# In[7]:


Uinv_ortho = U.transpose()
Uinv = linalg.pinv(U)
print(Uinv_ortho)
print(Uinv)


# In[11]:


Ainv_svd = ((V.transpose()).dot(sigmainv)).dot(U.transpose())
Ainv = linalg.pinv(A)
print(Ainv)
print(Ainv_svd)
print(A.dot(Ainv))
print(A.dot(Ainv_svd))


# In[12]:


import numpy as np
from matplotlib import pyplot as plt
mu=0
sigma=1
a=np.random.normal(mu, sigma, 10)
#print(a)
fig, ax = plt.subplots(figsize =(10, 7))
bins=np.linspace(-5,5,30)
#print(bins)
ax.hist(a, bins )
# Show plot
plt.show()


# In[14]:


import numpy as np
from scipy import linalg
m = 4
n = 4
A = np.random.standard_exponential(size=(m,n))
A=np.array([[5,-10,-5],[2,14,2],[-4,-8,6]])
print(A)
lam, V = linalg.eig(A)
print("lam=",lam)
print("V=",V)
print(V.shape)
print("AxV=",A.dot(V))
print("lam.V=",lam*V)


# In[15]:


print(A.dot(V))
print(lam * V )


# In[16]:


import numpy as np
from scipy import linalg
A=np.array([[3,1,1],[-1,3, 1]])
U, s, V = linalg.svd(A)
print(U)
print(s)
print(V)
print("multi U",U.shape, U.dot(U))
print("s=",s.shape,s)
print("multi V",V.shape, V.dot(V))
#print("A=", U.dot(s).dot(V))


# In[ ]:




