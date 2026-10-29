#!/usr/bin/env python
# coding: utf-8

# # 5.WAP to check password validation

# In[ ]:


#Length must be exact 8, atleast 1 Upperchar,lowerchar,digit & Special Char from (@#$&)

password=input("Enter Password:")
u=l=d=c=0

for i in password:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    elif (i=='@' or i=='#' or i=='$' or i=='&'):
        c+=1

if (len(password)==8 and u>=1 and l>=1 and d>=1 and c>=1):
    print("Password is valid!")
else:
    print("Password is invalid!")


# # 6.WAP to remove i'th char from string

# In[11]:


s=input("Enter String:")
ind=int(input("Enter Index no. to remove:"))
print(s[:ind]+s[ind+1:])


# # 7.WAP to check weather entered strings are balanced or not 

# In[9]:


#  All Characters of string should be present in s2 and length must be same 

s1="hello"
s2="lleho"

f=0
if len(s1)==len(s2):
    for i in s1:
        if i in s2:
            continue
        else:
            f+=1
    if(f>0):
        print("Not Balanced")
    else:
        print("Balanced")
else:
    print("Not balanced")


# # 8.WAP to find sum and average of digits in string entered by user

# In[14]:


s="Dhruv1234dqh12"
sum1=c=0

for i in s:
    if i.isdigit():
        sum1+=int(i)
        c+=1
print("Sum=",sum1)
print("AVG=",sum1/c)


# # 9.WAP using user defined function of shift decimal number up to n places to the left.
# # Wrapping the extra digits around. it shifts no of digits then reverse the no.

# In[18]:


def shift_no(n,shift):
    n=str(n)
    le=len(n)
    if shift>=le:
        r=n[::-1]
    else:
        r=n[shift:]+n[:shift]
    return int(r)
n=int(input("Enter No.:"))
shift=int(input("Enter shift:"))
shift_no(n,shift)


# # 10.WAP to create ceaser encrytion(ljiet eng--->omlhw hqj , shift=3)

# # Method-1

# In[24]:


s=input("Enter String:")
s1=s.lower()
key=int(input("Enter Shift key:"))
alpha="abcdefghijklmnopqrstuvwxyz"
r=""

for i in s1:
    if i.isalpha():
        letter_index=(alpha.find(i)+key)%len(alpha)
        r+=alpha[letter_index]
    else:
        r+=i

if s.isupper():
    print(r.upper())
else:
    print(r)


# # Method-2

# In[28]:


s=input("Enter String:")
key=int(input("Enter Shift key:"))
c=""

for i in s:
    if i.isalpha():
        if i.isupper():
            c+=chr((ord(i)-ord("A")+key)%26+ord("A"))
        elif i.lower():
            c+=chr((ord(i)-ord("a")+key)%26+ord("A"))
    else:
            c+=i
print(c)


# In[27]:


s="hello"
print(min(s))
print(max(s))
print(sorted(s))


# # Tuple

# In[38]:


t=(1,2,3,4)
print(type(t))
t1=(10)
print(type(t1))
t2=(10,)
print(type(t2))
t3=1,2,3,4
print(type(t3))


# In[37]:


t=tuple(range(1,10,1))
print(t)


# In[51]:


t=(1,2,3,4,5,6)
print(t[2])
print(t[-2])
print(t[1:5])
print(t[:1])
print(t[1:-6])
print(t[1:-1:2])
print(t*2)
print(t+('a','b'))
# print(("a","b")>(1,2)) comparison operator will not support for different datatype of tuples
print(("a","b")>("d","e"))


# In[61]:


t=(1,2,"asd","pqr")
print(t[2][-1])
print(t[-1][-2])


# In[69]:


t=(1,2,3,4,5,6)
print(len(t))
print(t.count(6))
print(t.index(6)) #If given index is more than length then it gives error
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t))
print(sorted(t,reverse=True))
for i in t:
    print(i)


# In[68]:


a,b,c,d=(1,2,3,4)
print(b)


# In[70]:


t=eval(input("Enter Tuple:"))
print(t)


# # WAP to print sum of even numbers & Sum odd numbers from the Tuple

# In[71]:


t=eval(input("Enter Tuple:"))
print(t)
o=0
e=0
for i in t:
    if i%2==0:
        e+=i
    else:
        o+=i
print("Sum of Odd:",o)
print("Sum of Even:",e)


# # WAP to encrypt your message using the shift key 

# In[73]:


s=input("Enter String:")
key=int(input("key="))
s1=""

for i in range(key):
    s1+=s[i::key]
print(s1)

