# 1. Q: WAP to count the frequency of each character in a string using a dictionary.
s = 'pappu'
res = {}
for char in s:
    if char in res:
        res[char] += 1
    else:
        res[char] = 1
print(res) 
# Output: {'p': 3, 'a': 1, 'u': 1}

# 2. Q: WAP to separate integers and strings from a mixed list into two different lists.
data = [10, 'hi', 20, 'bye', 30]
int_list = []
str_list = []
for item in data:
    if type(item) == int:
        int_list.append(item)
    else:
        str_list.append(item)
print(int_list, str_list)
# Output: [10, 20, 30] ['hi', 'bye']

# 3. Q: WAP to count the number of Uppercase, Lowercase, and Digits in a given string.
s = 'Doc_ID_101'
u, l, d = 0, 0, 0
for char in s:
    if char.isupper(): u += 1
    elif char.islower(): l += 1
    elif char.isdigit(): d += 1
print(f"U:{u}, L:{l}, D:{d}")
# Output: U:4, L:2, D:3

# 4. Q: WAP to check if a string is a palindrome without using the slicing [::-1] method.
s = 'radar'
rev = ''
for i in range(len(s)-1, -1, -1):
    rev += s[i]
if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
# Output: Palindrome

# 5. Q: WAP to create a dictionary where keys are vowels and values are their index positions.
s = 'medical'
vowels = 'aeiou'
res = {}
for i in range(len(s)):
    if s[i] in vowels:
        res[s[i]] = i
print(res)
# Output: {'e': 1, 'i': 3, 'a': 5}

# 6. Q: WAP to flip a binary string (change '1' to '0' and '0' to '1').
s = '10110'
out = ''
for bit in s:
    if bit == '1': out += '0'
    else: out += '1'
print(out)
# Output: 01001

# 7. Q: WAP to find the length of the longest word in a space-separated string.
s = 'Python is very easy'
words = s.split()
longest = 0
for w in words:
    if len(w) > longest:
        longest = len(w)
print(longest)
# Output: 6
