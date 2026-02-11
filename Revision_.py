#1. Conditional Statements (IF, ELSE, ELIF)
#***
# Simple IF: Condition checking only
age = 20
if age >= 18:
    print("Eligible for vote")

# IF-ELSE: Binary choices
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
#***
# ELIF: Multiple conditions (Grades)
marks = 85
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("Fail")

#**
# NESTED IF: Security/ATM logic
pin_correct = True
balance = 1000
if pin_correct:
    if balance > 500:
        print("Withdrawal successful")



#2. Basic Loops & String Manipulation        

# Print characters in a string
s = 'Python'
for i in s:
    print(i)

# Count length without len()
t = (1, 2, 3, 4)
count = 0
for i in t:
    count += 1

# Manual String Reversal
s = 'Good Morning'
out = ''
for i in s:
    out = i + out  # Adds character to the front


#3.Range & Filtering Collections

# Even numbers in a range
for i in range(0, 101, 2):
    print(i)

# Extract only integers from a mixed list
l = [10, 2.5, '30', 50]
for i in l:
    if type(i) == int:
        print(i)

# Remove duplicates from a list
l = [10, 20, 10, 30, 20]
out = []
for i in l:
    if i not in out:
        out.append(i)


#4. Dictionary & Data Mapping


# Word length mapping
s = 'Good Students'.split()
out = {i: len(i) for i in s} # {'Good': 4, 'Students': 8}

# Character frequency count
s = 'abacbaacc'
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1

# Vowel position mapping
s = 'apple'
vowels = {}
for i in range(len(s)):
    if s[i] in 'aeiou':
        vowels[s[i]] = i



#5.Advanced Extraction & Nested Loop

# Deep integer extraction (including nested lists/tuples)
l = [10, [100, 200], (6, 'hi')]
out = []
for i in l:
    if type(i) == int:
        out.append(i)
    elif type(i) in (list, tuple):
        for j in i:
            if type(j) == int:
                out.append(j)

# Extracting only lowercase with Even ASCII
s = "Python"
for char in s:
    if char.islower() and ord(char) % 2 == 0:
        print(char)


#6. Value Replacement & Binary Logic

# Replace space with '*'
s = "Always smile"
print(s.replace(" ", "*"))

# Binary Inverter (Flip 0 to 1 and 1 to 0)
input_bin = '0110'
output_bin = ''
for bit in input_bin:
    output_bin += '1' if bit == '0' else '0'


#*imp: Categorize Characters (Upper, Lower, Digit, Special)
s = 'Ha6753jkuds@hsdy'
lower, upper, digit, spec = '', '', '', ''

for char in s:
    if char.islower():
        lower += char
    elif char.isupper():
        upper += char
    elif char.isdigit():
        digit += char
    else:
        spec += char

print(f"Lower: {lower}\nUpper: {upper}\nDigits: {digit}\nSpecial: {spec}")

# *imp: Extract Nested Odd Numbers

l = [5.5, 2j, 10, [77, 65], (6, 'hi'), 'good']
out = []

for i in l:
    # Check main list
    if type(i) == int and i % 2 != 0:
        out.append(i)
    # Check nested list or tuple
    elif type(i) in (list, tuple):
        for j in i:
            if type(j) == int and j % 2 != 0:
                out.append(j)

print(out) # [77, 65]


#*imp: Extract Nested Even Numbers
l = [5.5, 2j, 10, [77, 65], (6, 'hi'), 'good']
out = []

for i in l:
    if type(i) == int and i % 2 == 0:
        out.append(i)
    elif type(i) in (list, tuple):
        for j in i:
            if type(j) == int and j % 2 == 0:
                out.append(j)

print(out) # [10, 6]



#*imp: Extract Strings if Palindrome
l = ['level', 'hello', 'radar', 'python', 'madam']
out = []
for i in l:
    if type(i) == str and i == i[::-1]:
        out.append(i)
print(out) # ['level', 'radar', 'madam']


#*imp: Square of all Integers in a List
l = [2, 'hi', 5, 10.5, 8]
for i in l:
    if type(i) == int:
        print(i**2) # Output: 4, 25, 64


