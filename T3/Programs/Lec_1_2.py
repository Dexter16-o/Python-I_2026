# Converted from Lec_1_2.ipynb

# File open syntax:
# f=open("filename.txt","mode")
read---r
write---w
append---a

# # Write Mode---w

# To create a new file , to write data in to text file ,
# it will overwrite data when you open it again in write mode
f=open("abc.txt","w")
# write() , writelines() : to write content in file
f.write("Hello\n")
f.write("Division d1\n")
f.writelines(["Mon\n","Tue\n","Wed\n","Thu\n","Fri\n","Sat\n","Sun"]) #It is used to write multiple lines
# writelines() can take input as string,list,tuple etc.
f.close()
# f.write("Hello") it will return error because we can't write anything after close the file

# # Read Mode---r

# To read data, if file is not available then it will return file doesn't found error
# it is a default mode, it will start reading from 0 position while you open file 
f=open("abc.txt") # read is default so we don't have to write "r" for it
a=f.read() # it will read all text of file
print(a)
f.close()

f=open("abc.txt")
a=f.read(5) # It will read 5 chars from file
print(a)
f.close()

f=open("abc.txt")
a=f.read(15) # It will read 15 chars from file & \n is count as 1 char also.
print(a)
f.close()

f=open("abc.txt")
a=f.readline() # It will read line from file
print(a)
a1=f.readline()
print(a1)
f.close()

f=open("abc.txt")
a=f.readline(50) # It will read all chars of line , even if input 50 is greater although it only reads that one line only
print(a)
f.close()

f=open("abc.txt")
a=f.readline(3) # It will read all chars of line , even if input 50 is greater although it only reads that one line only
print(a)
a1=f.readline()
print(a1)
f.close()

f=open("abc.txt")
a=f.readlines() # it will read all lines of file and return in list
print(a)
f.close()

f=open("abc.txt")
a=f.readlines(14) # it will read upto input number of character and will not break that line
print(a)
f.close()

# # Append Mode---a

# It will add data in existing file , if file is not available then it will create new file
f=open("abc.txt","a")
f.write("hey!")
f.close()

# # r+ , w+ , a+ , x

f=open("abc.txt","w+")
f.write("Hello\n123\n")
a=f.read()
print(a)
f.close()

f=open("abc.txt","r+")
a=f.read()
print(a)
f.write("Hello\n123")
f.close()

f=open("abc.txt","a+")
a=f.read()
print(a)
f.write("\nHello")
f.close()

f=open("abc.txt")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)

with open ("abc.txt","r") as f1:
    a=f1.read()
    print(a) # here file will close automatically when we leave the indentation
print(f1.closed)

f=open("abc.txt","a+")
print(f.tell()) # tell() return position of pointer
a=f.read()
print(a)
f.seek(0) # move pointer on perticular position
print(f.tell())
# f.write("Hello\n123\n")
f.close()

# WAP to write days in days.txt file (su,mon,...)
f=open("days.txt","w")
f.writelines(["Sun\n","Mon\n","Tue\n","Wed\n","Thu\n","Fri\n","Sat\n"])
f.close()

# WAP to count lines of days.txt file
f=open("days.txt")
print("No. of lines=",len(f.readlines()))

# WAP using user defined function to get age of user & write it in to file 
def cust():
    name=input("Enter Name: ")
    age=int(input("Enter Age: "))
    data=str([name,age])
    f=open("cust.txt","a")
    f.write(data+"\n")
    f.close()
cust()

# WAP to print odd lines of days.txt file
f=open("days.txt")
a=f.readlines()
s=a[::2]
for i in s:
    print(i)

# WAP to count words, characters , space from text file
# content of text file is "Frineds are crazy, Friends are naughty"
sp=0
ch=0
w=0
f=open("sample.txt","w")
f.write("Friends are crazy, Friends are naughty")
f.close()
f1=open("Sample.txt")
a=f1.read()
for i in a:
    ch+=1
    if i==" ":
        sp+=1
    # If given content is multiline then we must use this also:
    # if i==" " or i=="\n":  
    #     w+=1          
print("No. of ch=",ch-sp)
print("No. of space=",sp)
print("No. of Words=",sp+1)
