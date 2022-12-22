your_name = input("Please input your name: ")
your_age = input("Please input your age: ")
print(f"Hello {your_name}! \nYour age is {your_age} years old.")

# do a little calculation
your_age_next_year = float(your_age) + 1
print(f"Next year you will be {str(your_age_next_year)} years old.")

# calculate x year in the future
x_year = input("How many years in the future: ")
your_age_x_year = float(your_age) + float(x_year)
print(f"In {x_year} years you will be {str(your_age_x_year)} years old.")
