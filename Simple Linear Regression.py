#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
dataset=pd.read_csv('salary_data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values
print(dataset.head())


# In[13]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)
regressor=LinearRegression()
regressor.fit(x_train,y_train)
plt.scatter(x_train,y_train,color='red',label='Actual')
plt.plot(x_train,regressor.predict(x_train),color='blue',label='Predicted')
plt.title('Salary Vs Experience(Training Set)')
plt.xlabel('Year of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
plt.scatter(x_test,y_test,color='red',label='Actual')
plt.plot(x_train,regressor.predict(x_train),color='blue',label='Predicted')
plt.title('Salary Vs Experience(Test Set)')
plt.xlabel('Year of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
regressor=LinearRegression()
regressor.fit(x_train,y_train)


# In[16]:


y_pred=regressor.predict(x_test)
y_pred


# In[19]:


mse=mean_squared_error(y_test,y_pred)
rmse=np.sqrt(mse)
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print("Mean Squared Error(MSE):",mse)


# In[21]:


print("Root Mean Sqaured Error (RMSE):",rmse)


# In[22]:


print("Mean Absolute Error (MAE):",mae)


# In[23]:


print("R-Squared (R2):",r2)


# In[25]:


new_input=[[5]]
y_pred=regressor.predict(new_input)
print("Predicted Salary:",y_pred)


# In[ ]:




