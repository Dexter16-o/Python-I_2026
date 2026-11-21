# Converted from Lec_3_4.ipynb

f1=open("a1.txt")
f2=open("a2.txt")
a1=f1.readlines()
a2=f2.readlines()
m=max(len(a1),len(a2))
f3=open("a3.txt","w")
for i in range(m):
    if i<len(a1):
        f3.write(a1[i])
    if i<len(a2):
        f3.write(a2[i])
f1.close()
f2.close()
f3.close()
f4=open("a3.txt")
a4=f4.read()
print(a4)
f4.close()

# # PB 480 --> Write a “pager” program. Your solution should prompt for a filename, and display the text file 25 lines at a time, pausing each time to ask the user to enter the word “continue”, in order to show the next 25 lines or enter the word “stop” to close the file.

f=open(input("Enter File Name:"))
for i,j in enumerate(f):
    if i%25==0 and i:
        x=input("Enter y to continue and q to quit:")
        if x=="q":
            print("Thank you!")
            break
    else:
        print(j)

# # Q485 --> File Filtering. write all lines of a file1, except those that start with a pound sign ( # ), the comment character for Python to file2. And display data of file2.

f1=open("F1.txt")
f2=open("f2.txt","w")
while True:
    b=f1.readline()
    if len(b)!=0:
        if b[0]=="#":
            continue
        else:
            if "#" in b:
                for i in range(1,len(b)):
                    if b[i]=="#":
                        f2.write(b[0:i])
            else:
                f2.write(b)
    else:
        break
f1.close()
f2.close()
f3=open("f2.txt")
print(f3.read())

# # Q481 --> Write a Python program to reverse the content of a one file and store it in second file and also convert content of second file into uppercase and store it in third file and also count number of Vowels in third file and also print only 2nd line from the content of third file.

# Method-I
f1 = open("file1.txt", "r")
data1 = f1.read()
f1.close()

reversed_data = data1[::-1]

f2 = open("file2.txt", "w")
f2.write(reversed_data)
f2.close()

print("Output 1:")
print(reversed_data)

f2 = open("file2.txt", "r")
data2 = f2.read()
f2.close()

upper_data = data2.upper()

f3 = open("file3.txt", "w")
f3.write(upper_data)
f3.close()

print("Output 2:")
print(upper_data)

f3 = open("file3.txt", "r")
data3 = f3.read()
f3.close()

vowels = 0
for ch in data3:
    if ch in "AEIOU":
        vowels += 1

print("Output 3:")
print("Vowels =", vowels)

f3 = open("file3.txt", "r")
lines = f3.readlines()
f3.close()

print("Output 4:")
if len(lines) >= 2:
    print(lines[1].strip())

# # Q483 --> Write a python program to read a text file “Story.txt” and print only word starting with ‘I’ in reverse order.Example: If value in text file is : ‘INDIA IS MY COUNTRY’ Output will be: ‘AIDNI SI MY COUNTRY’

f=open("Story.txt","w")
f.write("INDIA IS MY COUNTRY")
f.close()
f1=open("Story.txt")
a=f1.read()
a1=a.split()
a2=""
for i in a1:
    if i[0]=="i" or i[0]=="I":
        a2=a2+" "+i[::-1]
    else:
        a2=a2+" "+i
print(a2)
