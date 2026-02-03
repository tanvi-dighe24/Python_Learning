# 1. Map String Keys to Specific Values
L = ['hai', 34, 3.4, 'hello', 90, 'byebye']
out1 = {item: item[0] + item[-1] for item in L if type(item) == str}
print(out1)
# Output: {'hai': 'hi', 'hello': 'ho', 'byebye': 'be'}

# 2. Extract Palindromes from a List
L2 = ['madam', 'python', 'level', 'world', 'racecar']
palindromes = [s for s in L2 if s == s[::-1]]
print(palindromes)
# Output: ['madam', 'level', 'racecar']

# 3. Positions of Vowels in a String
s3 = 'apple'
vowel_map = {}
for i in range(len(s3)):
    if s3[i] in 'aeiou':
        vowel_map[s3[i]] = i
print(vowel_map)
# Output: {'a': 0, 'e': 4}

# 4. Count Words in a String
s4 = 'hai hello how are you bye'
print(len(s4.split()))
# Output: 6

# 5. Separate Characters by Category
s5 = 'Ha6753jkuds@hsdy'
lower, upper, digit, spec = '', '', '', ''
for char in s5:
    if char.islower(): lower += char
    elif char.isupper(): upper += char
    elif char.isdigit(): digit += char
    else: spec += char
print(f"Lower: {lower}, Upper: {upper}, Digit: {digit}, Spec: {spec}")
# Output: Lower: ajkudshsdy, Upper: H, Digit: 6753, Spec: @

# 6. Square of Integers in a List
L6 = [2, 'hi', 5, 10.5, 3]
squares = [i**2 for i in L6 if type(i) == int]
print(squares)
# Output: [4, 25, 9]

# 7. Binary Bit Flip
s7 = '0110110010'
flipped = "".join(['1' if b == '0' else '0' for b in s7])
print(flipped)
# Output: 1001001101

# 8. Character Frequency Count
s8 = 'abacbaacc'
freq = {}
for char in s8:
    freq[char] = freq.get(char, 0) + 1
print(freq)
# Output: {'a': 4, 'b': 2, 'c': 3}
