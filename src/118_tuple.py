iconsiam_coordinate = (13.726294415060304, 100.51036937945553)
siamparagon_coordinate = (13.746233828725202, 100.53476597754464)
centralworld_coordinate = (13.745988627621033, 100.53998544365108)

# Print
print(type(iconsiam_coordinate))
print(iconsiam_coordinate)
print(siamparagon_coordinate)
print(centralworld_coordinate)

# Open coordinate in Google Maps
print("Google Maps -------------------------------------------")
base_url = "https://www.google.com/maps/search/?api=1&query="
print(f"IconSiam - {base_url}{iconsiam_coordinate[0]},{iconsiam_coordinate[1]}")
print(f"SiamParagon - {base_url}{siamparagon_coordinate[0]},{iconsiam_coordinate[1]}")
print(f"ContralWorld - {base_url}{centralworld_coordinate[0]},{iconsiam_coordinate[1]}")

# List of tuple
print("List of tuple-------------------------------------------")
department_stores = [
    ("IconSiam", (13.726294415060304, 100.51036937945553)),
    ("SiamParagon", (13.746233828725202, 100.53476597754464)),
    ("CentralWorld", (13.745988627621033, 100.53998544365108)),
]

print(department_stores)
print(department_stores[0])
print(department_stores[0][0])
print(department_stores[0][1])
print(department_stores[0][1][0])
