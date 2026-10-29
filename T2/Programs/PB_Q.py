#!/usr/bin/env python
# coding: utf-8

# In[3]:


l=[1,2,(5,)]
l[2][0]=7
print(l)


# In[4]:


d={1:"welcome",[1]:{1:2}}
print(d[[1]])


# In[9]:


x = ['ab', 'cd'] 
c=0
for i in x:
       x[c] = i.upper()
       c+=1
print(x)


# In[12]:


from functools import *
Series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range (n-2) , [0,1])
Series(5)


# In[15]:


def writer():
    title = 'Sir'
    name = (lambda x: title + ' ' * 2*x)
    return name
who = writer()
print(who('Arthur'))


# In[16]:


L = list('123456')
L[0] = L[5] = 0
L[3] = L[-2]
L[5]=1
L[-2]=4
L[2]=L[-1]
L[4]=L[3]
L[-1]=L[3]
print(L)


# In[18]:


tuple = {}
tuple[(1,2,4)] = 8
print(tuple)
tuple[(4,2,1)] = 10
print(tuple)
tuple[(1,2)] = 12
print(tuple)
_sum = 0
for k in tuple:
           _sum += tuple[k]
print(len(tuple) + _sum)


# In[19]:


L1 = [1, 1.33, 'LJU', 0, 'N', True, 'Y', 1]
val1= 0
val2= ""
for x in L1:
    if(type(x) == int or type(x) == float):
        val1 += x
    elif(type(x) == str):
        val2 += x
    else:
        break
        continue
print(val1, val2)


# In[20]:


L1 = [ ]
L1.append([1, [2, 3], 4])
L1.extend([7, 8, 9])
print(L1)
print(L1[0][1][1] + L1[2])


# In[22]:


def F(B,A=3,*C,**D):
    print(B)
    print(A)
    sum=A+B
    for i in C:
        sum=sum+i
    for i in D.values():    
        sum=sum+i
    return sum
print(F(1,5,7,4,3,e=1,f=2))


# In[ ]:




