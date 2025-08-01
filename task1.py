"""
Task 1: Music Concert Ticketing System
During the Jos Summer Music Concert, ticket sales were recorded as follows:

tickets = {"VIP": 50, "Regular": 150, "Student": 75}

Later in the day:
- A new "Backstage" experience with 10 tickets was introduced.
- The "Student" category sold out completely.
- The team wanted to keep a record of the day’s sales before preparing for next week’s concert.

"""

tickets = {"VIP": 50, "Regular": 150, "Student": 75}
tickets["Backstage"] = "10"
sold_out = {"Student":75}
#vip = tickets["VIP"]
#print(f"The sales for VIP section are", vip)
#regular = tickets["Regular"]
#print(f"The sales for Regular section are", regular)
#student = tickets["Student"]
#print(f"The sales for Student section are", student)
#backstage = tickets["Backstage"]
#print(f"The sales for backstage section are", backstage)
tickets.pop("Student")
print(f"The available tickets are:",tickets)
print(f"The sold out tickets are:", sold_out)

