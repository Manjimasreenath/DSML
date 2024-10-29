#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn import tree
data=load_iris()
x=data.data
y=data.target
print(x.shape,y.shape)


# In[15]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)
clf=DecisionTreeClassifier(random_state=10)
clf.fit(x_train,y_train)


# In[16]:


y_pred=clf.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy of the Decision Tree Classifier: {accuracy:.2f}")


# In[18]:


print("\nConfusion Matrix:")
print(confusion_matrix(y_test,y_pred))


# In[21]:


print("\nClassification Report:")
print(classification_report(y_test,y_pred))


# In[20]:


plt.figure(figsize=(12,8))
plot_tree(clf,feature_names=data.feature_names,class_names=data.target_names,filled=True)
plt.title("Decision Tree for Iris Dataset")
plt.show()


# In[22]:


new_data=[[5.1,3.5,1.4,0.2],[6.2,3.4,5.4,2.3]]
predictions=clf.predict(new_data)
for prediction in predictions:
    print(f"Predicted class:{prediction}")


# In[ ]:




