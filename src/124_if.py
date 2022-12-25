### Noodle Calculator ###
# Beef Noodle - Small, Big, Vermicelli Noodle = 50THB, Egg Noodle = 60THB
# Chicken Noodle 40THB - Small, Big, Vermicelli Noodle = 40THB, Egg Noodle = 50THB
# Extra + 10THB
# Take Home + 10THB
# Take Home and Extra + 15THB


def check_extra(is_extra):
    if is_extra:
        print("You ordered extra")
    else:
        print("You ordered normal")


def calculate_noodle_price(meat, noodle, is_extra, is_take_home):

    if meat == "Beef":
        if noodle == "Big" or noodle == "Small" or noodle == "Vermicelli":
            price = 50
        elif noodle == "Egg Noodle":
            price = 60
        else:
            return -1

    elif meat == "Chicken":
        if noodle == "Big" or noodle == "Small" or noodle == "Vermicelli":
            price = 40
        elif noodle == "Egg Noodle":
            price = 50
        else:
            return -1
    else:
        return -1

    if is_extra and is_take_home:
        price += 15
    elif is_extra:
        price += 10
    elif is_take_home:
        price += 10

    return price


meat1 = "Beef"
noodle1 = "Egg Noodle"
is_extra1 = False
is_take_home1 = False

check_extra(is_extra1)

price1 = calculate_noodle_price(meat1, noodle1, is_extra1, is_take_home1)
print(f"price1 = {price1}")

meat2 = "Beef"
noodle2 = "Egg Noodle"
is_extra2 = True
is_take_home2 = True
price2 = calculate_noodle_price(meat2, noodle2, is_extra2, is_take_home2)
print(f"price1 = {price2}")
