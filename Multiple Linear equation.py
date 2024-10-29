#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
data_df=pd.read_csv('SalaryMulti.csv')
data_df.head()


# In[3]:


x=data_df.drop(['Project Manager Experience'],axis=1).values
print(x)


# In[4]:


y=data_df['Project Manager Experience'].values
print(y)


# In[6]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=0)
regressor=LinearRegression()
regressor.fit(x_train,y_train)


# In[7]:


y_pred=regressor.predict(x_test)
print(y_pred)


# In[11]:


plt.figure(figsize=(15,10))
plt.scatter(y_test,y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('ACTUAL VS PREDICTED')
plt.show()
mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)


# In[12]:


print("Mean Squared Error(MSE):",mse)


# In[13]:


print("Root Mean Sqaured Error (RMSE):",rmse)


# In[14]:


print("Mean Absolute Error (MAE):",mae)


# In[15]:


print("R-Squared (R2):",r2)


# In[16]:


new_input=[[14.96,41.76,1024.07,73.17]]
y_pred=regressor.predict(new_input)
print("Predicted target value:",y_pred)


# In[ ]:




