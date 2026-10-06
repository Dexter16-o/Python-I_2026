# write a program to calculate electricity bill acc.to following criteria...upto 100 no charge..next 100 unit 5 rs per unit..
#next 200 unit rs 10 per unit
n=int(input("Enter unit:"))
if n<=100 and n>=1:
    print("No charge ")
elif n<=200:
    bill=(n-100)*50
    print("Bill=",bill)
else: 
    bill=(n-200)*10+500
    print("Bill=",bill)

#Write a program to find Area of trapezoid
a=float(input('enter size'))
b=float(input('enter size'))
h=float(input('enter size'))
Area=((a+b)/2)*h
print('AREA OF TRAPEZOID : ',Area)

# Write a program to calculate volume and total area of cylinder...
import math
r= int(input("enter r: "))
h= int(input("enter h: "))
p=math.pi
Volume=p*r*r*h
Area=2*p*r*(h+r)
print('Volume:',Volume)
print('Area',Area)

# Write a program to convert given sec into min, hour , sec.....
s=int(input("enter second: "))
hr=s//3600
min=(s%3600)//60
sec=(s%3600)%60
print(hr,",",min,",",sec)

#Write a program to convert no. of days into year, month and day   1 year=365 days and 1 month =30 days
d=int(input("enter days: "))
yr=d//365
month=(d%365)//30
days=(d%365)%30
print(yr,month,days)

# Currency count 
r=int(input("ENTER RUPEES : "))
a=r//500
b=(r%500)//200
i=((r%500)%200)//100
c=(((r%500)%200)%100)//50
d=((((r%500)%200)%100)%50)//20
e=(((((r%500)%200)%100)%50)%20)//10
f=((((((r%500)%200)%100)%50)%20)%10)//5
g=(((((((r%500)%200)%100)%50)%20)%10)%5)//2
h=((((((((r%500)%200)%100)%50)%20)%10)%5)%2)//1
print("500 Rs. :",a,"200 Rs. :",b,"100 Rs. :",i,"50 Rs. :",c,"20 Rs. :",d,"10 Rs. :",e,"5 Rs. :",f,"2 Rs. :",g,"1 Rs. :",h)

# Write a program to check entered number is even or odd
n=int(input("enter number"))
if n%2==0 :
    print("even")
else :
    print("odd")

# Write a python program to find max number of given 3 number by using if-elif-else method
a=int(input("Enter number: "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))
if (a>b)and(a>c) :
    print("a is greater number")
elif (b>c) :
    print("b is greater number")
else:
    print("c is greater")

# 
n=int(input("Enter number: "))
if n>20 :
    print("number is greater than 20")
    if n>40 :
        print("number is greater than 40")
    else :
        print("number is smaller than 20")
else :
    print("number is smaller than 20")

# write a program to check last digit of any given number is divisible or not
n=int(input("Enter number: "))
temp=n%10 # For last digit
if temp%3==0 :
   print("Divisible by 3:")
else :
  print("not")

# write a program to check middle digit any given 3 digit number is divisible by 3 or 5
n=int(input("Enter 3 digit number: "))
temp=(n//10)%10
if (temp%3==0) or (temp%5==0):
    print("Divisible by 3 and 5")
else:
    print ("not divisible by 3 and 5")

#write a program to check enter year is leap year or not
year=int(input('Enter year :'))
if (year%4==0):
    if ((year%400==0)or(year%100!=0)):
        print ('Leap year')
    else:
        print ('Not a leap year')
else:
    print('Not leap year')

# write a program to check enter alphabet is vowel or consonant
n=input("enter alphabet ")
if n in('a','e','i','o','u','A','E','I','O','U'):
    print("Vowel")
else:
    print("consonant")

#Write a program to take 2 number as a input and choice of operation from user 
#1 for addition 2 for subtraction 3 for multiplication 4 for division 5 for module
# if user is enetring any other choice above then it should invalid
a=int(input("enter number a "))
b=int(input("enter number b: "))
print(" 1 for addition")
print("2 for subtraction")
print("3 for multiplication ")
print("4 for division ")
print("5 for modulo ")

n=int(input("enter alphabet "))
if n==1 :
        print(a+b)
elif n==2 :
        print(a-b)
elif n==3 :
        print(a*b)
elif n==4 :
        print(a/b)
elif n==5 :
        print(a%b)
else:
        print("Invalid")
        

# Find salary 

age=int(input("Enter age : "))
if age>=18 and age<30:
    gender=input("Enter Gender:")
    if gender in("Male",'male'):
        day=int(input("enter day "))
        amount=day*700
        print("Amount=",amount)
    elif gender in("Female",'female'):
        day=int(input("enter day "))
        amount=day*750
        print("Amount=",amount)
    else:
        print("NOT APPROPRIATE GENDER")
elif age>=30 and age<40:
    gender=input("Enter Gender:")
    if gender in("Male",'male'):
        day=int(input("enter day "))
        amount=day*800
        print("Amount=",amount)
    elif gender in("Female",'female'):
        day=int(input("enter day "))
        amount=day*850
        print("Amount=",amount)
    else:
        print("NOT APPROPRIATE GENDER")
else:
    print("Not Appropriate age")
    

s="Welcome"
for i in s:
    print(i)

for i in range(5):
    print(i)

for i in range(1,7):
    print(i)

for i in range(1,8,2):
    print(i)

for i in range(9,4,-1):
    print(i)

for i in range(12,5,-2):
    print(i)

for i in range(-21,-11,3):
    print(i)

x=1
while x<=5:
    print(x)
    x=x+1

    

x=1
while x<=5:
    print(x)
    x=x+1

# ========================================================================
# NESTED FOR LOOP
# ========================================================================

for i in range(3):
    for j in range(3):
        print("i=",i,"j=",j)

# ========================================================================
# BREAK STATEMENT
# ========================================================================

for i in range(10):
    if i==7:
        break
    print(i)

# ========================================================================
# Continuous statement
# ========================================================================

for i in range(10):
    if i==7:
        continue
    print(i)

# pass
for i in range(10):
    if i==7:
        pass
    print(i)

# ========================================================================
# for/else
# ========================================================================

for i in range(1,4):
    print(i)
else:
    print("Hello")

for i in range(5,4):
    print(i)
else:
    print("Hello")

for i in range(1,4):
    print(i)
    break
else:
    print("Hello")

for i in range(10):
    if(i==3):
        break
    print(i)
else:
    print("Hello")

x=1
while x<=5:
    print(x)
    x=x+1
else:
    print("Hello")

x=1
while x<=5:
    if x==2:
        break
    print(x)
    x=x+1
else:
    print("Hello")

# WRITE A python program to check enter number is armstrong no. or not:

a=int(input("ENTER ANY NUMBER: "))
temp=a
count=0
while(temp!=0):
    temp=temp//10
    count+=1
print(count)
a1=a
sum=0
while a1!=0:
    r=a1%10
    sum=sum+(r**count)
    a1=a1//10
if a==sum:
    print(" no.is armstrong number")
else:
    print("not Armstrong number")
    
    

#WAP to find reverse number of any given number
n=int(input("Enter any number: "))
r=0
while(n!=0):
    r=r*10+(n%10)
    n=n//10
print(r)

# WAP to check enter number is perfect number or not....
n=int(input("Enter any number: "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if sum==n:
    print("IT's A PERFECT NUMBER....")
else:
    print("IT's NOT A PERFECT NUMBER....")

# WAP to check entered number is strong no.or not

n=int(input("ENTER ANY NUMBER : "))
temp=n
sum=0
while n!=0:
    r=n%10
    fact=1
    for i in range (1,r+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if(sum==temp):
    print("Strong number....")
else:
    print("Weak number")

#WAP to check enter two number is amicable number or not

a=int(input("ENTER ANY NUMBER : "))
b=int(input("ENTER ANY NUMBER : "))
sum1=0
sum2=0
for i in range(1,a):
    if(a%i==0):
        sum1=sum1+i
for j in range(1,b):
    if(b%j==0):
        sum2=sum2+j
if(a==sum2 and b==sum1):
    print("Amicable number")
else:
    print("Not Amicable number")


