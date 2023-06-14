#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(5*3)
l = 5; b = 6
print("length={}, width={}, Area={}".format(l, b, l*b) )


# In[2]:


import math
radius = 5.0
Area = math.pi *radius ** 2
print("Area of a circle:{}".format(Area) )


# In[3]:


print(math.sin(math.pi / 2))
print(math.log(1024, 2))


# In[5]:


def factorial(n):
 if(n==0): return 1
 
 if(n==1): return 1
 
 res = 1
 while(n>=1):
   res = res * n
   n = n-1
 return res
def recursive_factorial(n):
 if(n==0): return 1
 
 if(n==1): return 1
 
 return n*recursive_factorial(n-1)
print(factorial(4))
print(recursive_factorial(4)) 


# In[6]:


import numpy as np
a = np.array( [1,0,0] )
print(a)
print(type(a), a.dtype)


# In[7]:


a = np.zeros( (3,3) )
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a[2][2])


# In[8]:


a = np.arange( 10, 30, 5 )
print(a)
a = np.linspace( 0, 2, 9 )
print(a)


# In[ ]:




