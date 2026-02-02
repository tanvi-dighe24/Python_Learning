# Program to extract lowercase characters with even ASCII values
s = "Python Programming 2026"
res = ""
for char in s:
    if 'a' <= char <= 'z':
        if ord(char) % 2 == 0:
            res += char
print(res)


# Program to check if the last digit of an integer is even
num = 1458
last_digit = num % 10
if last_digit % 2 == 0:
    print("Last digit is even")
else:
    print("Last digit is odd")


# Program to extract key-value pairs where key is string and value is integer
d = {'name': 'John', 'age': 25, 10: 'id', 'score': 90}
new_d = {}
for k, v in d.items():
    if type(k) == str and type(v) == int:
        new_d[k] = v
print(new_d)


# Program to extract pairs where key and value are the same
d = {1: 1, 'a': 'b', 10: 20, 'python': 'python'}
new_d = {}
for k, v in d.items():
    if k == v:
        new_d[k] = v
print(new_d)


# Program to extract all non-default values from a list
data = [1, 0, "hello", "", True, False, None, []]
result = []
for x in data:
    if x:
        result.append(x)
print(result)


# Program to replace spaces with stars in a string
s = "hello world how are you"
res = ""
for char in s:
    if char == " ":
        res += "*"
    else:
        res += char
print(res)



# Program to count the occurrence of a specific character
s = "engineering"
char_to_find = "e"
count = 0
for char in s:
    if char == char_to_find:
        count += 1
print("Count is:", count)



# Program to reverse each word in a string without changing their order
s = 'always keep smile'
words = s.split()
result_list = []

for word in words:
    reverse_word = word[::-1]
    result_list.append(reverse_word)

output = " ".join(result_list)
print(output)




    
