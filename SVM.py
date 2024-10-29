#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


# In[2]:


newsgroups=fetch_20newsgroups(subset='all',categories=['sci.space', 'rec.autos'], shuffle=True, random_state=42)
X, y=newsgroups.data, newsgroups.target


# In[3]:


vectorizer=TfidfVectorizer(stop_words='english')
X=vectorizer.fit_transform(X)


# In[4]:


X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=42)


# In[5]:


svm=SVC(kernel='linear')
svm.fit(X_train, y_train)


# In[6]:


y_pred=svm.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=newsgroups.target_names))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# In[7]:


from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
newsgroups=fetch_20newsgroups(subset='all',categories=['sci.space', 'rec.autos'], shuffle=True, random_state=42)
X, y=newsgroups.data, newsgroups.target
vectorizer=TfidfVectorizer(stop_words='english')
X=vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=42)
svm=SVC(kernel='linear')
svm.fit(X_train, y_train)

