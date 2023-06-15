#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 
x=[0,1,2,3] 
y=[0,1,4,9] 
a,=plt.plot(x,y) 
print(a) 
plt.show() 


# In[2]:


x=np.linspace(-5,5,20) 
plt.plot(x,x**2,"ko") 
plt.plot(x,x**3,"r*") 
plt.show() 


# In[5]:


plt.figure(figsize=(8,6)) 
plt.plot(x,y) 
plt.xlabel("x") 
plt.ylabel("y") 
plt.savefig("newplot.pdf")


# In[9]:


omega = 2
z_line = np.linspace(0, 10, 100)
x_line = np.cos(omega*z_line)
y_line = np.sin(omega*z_line)
ax = plt.axes(projection='3d')
ax.plot3D(x_line, y_line, z_line, lw=4)



# In[10]:


from matplotlib import pyplot as plt 
import numpy as np 
# Creating dataset 
a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]) 
# Creating histogram 
fig, ax = plt.subplots(figsize =(10, 7)) 
ax.hist(a, bins = [0, 25, 50, 75, 100]) 
# Show plot 
plt.show() 


# In[11]:


plt.figure(figsize=(10,6)) 
x=np.linspace(-5,5,100) 
plt.plot(x,x**2,"ko", label="quadratic") 
plt.plot(x,x**3,"r*", label="cubic") 
plt.title("plot of various polynomials from (x[0]) to (x[-1])") 
plt.xlabel("X axis", fontsize=8) 
plt.ylabel("Y axis", fontsize=18) 
plt.legend(loc=1) 
plt.xlim(-6,6) 
plt.ylim(-10,10) 
plt.grid() 
plt.show() 


# In[ ]:




