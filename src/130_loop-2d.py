temperature_data = [  # at 9.00, 12.00, 15.00, 18.00
    [25.5, 24.3, 23.8, 24.6],  # Monday
    [24.6, 25.2, 23.9, 25.2],  # Tuesday
    [22.2, 23.4, 25.9, 24.3],  # Wednesday
    [23.9, 28.2, 24.9, 23.5],  # Thursday
    [25.5, 25.8, 26.9, 25.8],  # Friday
]

# iterate 2d list with 2d loop
for row in temperature_data:
    for temp in row:
        print(temp)
    print("end of column")
print("end of row")


# iterate and calculate 2d
temp_week = 0

for row in temperature_data:
    temp_day = 0

    for temp in row:
        temp_day += temp
        temp_week += temp
    print(f"mean temp of day {temp_day/4:0.2f}")
print(f"mean temp of week {temp_week/20:0.2f}")
