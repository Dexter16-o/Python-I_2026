# Converted from Lec_5_6.ipynb

# # PB 486

# """Write a python program to accept string/sentence from user till the user enters “END”. Each string/sentence entered by 
# user should be a newline in file. Save all the lines in file and display only those lines which begin with capital letter.
# Example:
# Enter Something (for quit enter END):Hi Friends
# Enter Something (for quit enter END):how are you all
# Enter Something (for quit enter END):I am fine
# Enter Something (for quit enter END):hope you all are fine
# Enter Something (for quit enter END):END
# The Line started with Capital Letters:
# Hi Friends
# I am fine """

f=open("Sentences.txt","w")

while True:
    x=input("Enter Something(for quit enter END):")
    if x=="END":
        break
    f.write(x+"\n")
f.close()
f1=open("Sentences.txt")
a=f1.readlines()
for i in a:
    if i[0].isupper():
        print(i.strip())

# # PB 487

# Write a program to compare two text files. If they are different, give the line and column numbers in the files where the first 
# difference occurs.
# Example:
# File 1: python1.txt
# Friends are crazy, Friends are naughty !
# Friends are honest, Friends are  best !
# Friends are like keygen, friends are like license key !
# new We are nothing without friends, Life is not possible without friends !
# File 2: python2.txt   
# Friends are crazy, Friends are naughty !
# Friends 6re honest, Friends are  best !
# Friends are like keygen, friends are like license key !
# new We are nothing without friends, Life is not possible without friends !    
# Output:
# line number 2 colNo. 9

f1=open("Pyhton1.txt")
f2=open("Pyhton2.txt")
a=f1.readlines()
b=f2.readlines()

for i,j in enumerate(a):
    if j!=b[i]:
        for k,m in enumerate(j):
            if m!=b[i][k]:
                print("Line no=",i+1,"Column no=",k+1)
                break
        break
f1.close()
f2.close()

# # PB 488

# Write a  python program to read through the mbox-short.txt and figure out who has 
# sent the  greatest number of mail messages. The program looks for 'From ' lines and 
# takes the    second word of those lines as the person who sent the mail. The program
# creates a  Python    dictionary that maps the sender's mail address to a count of the 
# number of   times they  appear in the file. After the dictionary is produced, the program reads through the dictionary to 
# identify the sender with the maximum count (the most prolific sender).
# Expected Output:
# {'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 
# 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1, 
# 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}
# cwen@iupui.edu 5

# Method-I
f = open("mbox-short.txt")
a=f.readlines()
counts = {}

for line in a:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender, 0) + 1

max_sender = None
max_count = None

for sender, count in counts.items():
  if max_count is None or count > max_count:
    max_sender = sender
    max_count = count

print(counts)
print(max_sender, max_count)

# Method-II
f = open("mbox-short.txt")
a=f.readlines()
d = {}
l=[]
for i in a:
    if not i.startswith("From "):
        continue
    else:
        b=i.split()
        l.append(b[1])
for i in l:
    d[i]=d.get(i,0)+1
print(d)
m=max(d.values())
for k,v in d.items():
    if v==m:
        print(k,"-",v)

# Text processing program---out of pb
"""Create a program to scan a text file for all lines longer than 80 chars.
For each of the offering lines find the closet word before 80 chars and break the line there.
Insert the remaining text to the next line there should be no lines longer than 80 chars."""

f=open("bhai.txt")
aa=f.readlines()
f1=open("bhai_output.txt","w")
l=[]
def process(a):
    if len(a)<=80:
        l.append(a)
    else:
        if a[79]==" ":
            l.append(a[:80]+"\n")
            process(a[80:])
        elif a[79]!=" ":
            ind=a.rfind(" ",0,79)
            l.append(a[:ind]+"\n")
            process(a[ind+1:])
for i in aa:
    process(i)
for j in l:
    f1.write(j)
f1.close()
f.close()

import mymodule
print(mymodule.x)
mymodule.product(10,20)

from mymodule import *
product(10,20)

import os
print(os.getcwd()) # it will return current working directories

os.mkdir("D:\myproject") # it will create new directory

os.rmdir("D:\myproject") # it will remove directory

os.listdir("D:\Dhruv_Python") # it will givelist of files available in directory

os.chdir("D:\Dhruv_Python") # It will change working directory

os.getcwd()

os.chdir("D:\Python")

os.remove("") # It will remove specific file from directory
