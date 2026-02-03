# Create a dictionary mapping string elements to their first and last characters
L = ['hai', 34, 3.4, 'hello', 90, 'byebye']
out = {}
for item in L:
    if type(item) == str:
        out[item] = item[0] + item[-1]
print(out)

# Extract string values from a list only if the string is a palindrome
L = ['madam', 'python', 'level', 'world']
palindromes = []
for s in L:
    if type(s) == str and s == s[::-1]:
        palindromes.append(s)
print(palindromes)


# Return the positions of vowels present in the given string
s = 'apple'
vowels = 'aeiou'
out = {}
for i in range(len(s)):
    if s[i] in vowels:
        out[s[i]] = i
print(out)


# Count the number of words in a string
s = 'hai hello how are you bye'
words = s.split()
print(len(words))


# Extract upper, lower, digit, and special characters present in a string
s = 'Ha6753jkuds@hsdy'
lower = ''
upper = ''
digit = ''
spec = ''
for char in s:
    if char.islower():
        lower += char
    elif char.isupper():
        upper += char
    elif char.isdigit():
        digit += char
    else:
        spec += char
print(lower, upper, digit, spec)



# Print the square of all the integers present in a list
L = [2, 'hi', 5, 10.5, 3]
for i in L:
    if type(i) == int:
        print(i**2)
        

# Binary bit flip: replace '0' with '1' and '1' with '0'
input_str = '0110110010'
output_str = ''
for bit in input_str:
    if bit == '0':
        output_str += '1'
    else:
        output_str += '0'
print(output_str)


# Count the frequency of each character in a string
input_str = 'abacbaacc'
out = {}
for char in input_str:
    if char in out:
        out[char] += 1
    else:
        out[char] = 1
print(out)
