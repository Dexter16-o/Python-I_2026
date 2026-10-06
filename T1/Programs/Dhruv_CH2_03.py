#Pattern
n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ") 
        #if we take i instead of "*" it prints 1,22,333,4444,55555
        #if we take j instead of "*" it prints 1,12,123,1234,12345
    print()

n=int(input("Enter no of rows:"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()

n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(i,n+1):
        print("*",end=" ")
    print(" ")

n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(i,n+1):
        print("*",end=" ")
    print(" ")

n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print(" ")

n=int(input("Enter no of rows:"))
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print("",end=" ")
    for k in range(i,0,-1):
        print("*",end=" ")
    print(" ")

n=int(input("Enter no of rows:"))
a=65
g=1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("",end=" ")
    for k in range(1,i+1):
        if i%2==1:
            print(chr(a),end=" ")
            a+=1
        else:
            print(g,end=" ")
            g=g+1
    print(" ")

n=int(input("Enter no of rows:"))
a=97
g=1
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print("",end=" ")
    for k in range(i,0,-1):
        if i%2==0:
            print(g,end=" ")
            g+=1
        else:
            print(chr(a),end=" ")
            a+=1
    print(" ")

n=int(input("Enter no of rows:"))
a=65
g=1
for i in range(1,n+1):
    a=65
    g=1
    for j in range(1,n-i+1):
        print("",end=" ")
    for k in range(1,i+1):
        if i%2==1:
            print(chr(a),end=" ")
            a+=1
        else:
            print(g,end=" ")
            g=g+1
    print(" ")

n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print(" ")
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print("",end=" ")
    for k in range(i,0,-1):
        print("*",end=" ")
    print(" ")

# ========================================================================
# # LCM & HCF
# ========================================================================

#WAP to find LCM & HCF of two integers number
a=int(input("Enter Number1:"))
b=int(input("Enter Number2:"))
f=0

if a>b:
    small=b
else:
    small=a

for i in range(1,small+1):
    if a%i==0 and b%i==0:
        hcf=i
print("HCF of numbers:",hcf)

if a>b:
    Big=a
else:
    Big=b

while True:
    if (Big%a==0) and (Big%b==0):
        lcm=Big
        break
    Big+=1
print("LCM of numbers:",lcm)

print("LCM of Numbers:",((a*b)//hcf))

#WAP to get marks from user upto user enter stop, after getting marks display sum,average,highest & Lowest
#if marks greater than 100 then ask user to enter marks again
sum=0
n=0
c=0
while True:
    marks=input("Enter marks or if done then enter 'STOP':")
    if(marks=="STOP"):
        break
    elif (int(marks)>100):
        print("Enter Valid Marks 0-100")
        continue
    c+=1
    if c==1:
        min1=int(marks)
        max1=int(marks)
    sum=sum+int(marks)
    if int(marks)>max1:
        max1=int(marks)
    if int(marks)<min1:
        min1=int(marks)
avg=sum/c

print("Sum:",sum,"| AVG:",avg,"| Min:",min1,"| Max:",max1)

#WAP to for piggy bank money calculation
days=int(input("Enter no of days:"))
m=1
w=days//7
sun=7
sum1=0
for i in range(w):
    for j in range(m,sun+1):
        sum1+=j
    m+=1
    sun+=1
for k in range(days%7):
    sum1+=m
    m+=1
print("Money:",sum1)

#WAP to find first and second lowest number
f_l=None
s_l=None
n=0
while True:
    n1=input("Enter a Number or if done then enter 'STOP':")
    if(n1=="STOP"):
        break
    n1=int(n1)
    n+=1 
    if f_l is None or n1<f_l:
        s_l=f_l
        f_l=n1
    elif s_l is None or n1<s_l:
        s_l=n1
if n<2:
    print("Enter more no")
else:
    print(f_l,s_l)


