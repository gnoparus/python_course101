from datetime import date


def tell_story(name, year, month, day):

    dob = date(year, month, day)
    print(f"dob {dob}")

    today = date.today()
    this_year = today.year
    print(f"this_year {this_year}")

    age = this_year - dob.year

    print(f"There is a student. His name is {name}.")
    print(f"{name} is {age} years old.")
    print(f"{name} loves to study programming")
    print(f"His birthday is {dob}.")
    print(
        f'{name}\'s favourite quote is "Imagination is more important than knowledge" '
    )
    print("-" * 40)


tell_story("Frank", 2000, 2, 28)
tell_story("George", 1995, 8, 19)
tell_story("Henry", 2005, 9, 2)
