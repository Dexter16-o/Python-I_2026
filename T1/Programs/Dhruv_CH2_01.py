if 10>5:
    print("10 is big no.")
else:
    print("10 is small no.")

marks=int(input('Enter marks:'))

if marks>=0 and marks<=100:
    if marks>=80 and marks<=100:
        print("Grade A")
    elif marks<80 and marks>=60:
        print("Grade B")
    elif marks<60 and marks>=35:
        print("Grade C")
    else:
        print("Fail")
else:
    print("Invalid Input Marks!")

X=14

if X>10:
    print("X is above 10")
    if X>20:
        print("X is also above 20")
    else:
        print("X is not above 20")
else:
    print("X is below 10")
print("Hello")

#WAP to get 3 different integer number from the use and display the maximum number.
n1=int(input("Enter Number1:"))
n2=int(input("Enter Number2:"))
n3=int(input("Enter Number3:"))

if n1>n2 and n1>n3:
    print("n1 is max")
elif n2>n3 and n2>n1:
    print("n2 is max")
else:
    print("n3 is max")

#WAP to check entered year is leap year or not.
year=int(input("Enter Year:"))

if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"is Leap year")
else:
    print(year,"is not Leap year")

#WAP to arrange 3 different numbers in ascending and descending order
n1=int(input("Enter Number1:"))
n2=int(input("Enter Number2:"))
n3=int(input("Enter Number3:"))

if n1>n2 and n1>n3:
    if n2>n3:
        x,y,z=n3,n2,n1
    else:
       x,y,z=n2,n3,n1
elif n2>n1 and n2>n3:
    if n1>n3:
        x,y,z=n3,n1,n2
    else:
        x,y,z=n1,n3,n2
elif n3>n1 and n3>n2:
    if n1>n2:
        x,y,z=n2,n1,n3
    else:
        x,y,z=n1,n2,n3
else:
    print("Valid No.")

print("Ascending order:",x,y,z)
print("Descending order:",z,y,x)

#WAP to get two different numbers from the user and perform arithmetic operation(+,-,*,/,//,%) as per the entered by the user.

n1=int(input("Enter Number1:"))
n2=int(input("Enter Number2:"))

operation=input("Enter Operation sign:")

if operation=="+":
    print("Addition of two nos:",n1+n2)
elif operation=="-":
    print("Substartion of two nos:",n1-n2)
elif operation=="*":
    print("Multiplication of two nos:",n1*n2)
elif operation=="/":
    print("Division of two nos:",n1/n2)
elif operation=="//":
    print("Floar division of two nos:",n1//n2)
elif operation=="%":
    print("Remainder of division of two number:",n1%n2)
else:
    print("Enter Valid Operation!")

#Electricity bill calculation

u=int(input("Enter Units:"))
cost1=0

if u<=100:
    cost=0
elif u>100 and u<=200:
    cost= (u-100)*5
elif u>200:
    cost= (100*5) + ((u-200)*10)
    
print("Cost:",cost)

#WAP to check whether the entered date by user is valid or not if the entered date is valid then print the date of next day

d=int(input("Enter a day:"))
m=int(input("Enter a month:"))
y=int(input("Enter a year:"))

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    max1=31
elif m==4 or m==6 or m==9 or m==11:
    max1=30
elif y%4==0 and y%100!=0 or y%400==0:
    max1=29
else:
    max1=28

if m<1 or m>13:
    print("Date is invalid!")
elif d<1 or d>max1:
    print("Date is Invalid!")
elif y<1000 or y>=10000:
    print("Date is Invalid!")
elif d==max1 and m!=12:
    d=1
    m=m+1
    print("Next Date:",d,"-",m,"-",y)  
elif d==max1 and m==12:
    d=1
    m=1
    y=y+1
    print("Next Date:",d,"-",m,"-",y)  
else:
    d=d+1 
    print("Next Date:",d,"-",m,"-",y)  

#WAP to ask user for an hour between 1 and 12 , again ask to enter AM and PM , and ask how many hours into the future he wants
#to go ahead print out what the hour will be that many hours into the future . print with Am or PM
# h=int(input("Enter Hour:"))
# am_or_pm=input("Enter AM or PM:")

# how_hr_go_ahead=int(input("How many hours do you want to go ahead?:"))

# if hr%12==0:

