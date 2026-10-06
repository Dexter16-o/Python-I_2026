#WAP to check enter number is disarium number or not:

n=int(input("Enter any number : "))
temp=n
count=0
while(n!=0):
    n=n//10
    count+=1
# print(count)
n=temp
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**count)
    count=count-1
    n=n//10
if temp==sum:
    print(" no.is disarium number")
else:
    print("not Disarium number")
    

for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,5,1):
    for j in range(i):
        print(i,end=" ")
    print()

for i in range(1,5,1):
    for j in range(i,i+1):
        print(j,end=" ")
    print()

#WAP TO ENTER NUMBER IS HAPPY NUMBER OR NOT

n=int(input("Enter any number:"))
while n!=1 and n!=4:
    sum=0
    while n>0:
        r=n%10
        sum=sum+r*r
        n=n//10
    n=sum
if n==1:
    print("----HAPPY-----")
else :
    print("---Not Happy----")

    

for i in range(1,6,1):
    for j in range(i):
        print(j,end=" ")
    print()

#WAP to read number n and compute 
n=input("Enter any number: ")
a=int(n)
b=int(n+n)
c=int(n+n+n)
sum=a+b+c
print("SUM:",sum)

#WAP to check entered number is prime number or not:
n=int(input("Enter any number:"))
count=0
for i in range(2,n):
    if n%i==0:
        count=1
        break
if count==0:
    print("Prime number")
else:
    print("Not Prime number")

#WAP to read date from user and print date of next day:
date=int(input("ENTER DATE :"))
month=int(input("ENTER MONTH :"))
year=int(input("ENTER YEAR :"))

if month==12 and date==31:
    month=1
    date=1
    year=year+1
elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10)and date==31:
    month=month+1
    date=1
elif (month==4 or month==6 or month==9 or month==11)and date==30:
    month=month+1
    date=1
elif month==2 and (date==28 or date==29):
    if (year%4==0)and((year%400==0)or(year%100!=0)):
        if date==28:
            date=date+1
        else:
            date=1
            month=month+1
    elif date==29:
        date=date+1
    else :
        date=1
        month=month+1
else:
    date=date+1

if 1<=date<=31 and 1<=month<=12 and month!=2:
    print(date,"/",month,"/",year)
elif month==2 and 1<=date<=29:
    print(date,"/",month,"/",year)
else:
    print("Incorrect date")


