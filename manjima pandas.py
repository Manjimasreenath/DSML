#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
data=pd.Series([10,20,30,40,50,60,70])
data


# In[6]:


data=pd.Series([10,20,30,40,50,60,80],index=['a','b','c','d','e','f','g'],dtype='int8')
data


# In[10]:


data.values


# In[11]:


array_data=data.values
print(array_data)


# In[12]:


data.index


# In[14]:


data_series={
    'Column1':pd.Series([100,200,300,400,500,600,700],dtype='int16'),
    'Column2':pd.Series([10,20,30,40,50,60,70],dtype='int16')
}
pd.DataFrame(data_series)


# In[15]:


movies_df=pd.read_csv('https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/boston_train.csv',sep=',')


# In[16]:


movies_df.head()


# In[17]:


movies_df.tail()


# In[2]:


import pandas as pd
stock_data=pd.read_excel("https://github.com/ammishra08/MachineLearning/raw/master/Datasets/data_akbilgic.xlsx",header=1)


# In[22]:


pip install openpyxl


# In[3]:


stock_data


# In[4]:


movies_df.shape


# In[5]:


movies_df=pd.read_csv('https://raw.githubusercontent.com/ammishra08/MachineLearning/master/Datasets/boston_train.csv',sep=',')
movies_df.shape


# In[6]:


movies_df.columns


# In[9]:


len(movies_df.columns)


# In[10]:


print(movies_df.shape[0], movies_df.shape[1])


# In[11]:


data_series = {
'Column1': pd.Series([100, 200, 300, 400, 500, 600],
index=['a', 'b', 'c', 'd', 'e', 'f'], dtype='int16'),
'Column2': pd.Series([10, 20, 30, 40, 50, 70],
index=['a', 'b', 'c', 'd', 'e', 'g'], dtype='int16')
}
df = pd.DataFrame(data_series)
df


# In[12]:


df.isnull() 


# In[13]:


df.isnull().sum() 


# In[14]:


df.isna().sum() 


# In[15]:


df.notnull() 


# In[16]:


df[df['Column1'].isnull() == True] 


# In[18]:


df[df['Column2'].isnull() == True] 


# In[ ]:




