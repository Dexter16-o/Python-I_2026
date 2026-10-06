def encrypt():#to put all our code in function
    strings=input('what is your message: ')
    even=strings[::2]#extract the even part 
    odd=strings[1::2]#extract the odd part
    print(even+odd)#print the result
encrypt() 

def decrypt():
    string=input('what is your message: ')
    length=len(string)#to get the length of the input
    half_length=(length+1)//2 #half of the input
    even=string[:half_length]#even part
    odd=string[half_length:]#odd part
#here we start inserting each of the part to form original
    msg=''
    for i in range (half_length):
        join=even[i:i+1]+odd[i:i+1]
        msg=msg+join
    print(msg)
decrypt()
for i in range(97,123):
    for j in range(i,123):
        print(chr(j),end="")
    for k in range(97,i):
        print(chr(k),end="")
    print()
s=input()
s1=""
key=int(input())
for i in range(key):
    s1+=s[i::key]
print(s1)
string=input('what is your message: ')
key=int(input())
length=len(string)#to get the length of the input
part=length//key #half of the input
extra=length%key #extra characters after dividing string in equal parts
l=[]
for i in range(key):
    if i<extra:
        s1=string[(part+1)*i:(part+1) * (i+1)]
        l.append(s1)
    else:
        s1=string[(part*i)+extra:(part*(i+1))+extra]
        l.append(s1)  
msg=""
for i in range(part+1):
    for j in range(len(l)):
        msg+=l[j][i:i+1]
print(msg)
def mayan(n):
    L=[chr(i) for i in range(65,85)]
    s=""
    while n!=0:
        r=n%20
        s+=L[r]
        n//=20
    print(s[::-1])
n=int(input())
mayan(n)
i=1
while True:
    temp=i
    x=str(i)
    y=x[1:]+x[0]
    if int(y)/temp==3.5:
        print(temp)
        break
    i+=1
L=[1,2,3,1,2,1,5,6,3,4,5]
S=set(L)
L1=list(S)
print(L1)
a=[['A',34],['B',21],['C',26]]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j][1]>a[j+1][1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
 
print(a)
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)
def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print( "Sum is:",sum1([[1,2,[1,2]],[3,4]]))

