from datetime import date


name = "Bob"
dob = date(1997, 12, 25)
print(f"dob {dob}")

today = date.today()
this_year = today.year
print(f"this_year {this_year}")

age = this_year - dob.year

print(f"There is a student. His name is {name}.")
print(f"{name} is {age} years old.")
print(f"{name} loves to study programming")
print(f"His birthday is {dob}.")
print("Bob's favourite quote is \"Imagination is more important than knowledge\" ")

