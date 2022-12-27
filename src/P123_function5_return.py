import math


def area_square(length):
    area = length * length
    return area
    print("Returning Area!")


def area_circle(radius):
    area = math.pi * radius**2
    return area


def volume_pringles(radius, height):
    area = area_circle(radius)
    volume = area * height
    return volume


if __name__ == "__main__":

    length1 = 5
    area1 = area_square(length1)
    print(f"area1 = {area1}")

    length2 = 7
    area2 = area_square(length=length2)
    print(f"area2 = {area2}")

    radius3 = 6
    area3 = area_circle(radius3)
    print(f"area3 = {area3:.2f} cm²")

    radius4 = 6
    height4 = 25
    volume4 = volume_pringles(radius4, height4)
    print(f"volume4 = {volume4:10.2f} cc.")
