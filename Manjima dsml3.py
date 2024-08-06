#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


import numpy as np
x=np.array([1,2,3,4])
print(x)


# In[4]:


pip install numpy


# In[1]:


import numpy as np
x=np.array([1,2,3,4])
print(x)


# In[2]:


print(type(x))


# In[3]:


print(x.shape)


# In[5]:


y=np.array([[1,2],[3,4]])
print(y)
print(y.shape)


# In[6]:


z=np.array([[1+0.j,2+5.j]])
print(z)
print(z.shape)


# In[7]:


a=np.zeros((2,3))
print(a)


# In[8]:


print(a.shape)


# In[9]:


b=np.ones((2,3),dtype=int)
print(b)


# In[10]:


d=np.eye(3)
print(d)


# In[12]:


e=np.arange(10)
print(e)


# In[13]:


e=np.arange(12,21)
print(e)


# In[14]:


e=np.arange(5,20,3)
print(e)


# In[44]:


f=np.linspace(1,10,4)
print(f)


# In[45]:


g=np.random.random((1,2))
print(g)


# In[47]:


h=np.random.random((3,4))
print(h.reshape(2,2,3))


# In[18]:


x=np.arange(12)
print(x)
print(x[4])


# In[19]:


print(x[-1])


# In[20]:


x.resize(3,4)
print(x)


# In[49]:


print(x[-1,-1])


# In[22]:


print(x[2][3])


# In[23]:


y=np.arange(1,26)
print(y)
print(y[:3])


# In[24]:


print(y[10:])


# In[25]:


print(y[10:15])


# In[26]:


print(y[-5:])


# In[27]:


print(y[3:-3])


# In[28]:


print(y[::3])


# In[29]:


print(y.reshape((5,5)))
print(y)


# In[30]:


y=y.reshape((5,5))
print(y)
print(y[:3,:3])


# In[31]:


print(y[2:-1,1:-1])


# In[32]:


print(:,:-1)


# In[33]:


print(y[:,:-1])


# In[34]:


print(y[:,-1])


# In[35]:


print(y[::,::2])


# In[36]:


print(y)


# In[37]:


print(y[1::2,1::2])


# In[38]:


a=np.arange(1,6)
b=np.arange(6,11)
print(a)
print(b)
print(a+b)
print(a-b)
print(b-a)
print(a**2)


# In[39]:


print(a>3)


# In[40]:


a=np.arange(0,4).reshape((2,2))
b=np.eye(2)
print(a*b)


# In[42]:


print(np.dot(a,b))

