for i in range(5):
    print(i)

for i in range(2,12,2):
    print(i)

for i in range(3,9):
    print(i)

#Gives no output
for i in range(10,1,2):
    print(i)

for i in 'LJIET':
    print(i)

for i in 'LJIET':
    print("hello")

for i in range(-15,-5,2):
    print(i)
    

x=1
while x<=5:
    print(x)
    x+=1

name=''
while name!='SHP':
    name=input('Enter name:')
print("Thank you")

#nested Loop
for i in range(2):
    for j in range(2):
        print("i=",i,"j=",j)

#break
for i in range(1,11):
    if i==7:
        print("Stop Execution!")
        break
    print(i)

#Continue
for i in range(1,11):
    if i%2==0:
        print(i)
    else:
        continue

for i in range(1,11):
    if i%2==0:
        continue
    print(i)

for i in range(1,5):
    print(i)
else:
    print("Hello")

#If loop executes fully , else part will be execute if it's not then else part will not execute
for i in range(1,5):
    if i==2:
        break
    print(i)
else:
    print("Hello")

c=0
while c<1:
    c=c+1
    print(0)
else:
    print("Hello")

c=0
while c<1:
    c=c+1
    print(0)
    break
else:
    print("Hello")

#Gives error 
#for i in range(1,5):
#else:
#    print("Hello")

#Pass
for i in range(1,6):
    pass
else:
    print("Hello")

#WAP to print sum and average of Numbers entered by user.
n=int(input("How many Numbers do you want to enter?:"))
sum=0

for i in range(n):
    num=int(input("Enter a Number:"))
    sum=sum+num
print("Sum:",sum,"| AVG:",sum/n)

#WAP to print multiplication table
n=int(input("Enter a No.:"))

for i in range(1,11):
    print(n,"*",i,"=",n*i)

#WAP to find factorial of enterd number.
n=int(input("Enter a number:"))
f=1

if n<0:
    print("-ve not allowed!")
elif n==0 or n==1:
    print("Factorial:",f)
else:
    for i in range(2,n+1):
        f=f*i
    print("Factorial of",n,":",f)

#WAP to print fibonacci sequence
n=int(input("Enter a number:"))
a=0
b=1

if n<0:
    print("-ve not allowed!")
elif n==1:
    print("Fibonacci series: 1")
else:
    print("Fibonacci Sequence:",end=" ")
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

#WAP to find pelindrome number.
n=int(input("Enter a number:"))
temp=n
d=0
rev_no=0

while n!=0:
    d=n%10
    rev_no=rev_no*10+d
    n=n//10
print("Reversed number:",rev_no)

if temp==rev_no:
    print("Pelindrome!")
else:
    print("Not Pelindrome!")

#WAP to check entered number is strong number or not! ex: 145=> 1!+4!+5! = 145
n=int(input("Enter a number:"))
temp=145
sum=0

while n!=0:
    d=n%10
    f=1
    for i in range(2,d+1):
        f=f*i
    sum=sum+f
    n=n//10

if sum==temp:
    print("Strong Number!")
else:
    print("Not Strong Number!")

# WAP to check Armstrong Number
n=int(input("Enter a Number:"))
temp=n
temp1=n
r=0
num=0

while n!=0:
    r=r+1
    n=n//10
print("Digit:",r)

while temp1!=0:
    d=temp1%10
    num = num + (d**r)
    temp1=temp1//10
    
print(num)
if num==temp:
    print("Armstrong Number!")
else:
    print("Not Armstrong number!")


