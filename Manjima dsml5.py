#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt


# In[3]:


pip install matplotlib


# In[6]:


x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[i**2 for i in x]
plt.plot(x,y)
plt.show()


# In[9]:


from matplotlib import pyplot as plt
x=[6,4,3,3,5,9]
plt.plot(x)
plt.show()


# In[12]:


import numpy as np
import math
x=np.arange(1,2,0.1).tolist()
y=[i**2 + 5 for i in x]
print(x)
print(y)
plt.plot(x,y)
plt.show()



# In[13]:


import numpy as np
x=np.arange(0,10,0.1)
y=np.sin(x)
print(x)
print(y)
plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sin')
plt.title('sin wave')
plt.show()


# In[14]:


import numpy as np
x=np.arange(0,10,0.1)
y=np.sin(x)
print(x)
print(y)
plt.plot(x,y)
plt.scatter(x,y)
plt.xlabel('angle')
plt.ylabel('sin')
plt.title('sin wave')
plt.show()


# In[23]:


plt.plot(x,np.sin(x),'g+',label='sin')
plt.plot(x,np.cos(x),'r--',label='cos')
plt.xlabel('angle')
plt.ylabel('sin/cos')
plt.title('sin/cos wave')
plt.ylim(-2,2)
plt.xlim(-5,15)
plt.legend()
plt.show()


# In[21]:


fig,axis=plt.subplots(1,2, figsize=(10,5))
print(axis.shape)


# In[26]:


fig,axis=plt.subplots(1,2, figsize=(10,5))
x=np.arange(0,10,0.1)
axis[0].plot(x,np.sin(x),'g+')
axis[0].set_title('sin')
axis[0].set_xlabel('angle')
axis[0].set_ylabel('sin')
axis[1].plot(x,np.cos(x),'r--')
axis[1].set_title('cos')
axis[1].set_xlabel('angle')
axis[1].set_ylabel('cos')
plt.show()


# In[29]:


fig,axis=plt.subplots(2,2,figsize=(10,10))
x=np.arange(0,10,0.1)
axis[0][0].plot(x,np.sin(x),'y--')
axis[0][0].set_title('sin')
axis[0][0].set_ylim(-3,3)
axis[0][1].plot(x,2*np.sin(x),'g--')
axis[0][1].set_title('sin')
axis[0][1].set_ylim(-3,3)
axis[1][0].plot(x,np.cos(x),'b--')
axis[1][0].set_title('cos')
axis[1][0].set_ylim(-3,3)
axis[1][1].plot(x,2*np.cos(x),'r--')
axis[1][1].set_title('cos')
axis[1][1].set_ylim(-3,3)
plt.show()


# In[30]:


x=np.random.random(100)*100
y=np.random.random(100)*100
plt.scatter(x,y)
plt.xlabel('price')
plt.ylabel('demand')
plt.title('stock')
plt.show()


# In[32]:


x=np.array([1,2,3])
y=[98,85,100]
plt.bar(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar chart')
plt.show()


# In[37]:


slice=[12,25,50,36,19]
activities=['NLP','Neural network','Data analytics','Quantum computing','Machine learning']
cols=['r','b','g','y','orange']
plt.pie(slice,labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0,0),
        autopct='%1.1f%%')
plt.title('Training subjects')
plt.show()


# In[43]:


days=[1,2,3,4,5]
humidity=[22,24,23,12,34]
temp=[23,45,63,76,41]
plt.plot([],[],color='c',label='Weather predicted',linewidth=5)
plt.plot([],[],color='g',label='weaather change happened',linewidth=5)
plt.stackplot(days,humidity,temp,colors=['c','g'])
plt.xlabel('Fluctuation with time')
plt.ylabel('Days')
plt.title('Weather Report using area plot')
plt.legend()
plt.show()


# In[45]:


pop=[22,33,42,45,64,76,3,4,6,8]
bins=[1,10,20,30,40,50]
plt.hist(pop,bins,rwidth=1)
plt.title('Histogram')
plt.show()


# In[ ]:




