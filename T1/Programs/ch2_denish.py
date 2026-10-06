if 10>5:
    print("10 is big number")
else :
    print("10 is small number")
print("hello")

marks=int(input("enter marks: "))
if marks>=0 and marks<=100:
    if marks>=80 and marks<=100:
        print("Grade A")
    elif marks <80 and marks>=60:
        print("Grade B")
    elif marks<60 and marks>=35:
        print("Grade C")
    else:
        print("fail")
else:
    print("invalid number")

x=4
if x>10:
    print("x is above 10")
    if x>20:
        print("x is above 20")
    else:
        print("x is not above 20")
else:
    print("x is below 10")
print("Hello")

#write a python program to get differnet integer number from the user and display the max number
n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))
n3=int(input("enter number 3: "))
if(n1>n2 and n1>n3):
    print("n1 is greater number")
elif (n2>n1 and n2>n3):
    print("n2 is greater number")
else:
    print(n3,"n3 is greater number")
    

#write a python program to check whether entered year is leap year or not
year=int(input("enter year: "))
if((year%4==0 and year%100!=0) or year%400==0):
    print("year is leap year")
else:
    print("year is not a leap year")

#write a python program to arrange three different numbers in ascending and descending numbers
a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=int(input("enter number 3: "))
if a>b and a>c:
    if b>c:
        x,y,z=a,b,c
    else:
        x,y,z=a,c,b
elif b>a and b>c:
    if a>c:
        x,y,z=b,a,c
    else:
        x,y,z=b,c,a
elif c>a and c>b:
    if a>b:
        x,y,z=c,a,b
    else:
        x,y,z=c,b,a
else:
    print("valid number")
print("Ascending number: ",x,y,z)
print("Descending number: ",z,y,x)


#write a python program to get two different numbers from the user and perform arithmetic operations (+,-,*,/,//,%) as per the entered by user 
a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=input("Operation: ")
if(c=='+'):
    print("Addition of two numbers= ",(a+b))
elif(c=='-'):
    print("Subtraction of two numbers= ",(a-b))
elif(c=='*'):
    print("Multiplication of two numbers= ",(a*b))
elif(c=='/'):
    print("Division of two numbers= ",(a/b))
elif(c=='//'):
    print("Floor Division of two numbers= ",(a//b))
elif(c=='%'):
    print("Remainder of two numbers= ",(a%b))
else:
    print("invalid operations")

#electricity bill
a=0
u=int(input("enter units: "))
if(u<=100):
    print("no charge")
elif(u>100 and u<200):
    print("charges are: ",(u-100)*5)
elif(u>200):
    print("charges are: ",((u-200)*10)+500)
else:
    pass

# write a python program to check whether the enterred date by user is valid or not if the enterred date is valid then print the date of next day
d=int(input("enter date: "))
m=int(input("enter month: "))
y=int(input("enter year: "))
if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    max1=31
elif(m==4 or m==6 or m==9 or m==11):
    max1=30
elif y%4==0 and y%100!=0 or y%400==0:
    max1=29
else:
    max1=28
if(m<1 or m>13):
    print("month is invalid")
elif(d<1 or d>max1):
    print("date is invalid")
    
elif(d==max1 and m!=12):
    d=1
    m=m+1
    print("next day date is: ",d,"-",m,"-",y)
elif(d==max1 and m==12):
    d=1
    m=1
    y=y+1
    print("next day date is: ",d,"-",m,"-",y)
else: 
    d=d+1
    print("next day date is: ",d,"-",m,"-",y)

#write a python program to ask user for an hour between 1 and 12 again ask to enter am or pm and ask how many hourse into the future he want to go
#ahead print out what the hour will be that many hours into the future print with am and pm
# h=int(input("enter hour: "))
# am_or_pm=input("enter hour: ")
# ahead_hours=int(input("enter hour: "))
# if(h>12 and am_or_pm==am):
#     print(h%12,"pm")
# elif(h>12 and am_or_pm==pm):

for i in 'LJIET':
    print(i)


for i in 'LJIET':
    print('hello')

x=1
while x<=5:
    print(x)
    x+=1

for i in range(2):
    for j in range (2):
        print("i=",i,"j=",j)

for i in range(1,11):
    if i==7:
        print('stop')
        break
    print(i)

for i in range(1,11):
    if i%2==0:
        print(i)
    else:
        continue

print('*'*10)
for i in range(1,11):
    if i%2==0:
        continue
    else:
        print(i)

for i in range(1,5):
    print(i)
else:
    print('hello')

for i in range(1,5):
    if i==2:
        break
    print(i)
else:
    print('hello')

c=0
while c<1:
    c=c+1
    print(c)
else:
    print('hello')

c=0
while c<1:
    c=c+1
    print(c)
    break
else:
    print('hello')

#write a python program to print sum and average of numbers entered by users
n=int(input("enter how many numbers to enter: "))
sum=0
for i in range(n):
    a=int(input("enter number: "))
    sum+=a
print("sum of numbers is: ",sum," avg of numbers is: ",(sum/n))

#write a python program to print multiplication table
n=int(input("enter number to get table: "))
for i in range(1,11):
    print(n,' x ',i,' = ',n*i)

#write a python program to find factorial of entered number
n=int(input("enter number to gfind factorial: "))
fac=1
if(n<0):
    print("-ve not allowed")
elif n==0 or n==1:
    print("factorial = ",fac)
else:
    for i in range(n,1,-1):
        fac=fac*i
    print("factorial of ",n," is ",fac)

#write a python program to write a fibonaaci sequence
n=int(input("enter number to get fibonacci: "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

#write a python program whether number is pallindrom or not
n=int(input("enter number to check pallindrome: "))
c=n
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)
if(rev==c):
    print("number is pallindrome")
else:
    print("number is not a pallindrome")

#write a python program whether number is strong or not
n=int(input("enter number to check pallindrome: "))
c=n
sum=0

while n!=0:
    d=n%10
    
    for i in range(d,1,-1):
        fac=fac*i
    sum+=fac
    n=n//10
if(sum==c):
    print("the number is strong number")
else:
    print("the number is not a strong number")

#write a python program whether number is armstrong or not
import math
n=int(input("enter number to check pallindrome: "))
c=n
b=n
sum=0
digits=0
#or use len(str(n)) directly to count digits
while n!=0:
    #d=n%10
    digits+=1
    n=n//10
while b!=0:
    v=b%10
    sum=sum+(math.pow(v,digits))
    b=b//10
if(sum==c):
    print("the number is armstrong number")
else:
    print("the number is not a armstrong number")

n=int(input("ENter number of rows: "))
for i in range (1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

a=int(input("ENter number of rows: "))
for b in range (1,a+1):
    for c in range(1,b+1):
        print(b,end=" ")
    print()

n=int(input("ENter number of rows: "))
for i in range (1,n):
    for k in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

n=int(input("ENter number of rows: "))
for i in range (1,n+1):
    for k in range(1,i+1):
        print(" ",end=" ")
    for j in range(i,n+1):
        print("*",end=" ")
    print()

n=int(input("ENter number of rows: "))
for i in range (1,n+1):
    for k in range(1,i+1):
        print("",end=" ")
    for j in range(i,n+1):
        print("*",end=" ")
    print()

n=int(input("ENter number of rows: "))

for i in range (1,n+1):
    a=65
    g=1
    for k in range(1,n-i+1):
        print("",end=" ")
    
    for j in range(1,i+1):
        
        if i%2==0:
            print(chr(a),end=" ")
            a+=1
        else:
            print(g,end=" ")
            g+=1
        
    
    print()

n=int(input("ENter number of rows: "))
for i in range (1,n+1):
    for k in range(1,n-i+1):
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range (1,n+1):
    for k in range(1,i+1):
        print("",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

# ========================================================================
# # LCM and HCF
# ========================================================================

#write a python program to find the lcm and hcf of two integer number
a=int(input("Enter number: "))
b=int(input("Enter number: "))
if a>b:
    small=b
else:
    small=a
for i in range(1,small+1):
    if(a%i==0 and b%i==0):
        hcf=i
print(hcf)

a=int(input("Enter number: "))
b=int(input("Enter number: "))
if a>b:
    big=a
else:
    big=b
while True:
    if(big%a==0 and big%b==0):
        lcm=big
        break
    big+=1
print(lcm)

#print("lcm= ",((a*b)//hcf))

### write a python program to get marks from user upto user enterred stop after getting marks display sum, avg, highest, and lowest marks 
# NOTE: if marks >100 asks user to enter marks again
c=0

sum=0
while True:
    n=(input("enter number: "))
    if n=="stop":
        break
    elif (int(n)>100):
        n=int(input("enter valid number"))
    n=int(n)
    c+=1
    if c==1:
        min1=n
        max1=n
    sum+=n
    if n>max1:
        max1=n
    if n<min1:
        min1=n
        
    
print("sum of marks: ",sum) 
print("avg of marks= ",(sum/c))
print("min no.= ",min1)
print("max no.= ",max1)

#write a python program for piggy bank money calculation
d=int(input("Enter number of days: "))
m=1
sun=7
s=d//7
sum=0
for i in range(s):
    for j in range(m,sun+1):
        sum+=j
    m+=1
    sun+=1
for k in range(d%7):
    sum+=m
    m=m+1
print(sum)

#WRITE A PYTHON PROGRAM TO FIND FIRST AND SECOND LOWEST NUMBER
f_1=None
s_1=None
n=0
while True:
    n1=input("Enter number or stop: ")
    if(n1=="stop"):
        break
    n1=int(n1)
    n+=1
    if f_1 is None or n1<f_1:
        s_1=f_1
        f_1=n1
    elif s_1 is None or n1<s_1:
        s_1=n1
if n<2:
    print("enter more number")
else: 
    print(f_1,s_1)