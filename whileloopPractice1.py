n = 6437      # Your starting number
rev = 0       # Your "empty stack" where the reversed number will go

while n != 0:
    ld = n % 10          # 1. Get the last digit
    rev = rev * 10 + ld  # 2. Push it to the new number
    n = n // 10          # 3. Chop off the last digit from 'n'

count = 1
while count <= 3:
    print("Health System Active")
    count += 1
else:
    print("Loop finished successfully.")

# Using 'not in' to filter duplicates while keeping order
l = [10, 20, 10, 30, 40, 20, 50]
res = []

for i in l:
    if i not in res:
        res.append(i)
print("Unique List:", res)

# Example: n=50 (Find sum of 1+3+5...+49)
n = 50
odd_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        odd_sum += i
print(f"Total Sum of Odd Numbers (1 to {n}):", odd_sum)

password = "admin"
while True:
    entry = input("Enter Password: ")
    if entry == password:
        print("Access Granted")
        break
    else:
        print("Access Denied. Try again.")

# System checks if entered OTP matches the stored one
correct_otp = "1234"
attempts = 3

while attempts > 0:
    user_otp = input("Enter PhonePe OTP: ")
    if user_otp == correct_otp:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print(f"Wrong OTP. Attempts remaining: {attempts}")