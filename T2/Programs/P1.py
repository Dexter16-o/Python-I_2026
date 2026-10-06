# # Indexing
s="Python@123"
print(s[2])
print(s[-3])
# print(s[10]) Gives indext out of range
# s[2]="x" gives TypeError: 'str' object does not support item assignment
# # Slicing
#index  +ve direction left to right (number start will 0)
#index -ve direction right to left (number start with -1)
s1="Python is very easy" 
print(s1[0:8]) #start from zero to 7th index By default Stepping is +1
print(s1[:6]) #start from zero
print(s1[8:]) #ends with last character
print(s1[3:12:2]) #with 2 stepping
print(s1[:]) #String as it is
print(s1[::]) #string as it is
print(s1[-1:-5]) #no output , stepping must be minus integer for output
print(s1[-1:-5:-1])
print(s1[:-1]) #goes from zero to last except -1
print(s1[::-1]) #read string from backwards , reverse the string
print(s1[-1:5]) #No output , stepping must be minus integer for output
print(s1[-6:-2])
print(s1[:20]) #will not give index out of bound error
# # Mathematical operation(+,=)
a="Python"
print(a*5)
print(a+"hello")
# # Comparison Operation(>,<,>=,<=)
s1=input("Enter String:")
s2=input("Enter String:")
##string not compare with length ....it compare with ascii value of first letter
if s1==s2:
    print("same")
elif s1>s2:
    print("s1 is greater")
else:
    print("s2 is greater")
print(s1>s2)
# # Format of String
a=5
b=10
print(f"a={a} and b={b}")
print("a={} and b={}".format(a,b))

name="rohan"
salary=100000
age=26
print("{}'s salary is {} and his age is {} ".format(name,salary,age))
print("{0}'s salary is {1} and his age is {2} ".format(name,salary,age))
print(f"{name}'s salary is {salary} and his age is {age} ")
# # Join Function
t=("abs","dfg","gsd")
s="-".join(t)
print(s)
# # Important Function os string
# # 1. len,strip,rstrip,lstrip
s="  python "
print(s)
print(len(s))
x=s.strip()
print(x)
print(len(x))
y=s.rstrip()
print(y)
print(len(y))
z=s.lstrip()
print(z)
print(len(z))
a="banana"
a=a.strip("a") #strip function will only remove the characters from begin & end can't remove characters between them
print(a)
#same we can use with argument function with lstrip & rstrip
# # 2. Upper, Lower, Swapcase, title, capitalize
s1="this Is my bag"
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())
print(s1.capitalize())
# # 3. Boolean functions (is functions) 
s1="asd123"
print(s1.isalnum())
s2="asd"
print(s2.isalpha())
s3="123"
print(s3.isnumeric())
print(s1.isdigit())
s4="ASD"
print(s4.isupper())
print(s4.islower())
print(s4.istitle())
s5=" "
print(s5.isspace())
print("hello hi".isspace())
print(s1.isidentifier())
print('a@1'.isidentifier())
# # 4. Find, rfind, count, replace, split, enumerate, punctuation(?,"",!)
#return Index no
s="this is myi bag"
print(s.find("i"))
print(s.rfind("i"))
print(s.find("i",11,13)) #if character not available return by default -1
print(s.count("i"))
print(s.count("i",4,12))
s1="hello hii hiii"
print(s1.replace("hi","@"))
s2="this is my bag"
print(s2.split())
print(s2.split("is"))
l1=list(enumerate(s1))
print(l1)
l2=list(enumerate(s1,4)) #start indexing form 4
print(l2)
import string
print(string.punctuation)
s3="hellp???!!!$$@@"
print(s3)
for i in string.punctuation:
    s3=s3.replace(i,"")
print("after punctuation:",s3)
# # WAP to chek enter string is palindrome or not
n='malayalam'
m=n[::-1]
if n==m:
    print("pelindrome")
else:
    print("not")
# # WAP to convert first half string in upper case and 2nd half string in lowe case...
a="Python"
n=len(a)//2
print(a[:n].upper()+a[n:].lower())
# # WAP tp check weather the entered string is balanced or not
# All Characters of string should be present in s2
s1=input("Enter String s1:")
s2=input("Enter String s2:")
c=0
for i in s1:
    if i in s2:
        continue
    else:
        c+=1
if c>0:
    print("not balanced")
else:
    print("balanced")
# # 4. WAP to count no of uppercase alphabate,lowercase,digits,space and special char
s1=input("Enter String:")
u=l=d=s=c=a=0

for i in s1:
    if i.isalpha():
        a+=1
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
    else:
        c+=1
print("Alphabates:",a,"| Uppercase:",u,"| Lowercase:",l,"| Digit:",d,"| Space:",s,"| Special character:",c)

