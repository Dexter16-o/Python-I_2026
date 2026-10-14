s=input("Enter String:")
key=int(input("key="))
s1=""

#Encryption
for i in range(key):
    s1+=s[i::key]
print(s1)

#Decryption
length=len(s1)
part=length//key
extra=length%key
part1=s1[:(part+1)*extra]
part2=s1[(part+1)*extra:]
msg=""
for i in range(part+1):
    if i<part:
        msg+=part1[i::part+1]+part2[i::part]
    else:
        msg+=part1[i::part+1]
print("Decrypted msg:",msg)

# list is muatable, ordered and hetrogeneous datatype
l=[1,2,3,4]
print(type(l))
l[0]=5 #We can't assign element like this in String & tuple
print(l)
print(list(range(1,11)))
print(list("Hello"))

print("This is my pen".split())
l1=[]
print(type(l1))
l2=eval(input("Enter List:"))
print(l2)

l3=[1,2.5,"asdf",(1,2,3),["a","b","c"],9,89]
print(l3)
#print(l3[89]) index out of bound error
print(l3[1:-1])
print(l3[-3][-2])
print(l3[2][2])
print(l3[-1:2:-1])
print(l3[-1:15])
print(l3[-1:15:-1])
print(l3)

# Looping with list
l=[10,20,30,40]
for i in l:
    print(i)
for i in range(len(l)):
    print(l[i])
i=0
while i<len(l):
    print(l[i])
    i+=1

l1=[[1,2,3],[4,5,6],[7,8,9]]

for i in l1:
    for j in i:
        print(j,end=" ")
    print()

l=[1,2,3,4]
print(len(l))

l=[1,2,3,4,2]
print(l.count(2))

l=[1,2,3,4,2,2]
print(l.index(2))
#print(l.index(12)) if element not available then gives error

l=[1,2,3,4]
l.append(99)
print(l)
l.append(9)
print(l)

l=[1,2,3,4]
l.insert(3,99)
print(l)
l.insert(0,11)
print(l)
l.insert(-1,10)
print(l)

l=[1,2,3,4]
l.extend(["a","b"])
print(l)
l.extend("hello")
print(l)
l.extend((9,8))
print(l)
#l.extend(9) this gives error because int object is not iterable , only iterable objects like string,tuple,list is allow

l=[1,2,3,4]
l.remove(3)
#l.remove(12) if element is not available then it gives error : not in list

l=[1,2,3,4,5]
l.pop()
print(l)
l.pop(2) # 2 is index no.
print(l)

l=[1,2,3,4]
l.clear()
print(l)

l=[4,3,2]
l.reverse()
print(l)
# print(l.reverse()) - ans will be None
#reverse is operation so it will not be direct printed

l=[11,2,33,4]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
# l=["a",1,"c"] 
# l.sort() - Sorting can not be possible in different datatypes
# print(l)

l=[1,2,3]
print(l*3)
print(l+["a","b"]) #concat
print(min(l))
print(max(l))
print(sum(l))
# print(sum(["a","b"])) #sum is numeric function which can't be applied on string
print([1,2]<[3,8])
print(["dog","cat-1"]<["dog","cat-2"])
print(1 in l)
print(5 not in l)

x=[1,2,3]
y=x
print(id(x))
print(id(y))
y[1]=99
print(x)
print(y)

# clonnig 
# method-1
x=[1,2,3]
y=x[:]
y[0]=99
print(x)
print(y)

# method-2
z=x.copy()
z[1]=100
print(z)
print(x)

print([x*x for x in range(1,6)])
s=[1,2,3,4,5,6]
print([x for x in s if x%2==0])

# WAP to count no of string where string length is 3 or more and 
# first and last chars of string are same.
l=["abc","1231","xyyx","asdf"]
l1=[]
for i in l:
    if len(i)>=3 and i[0]==i[-1]:
        l1.append(i)
print(l1)

l=eval(input("Enter List:"))
print("original list:",l)
c1=0

for i in range(len(l)):
    c=l.copy()
    c.pop(i)
    sum1=sum(c[::2])
    sum2=sum(c[1::2])
    if sum1==sum2:
        print("index to be removed is:",i)
        c1+=1
        print("after removal of index",i,"list is",l[0:i]+l[i+1:])
print("no of special elements=",c1)


