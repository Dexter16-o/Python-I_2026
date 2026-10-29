#!/usr/bin/env python
# coding: utf-8

# # SET

# In[3]:


#Unordered hetrogeneous ds
#Duplicate are not allowed
s={1,2,3,4}
s1=set()
print(s)
print(type(s))
print(type(s1))


# In[4]:


print(set([1,2,"a",1,"b"]))


# In[5]:


print(set(range(11,16)))


# # mathematical operations of set

# # union

# In[6]:


x={1,2,3,4}
y={3,4,5,6}
print(x|y)
print(x.union(y))


# # intersection

# In[7]:


x={1,2,3,4}
y={3,4,5,6}
print(x&y)
print(x.intersection(y))


# # Difference

# In[6]:


x={1,2,3,4}
y={3,4,5,6}
print(x-y)
print(x.difference(y))
print(y-x)
print(y.difference(x))


# # Symmetric difference

# In[ ]:


x={1,2,3,4}
y={3,4,5,6}
print(x^y)
print(x.symmetric_difference(y))


# In[12]:


print("h" in set("hello"))
print("x" not in set("hello"))


# # impoimportant functions of set

# # add()

# In[13]:


s={1,2,3}
s.add(10)
print(s)
s.add(2)
print(s)


# # update()

# In[20]:


s={1,2,3}
s1=[7,8]
s.update(s1,range(11,15))
print(s)
s.update(("a"))
print(s)
s.update(("ab"))
print(S)


# # COPY()

# In[22]:


s={1,2,3}
s1=s.copy()
s.add(10)
print(s)
print(s1)


# # pop()

# In[26]:


s={1,2,3,4}
s.pop()
print(s)


# # remove()

# In[28]:


s={1,2,3,4}
s.remove(3)
print(s)
# s.remove(31)
# print(s)


# # discard()

# In[29]:


s={1,2,3,4}
s.discard(3)
print(s)
s.discard(31)
print(s) #discard will not give error but remove give error


# # clear(),del

# In[31]:


s={1,2,3,4}
s.clear()
print(s)
del s #it will delete set
# print(s)


# # Set comperehension

# In[32]:


print({x**2 for x in range(1,6)})


# In[33]:


s="asd"
print(s.startswith("a"))
print(s.endswith("d"))


# # tuple comprehension

# In[34]:


print((x**2 for x in range(1,6)))


# In[35]:


print(list(x**2 for x in range(1,6)))


# In[36]:


a=(x**2 for x in range(1,6))
for i in a:
    print(i)


# # Q460

# In[39]:


def analyze_string(user_input):
    vowels = set("aeiouAEIOU")

    # 1) Reverse each word but keep word order
    reversed_words = " ".join([word[::-1] for word in user_input.split()])
    print("1) String with each word reversed:")
    print(reversed_words)

    # 2) Dictionary with word lengths
    word_lengths = {word: len(word) for word in user_input.split()}
    print("\n2) Dictionary with word lengths:")
    print(word_lengths)

    # 3) Words with at least 3 vowels
    words_with_vowels = [word for word in user_input.split() if sum(1 for ch in word if ch in vowels) >= 3]
    print("\n3) Words containing at least 3 vowels:")
    print(words_with_vowels)

    # 4) Character categories
    categories = {"vowels": 0, "consonants": 0, "digits": 0, "special": 0}
    for ch in user_input:
        if ch in vowels:
            categories["vowels"] += 1
        elif ch.isalpha():
            categories["consonants"] += 1
        elif ch.isdigit():
            categories["digits"] += 1
        else:
            categories["special"] += 1
    print("\n4) Character categories:")
    print(categories)

    # 5) Category with highest count
    highest_category = max(categories, key=categories.get)
    print("\n5) Category with highest count:")
    print(highest_category)

    # 6) Words with highest number of unique letters (case-insensitive)
    word_unique_counts = {word: len(set(word.lower())) for word in user_input.split()}
    max_unique = max(word_unique_counts.values())
    words_max_unique = [word for word, count in word_unique_counts.items() if count == max_unique]
    print("\n6) Words with the highest number of unique letters:")
    print(words_max_unique)


user_input = input("Enter a string: ")
analyze_string(user_input)

