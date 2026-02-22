# Displaying available hours, but skipping the 12:00 lunch hour
operating_hours = [9, 10, 11, 12, 13, 14, 15, 16]

print("Available Appointment Slots:")
for hour in operating_hours:
    if hour == 12:
        continue  # Skip 12:00 and move to 13:00
    print(f"{hour}:00 is open for booking.")

#--
patient_records = [
    {"id": 101, "name": "Alice"},
    {"id": None, "name": "Unknown"},  # Corrupted record
    {"id": 103, "name": "Charlie"}
]

for patient in patient_records:
    if patient["id"] is None:
        print("Skipping invalid record...")
        continue  # Move to the next patient immediately
    
    print(f"Processing Patient ID: {patient['id']}")

#--
i = 0
while i < 6:
    i += 1
    if i == 3:
        # Skip the number 3
        continue
    print(f"Current count: {i}")

#--
# List of appointment objects (some are missing patient names)
appointments = [
    {"time": "09:00", "patient": "John Doe"},
    {"time": "10:00", "patient": ""},  # Missing name
    {"time": "11:00", "patient": "Jane Smith"},
]

for appt in appointments:
    if not appt["patient"]:
        print(f"Error: No patient assigned for {appt['time']}. Skipping...")
        continue 
    
    # This code only runs if the name exists
    print(f"Sending reminder text to {appt['patient']} for {appt['time']}.")


#--
# Logic to find a specific slot for a specialist
slots = [8, 9, 10, 11, 12, 13, 14, 15]
booked_slots = [9, 11]
lunch_hour = 12

for slot in slots:
    # Guard 1: Skip if already booked
    if slot in booked_slots:
        continue
        
    # Guard 2: Skip if it's lunch
    if slot == lunch_hour:
        continue
        
    # Guard 3: Skip if it's too early for this doctor
    if slot < 10:
        continue

    print(f"Valid slot found: {slot}:00")    


#--
# Processing multiple doctors' schedules
hospital_staff = {
    "Dr. Khan": [9, 10, 11],
    "Dr. Lee": [14, 15, 16]
}

for doctor, schedule in hospital_staff.items():
    print(f"Checking {doctor}...")
    for hour in schedule:
        if hour == 11:
            print(f"Skipping {hour}:00 (Staff Meeting)")
            continue
        print(f"Booking {hour}:00 for {doctor}")




        
