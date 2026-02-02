# Program to extract all numeric digits from a string
s = "Patient ID 102 and Age 45"
res = ""
for char in s:
    if '0' <= char <= '9':
        res += char
print(res)


# Program to find the largest number in a list using a loop
nums = [12, 45, 2, 89, 33]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print("Largest number is:", largest)



# Program to count vowels and consonants in a string
s = "health care"
vowels = "aeiouAEIOU"


# Program to combine two lists into a dictionary
keys = ["name", "dept", "exp"]
values = ["Dr. Smith", "Cardiology", 10]
info = {}

for i in range(len(keys)):
    info[keys[i]] = values[i]

print(info)v_count = 0
c_count = 0

for char in s:
    if char.isalpha(): # check if it is a letter
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)




# Program to remove duplicate items from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for x in my_list:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)





