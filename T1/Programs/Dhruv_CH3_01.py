# # Functions
# def add(s):
#     return(s)
# s=input("Enter Your name:")
# print("GM",add(s))

#Fun. with no parameters & no return
def msg():
    s=input("Enter Your name:")
    print("Hello!",s)
msg()

#Fun. with no parameters & with return
def sub():
    s=input("Enter Your name:")
    return (s)
print("Name:",sub())

def sum_sub(a,b):
    s1=a+b
    s2=a-b
    return s1,s2
print(sum_sub(100,20))
x,y=sum_sub(20,30)
print(x) 
print(y)

def calc(a,b):
    m=a*b
    d=a/b
    add=a+b
    sub=a-b
    return m,d,add,sub
t=calc(10,20)
print(t)
print(type(t))
for i in t:
    print(i)

def wish():
    """This is function"""
    print('XYZ')
print(wish.__doc__)

# # Parameters & Arguments

#1.Positional Arguments
def sub(a,b):
    print(a-b)
sub(10,20)
sub(20,10)

#2.Keyword Arguments
def wish(name,msg): 
    print('Hello',name,msg)
wish(name='Raj',msg='GM')
wish(msg='GM',name='Raj')
wish('Arya','GM')
wish('Arya',msg='GM') #positional argument pachi Keyword argument chale
#wish(name='Arya','GM') #but Keyword argument pachi positional argument naa chale

#3.Default Argument
def wish(name='Guest'):
    print('Hello',name)
wish()
wish("Arya")

#4.Variable length Argument
def sum(*n):
    total=0
    print(type(n))
    for i in n:
        total+=i
    print(total)
sum(10)
sum(10,20,30)
sum(1,2,3,4,5)

def f1(n1,*s): #n1 is Positional argument & s is variable length argument
    #f1(*s,n1) this gives error because n1 would be never defined 
    #n1=int s=tuple
    print(n1)
    print(s)
    for i in s:
        print(i)
f1(10)
f1(10,20,30) #10 will consider as int parameter and 20,30 are considered as tuples
f1(1,2,3,4,5,6) #1 will consider as int parameter and remains will consider as tuples

#5.Variable length argument with **
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,'=',v)
display(m1=100,m2=200,m3=300)

# # Types of variables

a=10 #Global
def f1():
    print(a)
def f2():
    print(a)
f1()
f2()
def f1():
    a=20
    print(a)
f1()
f2()

a="Banko"
def myfun():
    global a
    a='fantastic'
myfun()
print("My friend is",a)

# # Recursive Function

def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
n=5
fact(n)

# # Nested Function

def f():
    def g():
        print("Inside")
    g()
    print("Outside")
f()


def g(x):
    def h():
        x="abc"
    x=x+1
    print("in g func x is",x)
    h()
    return x
x=3
z=g(x)
print(z)

#WAP to check whether the entered number is armstrong numbert or not
# WAP to check Armstrong Number
def armstrong(n):
    temp=n
    n1=n
    c=0
    sum1=0
    while n1!=0:
        d=n1%10
        c+=1
        n1//=10
    print(c)
    while n!=0:
        d1=n%10
        sum1= sum1 + (d1**c)
        n//=10 
    if sum1==temp:
        print("Armstrong Number!")
    else:
        print("Not Armstrong number!")
n=int(input("Enter a Number:"))
armstrong(n)