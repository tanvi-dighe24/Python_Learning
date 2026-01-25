#PhonePay OTP Checking
correct_otp = "1234"
user_otp = ""
while user_otp != correct_otp:
    user_otp = input("Enter the 4-digit OTP: ")
    if user_otp != correct_otp:
        print("Incorrect OTP entered, Try again.")
else:
print("Login Successful")


#Infinite Loop Until Correct Password:
password = "python123"
while True:
    attempt = input("Enter Password: ")
    if attempt == password:
        print("Access Granted!")
        break  # This stops the infinite loop
    else:
        print("Wrong password. Access Denied.")
        

#Remove Duplicates from a List (No Sets)        
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
index = 0
   while index < len(original_list):
    item = original_list[index]
    if item not in unique_list:
        unique_list.append(item)
    index += 1
print("List without duplicates:", unique_list)





