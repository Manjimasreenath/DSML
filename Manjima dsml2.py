#!/usr/bin/env python
# coding: utf-8

# In[3]:


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# In[4]:


mylist=['a','b',1,1.2,True]
print(mylist)
mylist.append("new")
print(mylist)


# In[5]:


print(mylist.pop())


# In[7]:


mylist.insert(2,'new')
print(mylist)


# In[9]:


mylist.remove('new')
print(mylist)


# In[10]:


b=[1,2,3]
print(b)
mylist.append(b)
print(mylist)


# In[11]:


mylist.remove(b)
print(mylist)


# In[12]:


mylist.extend(b)
print(mylist)


# In[13]:


a=[2,3,4,1,8,6]
a.sort()
print(a)


# In[14]:


print(list('hello'))


# In[15]:


num=[0,1,2,3,4,5,6,7,8,9,10]
print(num[1],num[-1])


# In[16]:


sliced=num[5:11]
print(sliced)


# In[17]:


slice1=num[5:]
print(slice1)


# In[18]:


sliced=num[:7]
print(sliced)


# In[19]:


slice2=num[-2:]
print(slice2)


# In[20]:


num=list(range(1,8))
print(num)


# In[21]:


square=[]
for i in num:
    square.append(pow(i,2))
print(square)


# In[23]:


square=[x**2 for x in num]
print(square)


# In[24]:


odd_square=[x**2 for x in num if x%2!=0]
print(odd_square)


# In[25]:


A=[4,6,8,9]
AxA=[(a,b) for a in A for b in A if a!=b]
print(AxA)


# In[26]:


person={'name':'Manji','age':22}
print(person['name'])


# In[27]:


print('name' in person)


# In[28]:


print('sex' in person)


# In[29]:


person['sex']='female'
print(person)


# In[30]:


for item in person:
    print(item,person[item])


# In[33]:


for (key,value) in person.items():
    print(key.capitalize(),'\t:\t',value)
print(person.keys())


# In[34]:


def square(num):
    return pow(num,2)
s=square(5)
print(s)


# In[35]:


def isPrime(num):
    for factor in range(2,(num//2)+1):
        if num%factor==0:
            return False
    return True
num=int(input("Enter a number:"))
print(isPrime(num))


# In[36]:


def isPrime(num):
    for factor in range(2,(num//2)+1):
        if num%factor==0:
            return False
    return True
num=int(input("Enter a number:"))
print(isPrime(num))


# In[37]:


def printPrimes(llimit,ulimit):
    for num in range(llimit,ulimit+1):
        if isPrime(num)==True:
            print(num,end=' ')
printPrimes(5,50)


# In[38]:


def swap(x,y):
    t=x
    x=y
    y=t
    return x,y
a=5
b=7
a,b=swap(a,b)
print(a,b)


# In[ ]:




