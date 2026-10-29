#!/usr/bin/env python
# coding: utf-8

# # lambda Function

# In[2]:


a=lambda x,y:x+y
print(a)
a(5,7)


# In[3]:


sub_string=lambda s:s in "welcome lju"
sub_string("lj")


# In[5]:


(lambda a,b:a*b)(2,4)


# In[7]:


a=lambda x,y=15,z=24:x+y+z
a(1)


# In[11]:


a(1,2)


# In[10]:


print(a(y=18,x=3,z=10))


# # map 

# In[14]:


l=[3,5,8,10,9]
list(map(lambda x:x*2,l))


# In[16]:


list(map(lambda x:"even" if x%2==0 else "odd",l))


# # Filter

# In[17]:


l=[3,5,8,10,9]
list(filter(lambda x:x>5,l))


# In[18]:


fruits=["apple","banana","cherry"]
list(filter(lambda x:x.startswith("c"),fruits))


# # Reduce 

# In[19]:


from functools import reduce
l=[3,5,8,10,9]
reduce(lambda x,y:x+y,l)


# # Sorted

# In[24]:


l=[3,5,8,10,9]
print(sorted(l))
print(sorted(l,reverse=True))
d={1:"a",2:"c",3:"b"}
print(sorted(d.items()))
print(sorted(d.items(),key=lambda x:x[1]))
t=["shp12","Shp","shp1234"]
print(sorted(t,key=len))
print(sorted(t,key=len,reverse=True))


# In[27]:


# WPP to print smallest positive missing value from the list
# input= [10,0,3,-4,2,1]
# output= 4
def find_smallest_missing_positive(nums):
    # Convert the list to a set for O(1) lookups
    num_set = set(nums)

    # Start checking from the smallest positive integer
    missing = 1
    while missing in num_set:
        missing += 1

    return missing

# Given input list
input_list = [10, 0, 3, -4, 2,1]

# Get the result and print it
output = find_smallest_missing_positive(input_list)
print("Output:", output)


# In[29]:


l=[10,0,3,-4,2,1]
l=set(l)
i=1

while(True):
    if i not in l:
        print("Smallest +ve no=",i)
        break
    i+=1


# In[60]:


s=input("Enter a String:")

split_S=s.split()
print(split_S)
print()
rev_s=""
for i in split_S:
    rev_s+=i[::-1]+" "
print("Output-1:",rev_s)
print()
word_length_dict={w: len(w) for w in split_S}
print("output-2:",word_length_dict)
print()
vowels = set("aeiouAEIOU")
list_3vowels=[]
for i in split_S:
    c=sum(1 for ch in i if ch in vowels)
    if c>=3:
        list_3vowels.append(i)
print("Output-3:",list_3vowels)
print()
categories={"vowels":0,"consonant":0,"digits":0,"special char":0}
for ch in s:
        if ch in vowels:
            categories["vowels"] += 1
        elif ch.isalpha():
            categories["consonant"] += 1
        elif ch.isdigit():
            categories["digits"] += 1
        else:
            categories["special char"] += 1
print("Output-4:",categories)
print()
highest_category = max(categories, key=categories.get)
print("Output-5:",highest_category)
print()
unique={w:len(set(w.lower())) for w in split_S+}
max_unique = max(unique.values())
words_max_unique = [w for w, count in unique.items() if count == max_unique]
print("Output-6:",words_max_unique)


# In[58]:


# WPP to find highest ODD number from the list
l=eval(input("Enter List:"))
n_l=list(filter(lambda x:x if x%2!=0 else "",l))
print(max(n_l))


# In[61]:


"""Write a Python program to manage and analyze a small library’s book database using strings, lists, and dictionaries. 
Static Input: Use the following list of strings as input data (no user input required):
books_data = [ "Inferno,Dan Brown,Thriller,450,4.5", "Atomic Habits,James Clear,SelfHelp,550,4.8", "Ikigai,Hector Garcia,
SelfHelp,300,4.2","Dune,Frank Herbert,ScienceFiction,600,4.6", "1984,George Orwell,ScienceFiction,500,4.7" ]
Your Task: Convert the above list of strings into a dictionary, where: The key = book title The value = another dictionary
with: {"Author": ..., "Genre": ..., "Price": ..., "Rating": ...}
Perform the following analyses: a. Display the average price of all books. 
                                b. Display the highest-rated book (title, author, rating). 
                                c. Group books by genre and show the count of books in each genre.
                                d. Display all ScienceFiction books sorted by rating (descending). 
                                e. (Bonus) Display the most expensive book in each genre.
Expected Output:
Average Price of all books: 480.0
Highest Rated Book:
Atomic Habits by James Clear (Rating: 4.8) 
Books by Genre: 
Thriller: 1 
SelfHelp: 2
ScienceFiction: 2 
ScienceFiction Books(sorted by rating):
1. 1984 — 4.7
2. Dune — 4.6 
Most Expensive Book per Genre: 
Thriller: Inferno (450) 
SelfHelp: Atomic Habits (550) 
ScienceFiction: Dune (600)"""

