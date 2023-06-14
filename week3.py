#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.linalg as spylinalg
a = np.random.normal(5, 1, size=(4,4))
#a=np.array([1,2])
ainv = spylinalg.inv(a)
print(ainv)


# In[2]:


print(a.dot(ainv))


# In[3]:


np.eye(4)


# In[4]:


print(spylinalg.det(a))


# In[5]:


spylinalg.norm(a)
help(spylinalg.norm)


# In[ ]:




