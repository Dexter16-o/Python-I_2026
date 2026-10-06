print("Hello")

Abc=100
print(Abc)
a123=10

print(print('abc'))
print(bool(''))
print(bool(0))
print(bool(0.0))
print(bool(12))
print(bool('abc'))
print(bool(12.25))

#Python Operators
#1.Arithmetic Operators: +,-,*,/,//,%,**
a=12
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)  #division but only returns float number
print(a//b) #division but returns only integer number
print(a%b)
print(a**b) #Exponent a^b

print(True*False)

#print(True/False) gives error Zero division Error
print(False/True)

#2.Relational Operators: >,<,>=,<=,==,!=
print(10>0)
print(10<0)
print(True<False)
print(True==False)
print(True>False)
print(10>=10)
print(10<=5)
print(10!=10)
print(10==10.0)
print(10<20<30)
print(10>20<30)
print('ab'=='ab')
print('AB'=='ab')
print(10>True)
print(0>False)

#3.Logical Operators: and,or,not
#and: if both true -> true
#or: if both false -> false
#not: invert

print(False and True)
print(False and False)
print(True and True)
print(True and False)
print(True or True)
print(False or True)
print(True or False)
print(False or False)
print("1",10 and 20)
print("2",0 and 20)
print("3",20 and 0)
print("4",10 or 20)
print("5",0 or 10)
print("6",10 or 0)
print("7",not 20)
print("8",not 0)
print("9",'ab' or 'cd')
print("10",'' and 'cd')
print("11",'ab' or ' ')

#4.Conditional(Ternary) operators
a,b=10,20
x=30 if a>b else 40 
print(x)

#5.Membership Operators: in,not in 
print('a' in 'abc')
print('a' not in 'Abc')

#6.Assignment Operators: +=,-+,*=,/=,//=,**=,%=
x=10
x+=20
#print(x+=20) gives error
print(x)
x*=2;
print(x)
x-=10
print(x)
x/=2
print(x)
x//=5
print(x)
x**=2
print(x)
x%=2
print(x)

#7.Bitwise Operators: &,|,^,~,<<,>>   [Not in Syllabus]
print(4 & 5)
print(4 | 5)
print(4 ^ 5)

#ord() : Character to ASCII value
#chr() : ASCII to Character Value
#a-z : 97-122
#A-Z : 65-90
print(ord('A'))
print(ord('a'))
print(chr(83))
print(chr(100))

#Math Module
import math
print(math.pi)
print(math.e)
print(math.tau)

###### Operator Precedence MIMP
#1.() parenthesis
#2.** Right to Left
#3.*,/,%,// (Left to right)
#4.+-
#5.>,<,>=,<=,==,!=
#6.+=,-=,*=,/=,//=
#7.in,not in
#8.not
#9.and
#10.or
a,b,c,d=30,20,10,5
print((a+b)*c/d)
print((a+b)*(c/d))
print(a+(b*c)/d)
print(5==5.0 or 10 and 5 or 5==5.0 and 7!=7.0)
print(10*4+5**2**2/10)

print(7 and 0 or 5 and 3 or 7/0)
##print(5 and False or 3/0) Gives error 
print(5 and True or 3/0)
print(7*5**2/True * False)
print('1' in '123' and 'False' or True) #Returns False as String because of 'False' or True
new=((1 and 'True') and ('False' or "Train"))
str="This statement is"+new
print("This is False" if "False" in new else "This is True")

bool(None)

a=5
p=7
a+=p
a-=p
p*=a
p/=a
print(p)
print(a)

print(10/(1*3/6))

print(3**1**3/True)

a=4
b=6
c=3
print(a+b*c/a-b)
print(2**(3**2))
print((2**3)**2)
print(2**3**2)
print(int(43.55+4/6))
x=0.0
y=48>0
z=11<7
print(not(float(x or y or z)))
print(int(6==6.0)*3+4%5)
print(int('6'==6.0)*3+4%5)
print(bool(2+9*((3*12)-8)/10))

#WAP to find Area of circle.get user input for Radius of Circle.
import math
r=int(input("enter radius="))
Area = math.pi*r**2
print(Area)

#WAP to get Seconds from the user and convert it into hr:min:sec format
s=int(input("Enter Seconds:"))
hr=s//3600
mi=(s%3600)//60
sec=((s%3600)//60)%60
print("Time=",hr,":",mi,":",sec)
##ALternate Method
#s=int(input("Enter Seconds:"))
#hr=s//3600
#s=s%3600
#mi=s//60
#s=s%60


