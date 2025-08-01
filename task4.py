"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

# print(participants_snapshot)
# print(participants)

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}
participants["Guest"] = "Daisy"
participants.pop("Student")
pre_record = participants.copy()
participants.popitem()
print(f"The record for the day is: ",pre_record)
print(f"The current record is:", participants)