# Static input
books_data = [
 "Inferno,Dan Brown,Thriller,450,4.5",
 "Atomic Habits,James Clear,SelfHelp,550,4.8",
 "Ikigai,Hector Garcia,SelfHelp,300,4.2",
 "Dune,Frank Herbert,ScienceFiction,600,4.6",
 "1984,George Orwell,ScienceFiction,500,4.7"
]
# Step 1: Convert list of strings into a nested dictionary
books_dict = {}
for record in books_data:
 parts = record.split(",") # Split each string by comma
 title = parts[0].strip()
 author = parts[1].strip()
 genre = parts[2].strip()
 price = float(parts[3].strip())
 rating = float(parts[4].strip())

 books_dict[title] = {
 "Author": author,
 "Genre": genre,
 "Price": price,
 "Rating": rating
 }
print(books_dict)
# Step 2a: Average price of all books
total_price = sum(book["Price"] for book in books_dict.values())
average_price = total_price / len(books_dict)
print(f"Average Price of all books: {average_price:.1f}\n")
# Step 2b: Highest-rated book
highest_rated_book = max(books_dict.items(), key=lambda x: x[1]["Rating"])
title, info = highest_rated_book
print("Highest Rated Book:")
print(f"{title} by {info['Author']} (Rating: {info['Rating']})\n")
# Step 2c: Books grouped by genre
genre_count = {}
for info in books_dict.values():
    genre = info["Genre"]
    genre_count[genre] = genre_count.get(genre, 0) + 1
print("Books by Genre:")
for genre, count in genre_count.items():
    print(f"{genre}: {count}")
print()
# Step 2d: ScienceFiction books sorted by rating (descending)
sci_fi_books = [(title, info["Rating"]) for title, info in books_dict.items() if info["Genre"] == "ScienceFiction"]
sci_fi_books.sort(key=lambda x: x[1], reverse=True)
print("ScienceFiction Books (sorted by rating):")
for i, (title, rating) in enumerate(sci_fi_books, start=1):
    print(f"{i}. {title} — {rating}")
print()
# Step 2e: Most expensive book per genre (Bonus)
most_expensive_per_genre = {}
for title, info in books_dict.items():
    genre = info["Genre"]
    price = info["Price"]
    if genre not in most_expensive_per_genre or price > most_expensive_per_genre[genre]["Price"]:
        most_expensive_per_genre[genre] = {"Title": title, "Price": price}
print("Most Expensive Book per Genre:")
for genre, data in most_expensive_per_genre.items():
    print(f"{genre}: {data['Title']} ({data['Price']})")


# In[11]:


books_data = [
 "Inferno,Dan Brown,Thriller,450,4.5",
 "Atomic Habits,James Clear,SelfHelp,550,4.8",
 "Ikigai,Hector Garcia,SelfHelp,300,4.2",
 "Dune,Frank Herbert,ScienceFiction,600,4.6",
 "1984,George Orwell,ScienceFiction,500,4.7"
]
library={}
for i in books_data:
    title,author,genre,price,rating=i.split(",")
    library[title]={"author":author,"genre":genre,"price":int(price),"rating":float(rating)}
print(library)

t=0
for i in library.values():
    t+=i["price"]
print("AVG price of book=",t/len(library))
print()
h_title=""
h_rate=0
for i,j in library.items():
    if j["rating"]>h_rate:
        h_rate=j["rating"]
        h_title=i
print("Highest rated book=",h_title,library[h_title]["rating"],library[h_title]["author"])
print()

print("Books by Genre:")
gen={}
for i,j in library.items():
    genre=j["genre"]
    if genre not in gen:
        gen[genre]=1
    else:
        gen[genre]+=1
print(gen)
for i,j in gen.items():
    print(i,"-",j)
print()
gen1={}
for i,j in library.items():
    genre=j["genre"]
    if genre not in gen1:
        gen1[genre]=[i]
    else:
        gen1[genre].append(i)
print(gen1)
for i,j in gen1.items():
    print(i,"-",len(j),"-",",".join(j))
print()
sf=[]
for i,j in library.items():
    if j["genre"]=="ScienceFiction":
        sf.append((j["rating"],i))
print(sf)
sf.sort(reverse=True)
print("ScienceFiction Books (sorted by rating):")
for i,j in sf:
    print(j,"-",i)


# In[23]:


#WAP to find sum & avg. of a digits present in string which is entered by user.

s=input("Enter a digit:")
sum1=0
c=0
for i in s:
    if not(i.isalpha()):
        sum1+=int(i)
        c+=1
print("Sum:",sum1)
if c>0:
    print("AVG:",sum1/c)


# In[ ]:




