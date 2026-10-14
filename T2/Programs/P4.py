l=["lessonplan","lesson","less","length"]
if len(l)==0:
    print("nothing")
if len(l)==1:
    print(l[0])
l.sort()
print(l)

end=min(len(l[0]),len(l[-1]))
print(end)

i=0
while i<end and l[0][i]==l[-1][i]:
    i+=1
    pre=l[0][0:i]
if pre=="":
    print(-1)
else:
    print(pre)

N = int(input("Enter the size of the matrix (N for N x N): "))
m = []

for i in range(N):
    a=[]
    for j in range(N):
        a.append(int(input("Enter element:")))
    m.append(a)    
print("Original matrix:",m)

for i in range(N):
    for j in range(i,N):
        m[i][j],m[j][i]=m[j][i],m[i][j] #Convert row to column
for i in range(N):
    m[i].reverse() #reverse the element of rows
print("Transposed matrix",m)

# mutable, key-value pair, keys must be unique, duplicate values are allowed
dict1={"a":20,"b":30,"c":40}
print(dict1)
print(type(dict1))
d={}  #to create empty dictionary
d1=dict() #to create empty dictionary
d[10]="asd"
d[2]="qwe"
d1["s1"]=10
print(d)
print(d1)

d1={10:"asd",2:"qwe"}
print(d1[2])
# print(d1[20]) if key is not available in dictionary it will return keyerror
d1[30]="zxc"
print(d1)

d={10:"asd",2:"zxc",30:"qwe"}
del d[2]
print(d)
d.clear()
print(d)
# del d --> d is already clear so there is nothing to delete anymore
# print(d)

d={10:"asd",2:"zxc",30:"qwe"}
print(len(d))

d=dict([(10,"asd"),(2,"zxc"),(30,"qwe")])
print(d1)

d={10:"asd",2:"zxc",30:"qwe"}
d2=d
d2[2]="hello"
print(d2)
print(d)

d={10:"asd",2:"zxc",30:"qwe"}
d2=d.copy()
d2[2]="hello"
print(d2)
print(d)

d={10:"asd",2:"zxc",30:"qwe"}
x={"a":10,'b':20}
d.update(x)
print(d)

d={10:"asd",2:"zxc",30:"qwe"}
print(d.get(10))
print(d[10])
print(d.get(10,"hello"))
print(d.get(40,"hello"))
print(d.get(40))
print(d)

d={10:"asd",2:"zxc",30:"qwe"}
print(d.popitem()) #delete and returns last elment as tuple form
print(d)

d={10:"asd",2:"zxc",30:"qwe"}
print(d.keys())
for i in d.keys():
    print(i)

d={10:"asd",2:"zxc",30:"qwe"}
print(d.values())

d={10:"asd",2:"zxc",30:"qwe"}
print(d.items())
for i,j in d.items():   #To access elements of dictionary
    print(i,"-",j)

d={10:"asd",2:"zxc",30:"qwe"}
d.setdefault(40,"hello") #add key to dictionary
print(d)
d.setdefault(30,"poi") # if already key available then it will not change
print(d)

print({x:x**2 for x in range(1,6)})

def count_word_frequency(paragraph):
    # Convert the paragraph to lowercase to make the count case-insensitive
    cleaned_paragraph = paragraph.lower()
    
    # Split the paragraph into individual words based on spaces
    words = cleaned_paragraph.split()
    
    # Initialize an empty dictionary to store frequencies
    freq_dict = {}
    
    # Loop through each word in the list
    for word in words:
        # If the word is already in the dictionary, increment its count
        if word in freq_dict:
            freq_dict[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            freq_dict[word] = 1
            
    return freq_dict

input_string = input("Enter string:")
output = count_word_frequency(input_string)

print("Output:", output)


def group_words_by_first_char(text):
    # Split the sentence into individual words by whitespace
    words = text.split()
    
    result_dict = {}
    
    for word in words:
        # Get the first character of the word
        first_char_key = word[0]
        
        # Append the word to the list corresponding to its first character
        if first_char_key in result_dict:
            result_dict[first_char_key].append(word)
        else:
            result_dict[first_char_key] = [word]    
        
    return result_dict

input_text = "Don’t wait for your feelings to change to take the action. Take the action and your feelings will change"
output_dict = group_words_by_first_char(input_text)

print(output_dict)

 # WAP to convert decimal no. from 0-999 in to word
 # eg. input = 367
 #     output = three hundred sixty seven
def int_to_word(n):
    d={0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    k=1000
    if n<20:
        return d[n]
    if n<100:
        if n%10==0:
            return d[n]
        else:
            return d[(n//10)*10]+" "+d[n%10]
    if n<k:
        if n%100==0:
            return d[n//100]+" hundred "
        else:
            return d[n//100]+" hundred "+int_to_word(n%100)
n=int(input("Enter Number:"))
print(int_to_word(n))
    


