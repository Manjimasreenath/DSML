#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


a=5
print(a)
print(type(a))


# In[3]:


f=1.5
print(f)
print(type(f))


# In[4]:


s="hello"
print(s)
print(type(s))


# In[5]:


b=True
print(b)
print(type(b))


# In[6]:


t=True
f=False
print(t,f)
print(type(t))


# In[7]:


t=5+3j
print(t)
print(type(t))


# In[8]:


a=7
b=3
sum=a+b
print(sum)


# In[9]:


a=7
b=3
diff=a-b
print(diff)


# In[10]:


a=7
b=3
pro=a*b
print(pro)


# In[11]:


a=4
b=2
quo=a/b
print(quo)


# In[12]:


a=7
b=3
quo=a/b
print(quo)


# In[14]:


a=7
b=3
iquo=a//b
print(iquo)


# In[15]:


a=7
b=3
rem=a%b
print(rem)


# In[16]:


a=7
b=3
pow=a**b
print(pow)


# In[17]:


t=True
f=False
print(t,f)


# In[18]:


p=5>3
print(p)


# In[19]:


q=-1<-12.5


# In[20]:


q=-1<-12.5
print(q)


# In[21]:


print(p and q)


# In[22]:


print(p or q)


# In[23]:


print(not q)


# In[24]:


s='hello'
u="hello"
print(s)
print(u)


# In[25]:


s1="python"
s2="world"
s3=s1+''+s2
print(s3)


# In[26]:


s1="python"
s2="world"
s3=s1+' '+s2
print(s3)


# In[28]:


s3='%s %s %d' %(s1,s2,1011)
print(s3)


# In[29]:


print(len(s3))


# In[30]:


print(s3.upper())


# In[31]:


print(s3.capitalize())


# In[32]:


print(s3.lower())


# In[33]:


print('hello world how are you'.split(' '))


# In[35]:


print('book'.replace('o','e'))


# In[37]:


word='jewellery'
print(word.find('well'))
print(word.find('is'))


# In[39]:


number=123
if number>99 and number<1000:
    print('3 digit')
else:
    print('not 3 digit')


# In[41]:


response=input('Are you familiar with python')
if response.upper()=='YES':
    print("You can skip this course:-)")
elif response.upper()=='NO':
    print("You are at the right place:-)")
else:
    print('Sorry wrong input:-(')


# In[42]:


response=input('Are you familiar with python')
if response.upper()=='YES':
    print("You can skip this course:-)")
elif response.upper()=='NO':
    print("You are at the right place:-)")
else:
    print('Sorry wrong input:-(')


# In[44]:


response=input('Are you familiar with python')
if response.upper()=='YES':
    print("You can skip this course:-)")
elif response.upper()=='NO':
    print("You are at the right place:-)")
else:
    print('Sorry wrong input:-(')


# In[46]:


for x in range(10):
    print(x,end=' ')
    


# In[ ]:


limit=int(input('Enter a limit:'))
sum=0
for i in range(1,limit+1):
    if i%2!=0:
        sum+=i
print("Odd sum="+str(sum))


# In[49]:


print(list(range(10)))


# In[50]:


print(list(range(1,10)))


# In[51]:


print(list(range(1,10,2)))


# In[ ]:


number=int(input("Enter a number:"))
s=0
while number>0:
    s+=number%10
    number=number//10
print(s)


# In[ ]:


limit=int(input("Enter a number:"))
for num in range(2,limit+1):
    is_divisible=False
    k=2
    while k<=num//2:
        if num%k==0:
            is_divisible=True
            break;
        k+=1
    if not is_divisible:
         print(num,end=" ")


# In[ ]:


limit=int(input("Enter a number:"))
for num in range(2,limit+1):
    is_divisible=False
    k=2
    while k<=num//2:
        if num%k==0:
            is_divisible=True
            break;
            k+=1
            if not is_divisible:
                print(num,end=" ")


# In[ ]:




