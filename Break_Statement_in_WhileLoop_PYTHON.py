# Finding the first number divisible by 7
i = 1
while i <= 100:
    if i % 7 == 0:
        print(f"Found the first multiple of 7: {i}")
        break  # Stops the loop immediately
    i += 1

#2
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    if fruit == "cherry":
        print("Found the cherry! Stopping search.")
        break
    print(f"Checking {fruit}...")


#3
while True:
    command = input("Enter a command (type 'exit' to quit): ").lower()
    
    if command == "exit":
        print("Goodbye!")
        break
    
    print(f"Executing: {command}")


#Breaking Out of Nested Loops
# Searching through a 2D grid (e.g., a weekly schedule)
schedule = [
    ["Available", "Booked"],  # Monday
    ["Booked", "Available"],  # Tuesday
    ["Available", "Available"] # Wednesday
]

found = False
for day_index, day in enumerate(schedule):
    for slot_index, status in enumerate(day):
        if status == "Available":
            print(f"Found slot at Day {day_index}, Slot {slot_index}")
            found = True
            break  # Exits the 'slot' loop
    if found:
        break  # Exits the 'day' loop


#4
while True:
    phone = input("Enter patient phone (10 digits): ")
    
    if len(phone) == 10 and phone.isdigit():
        print("Phone number saved.")
        break  # The only way to escape the loop
    else:
        print("Invalid input. Please try again.")


#5
doctors = ["Dr. Smith", "Dr. Jones", "Dr. Taylor"]
search_name = "Dr. House"

for doc in doctors:
    if doc == search_name:
        print(f"Match found: {doc}")
        break
else:
    # This runs ONLY if the loop finishes without finding a match
    print(f"Error: {search_name} is not in the system.")



    

    
