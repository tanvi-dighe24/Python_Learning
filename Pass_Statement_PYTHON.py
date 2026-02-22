#--
# Checking appointment status
status = "Confirmed"

if status == "Confirmed":
    pass  # No action needed for confirmed cases
elif status == "Pending":
    print("Sending reminder to patient...")
else:
    print("Handling cancellation...")


#--
class PatientNotFoundError(Exception):
    pass

# Usage in your system
raise PatientNotFoundError("ID 505 not found in database.")


#--
# Attempting to delete a temporary cache file
import os

try:
    os.remove("temp_log.txt")
except FileNotFoundError:
    # If the file isn't there, we don't care. Do nothing.
    pass


#--
patient_id=[101,102,103,104,105,10]
target=103
for id in patient_id:
    if id==target:
        print('target found!')
        break
    print('checking for target in ids')


#--
def process_billing(patient_id, amount):
    # Logic for insurance and credit cards will go here later
    pass 

def update_patient_records():
    pass

# The program runs fine even though these functions are empty
process_billing(101, 500)
print("Billing function called, but nothing happened yet.")    
    
