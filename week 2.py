#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
a = np.arange( 10, 30, 5 ) 
print(a) 
a = np.linspace( 0, 2, 9 ) 
print(a) 


# In[2]:


print("a=", a) 
b = np.sin(a) 
print("b=", b) 
c = a-b 
print("c=", c) 
d= b**2 
print("d=", d ) 


# In[3]:


ar = np.random.randint(5, size=(6)) 
print("ar=",ar) 
br = np.random.randint(5, size=(6)) 
print("br=",br) 
print("ar.br=",ar.dot(br)) 


# In[4]:


import scipy.linalg as sp 
print("norm of ar", sp.norm(ar)) 
print( "norm of ar", np.sqrt((ar**2).sum())) 
print("norm of br",sp.norm(br)) 
print( "norm of br", np.sqrt((br**2).sum())) 
costheta = ar.dot(br) / (sp.norm(ar) * sp.norm(br)) 
print("cosh =", costheta) 
print("angel is ", np.arccos(costheta)) 
coshcal=np.cosh(costheta) 
print(coshcal) 
print(np.arccosh(coshcal)) 


# In[5]:


a = np.array([6, 5, 7]) 
b = np.array([3, 8, 2]) 
costheta1 = a.dot(b) / (sp.norm(a) * sp.norm(b)) 
print("costheta", costheta1) 
rad = np.arccos(costheta1) 
print("rad",rad) 
print("degree", np.degrees(rad)) 
dotab = a.dot(b) 
abcostheta = (sp.norm(a) * sp.norm(b))*costheta1 
print(dotab, abcostheta) 
print("cross product", np.cross(a,b)) 


# In[7]:


ar = np.random.randint(5, size=(2,3)) 
br = np.random.randint(2, size= (3,2)) 
cr = np.random.randint(2, size= (2,3)) 
print("ar=", ar) 
print("br=", br) 
print("cr=", cr) 


# In[8]:


print("ar @ br=", ar@br) 
print("ar dot br=", ar.dot(br)) 


# In[9]:


anr = np.random.normal(0, 1.5, size=(2,3)) 
bnr = np.random.normal(0, 3, size= (3,2)) 
print(anr) 
print(bnr) 


# In[12]:


a = np.array([[1.0, 2.0], [-1.0, 3.0]]) 
from scipy.linalg import expm, sinm, cosm
print("expjTheta ={}".format(expm(1j*a)) ) 
v = cosm(a) + 1j*sinm(a) 
print("cosTheta + jsinTheta={}".format(v)) 


# In[ ]:




