l=[1,13,2,3,4]
s=0
i=0

while i<len(l):
    if l[i]==13:
        i+=2
    else:
        s=s+l[i]
        i+=1
print(s)

#Method-I
n=int(input("Enter Size of List:"))
l=[]
for i in range(n):
    l.append(int(input("Enter Element:")))
print("Original List:",l)

for i in range(1,n):
    if i%2==1:
        target_index=n-1
    else:
        target_index=i
    val=l[target_index]
    if target_index>i:
        for j in range(target_index, i, -1):
            l[j] = l[j-1]
        l[i] = val

print("New List:",l)

#Method-II
n=int(input("Enter Size of List:"))
l=[]
for i in range(n):
    l.append(int(input("Enter Element:")))
print("Original List:",l)

left=1
right=n-1
while left<right:
    temp=l[right]

    for j in range(right,left,-1):
        l[j]=l[j-1]
    l[left]=temp
    left=left+2
    right=right-1
print("New list:",l)

#Method-III
l=[2,4,6,8,10]

for i in range(1,len(l)):
    if i%2!=0:
        a=l.pop()
        l.insert(i,a)
print(l)

# 
""" A company has decided to give gift to each employee. A company has given rank to each employee.
    rules for giving gift are:
    I.each employee must recieve atleast 1 gift.
    II.employee having higher ranking gets grater no og gifts than neighbours.
    WPP to find min. no. of gifts as per employee rank.
    eg.if there are 5 employees and rank of employees are
        i. [1,2,1,5,1] ---> min. no. of gifts required 7
        ii. [1,2,3,2,1] ---> min. no. of gifts required 9
"""
n=int(input("Enter no. if employees:"))
l=[]
for i in range(n):
    l.append(int(input("Enter rank of employee "+str(i+1)+":")))
print("Original List:",l)

# Rule 1: Each employee must receive at least 1 gift
gifts = [1] * n
    
# Rule 2 (Left Neighbour): Scan from left to right
for i in range(1, n):
    if l[i] > l[i - 1]:
        gifts[i] = gifts[i - 1] + 1
            
# Rule 2 (Right Neighbour): Scan from right to left
for i in range(n - 2, -1, -1):
    if l[i] > l[i + 1]:
        # Keep the maximum to satisfy both left and right neighbour conditions
        gifts[i] = max(gifts[i], gifts[i + 1] + 1)
        
print("Min. required gifts: ",sum(gifts))

#
""" 
M=1000 CM=900 D=500 CD=400 C=100 XC=90
L=50 XL=40 X=10 IX=9 V=5 IV=4 I=1
hint: make list of this all
"""
n=int(input("Enter Number:"))
val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbol=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
Roman=""
i=0
while n>0:
    for j in range(n//val[i]):
        Roman+=symbol[i]
        n-=val[i]
    i+=1
print("Roman No.:",Roman)

#Method-I
roman = input("Enter Roman Number:")
val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

i = 0
num = 0
while len(roman) > 0:
    # Check if the current Roman string starts with symbol[i]
    while roman.startswith(symbol[i]):
        num += val[i]
        roman = roman[len(symbol[i]):]   # remove matched part
    i += 1

print("Integer No.:", num)

#Method-II
s=input("Enter roman")
val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbol=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
n=0
i=0
while i<len(s):
    if i+1<len(s) and s[i:i+2] in symbol:
        a=symbol.index(s[i:i+2])
        n+=val[a]
        i+=2
    else:
        b=symbol.index(s[i:i+1])
        n+=val[b]
print(n)
        

def analyze_string(user_input):
    vowels = set("aeiouAEIOU")
    
    # 1) Reverse each word but keep word order
    reversed_words = " ".join([word[::-1] for word in user_input.split()])
    print("1) String with each word reversed:")
    print(reversed_words)

    # 2) Dictionary with word lengths
    word_lengths = {word: len(word) for word in user_input.split()}
    print("\n2) Dictionary with word lengths:")
    print(word_lengths)

    # 3) Words with at least 3 vowels
    words_with_vowels = [word for word in user_input.split() if sum(1 for ch in word if ch in vowels) >= 3]
    print("\n3) Words containing at least 3 vowels:")
    print(words_with_vowels)

    # 4) Character categories
    categories = {"vowels": 0, "consonants": 0, "digits": 0, "special": 0}
    for ch in user_input:
        if ch in vowels:
            categories["vowels"] += 1
        elif ch.isalpha():
            categories["consonants"] += 1
        elif ch.isdigit():
            categories["digits"] += 1
        else:
            categories["special"] += 1
    print("\n4) Character categories:")
    print(categories)

    # 5) Category with highest count
    highest_category = max(categories, key=categories.get)
    print("\n5) Category with highest count:")
    print(highest_category)

    # 6) Words with highest number of unique letters (case-insensitive)
    word_unique_counts = {word: len(set(word.lower())) for word in user_input.split()}
    max_unique = max(word_unique_counts.values())
    words_max_unique = [word for word, count in word_unique_counts.items() if count == max_unique]
    print("\n6) Words with the highest number of unique letters:")
    print(words_max_unique)


user_input = input("Enter a string: ")
analyze_string(user_input)

def is_valid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for ch in s:
        if ch in bracket_map.values():  # opening bracket
            stack.append(ch)
        elif ch in bracket_map:  # closing bracket
            if not stack or stack[-1] != bracket_map[ch]:
                return False
            stack.pop()
        else:
            # invalid character (not required here, but safe check)
            return False
    
    return not stack


# Driver code
test_cases = [
    "{[()]}",   # Valid
    "()[]{}",   # Valid
    "[(})",     # Invalid
    "({[}])",   # Invalid
    "({[]]})"   # Invalid
]

for s in test_cases:
    print(f"Input: {s} -> {'Valid' if is_valid(s) else 'Invalid'}")


