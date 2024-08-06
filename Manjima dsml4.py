#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
x=np.arange(1,10).reshape(3,3)
print(x)


# In[3]:


print(x.sum())


# In[4]:


print(x.sum(axis=1))


# In[5]:


x=np.arange(1,19).reshape(3,3,2)


# In[12]:


x=np.arange(1,19).reshape(3,3,2)
print(x)
print(x.sum(axis=1))


# In[8]:


print(x.max())


# In[10]:


x=np.arange(1,10).reshape(3,3)
print(x)
print(x.max())


# In[17]:


print(x.sum(axis=0))


# In[18]:


print(x)


# In[15]:


print(x.max(axis=0))


# In[19]:


print(x.sum(axis=1))


# In[20]:


print(x.sum(axis=0))


# In[21]:


x=np.arange(1,10).reshape(3,3)
print(x)
print(x.max())


# In[22]:


print(x.max(axis=0))


# In[23]:


print(x.transpose())


# In[ ]:




