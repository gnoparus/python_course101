noodle_order1 = {
    "order_id": 1,
    "meat": "Beef",
    "noodle": "Big",
    "is_extra": True,
    "is_take_home": False,
    "quantity": 2,
}

noodle_orders = [
    {
        "order_id": 2,
        "meat": "Chicken",
        "noodle": "Small",
        "is_extra": False,
        "is_take_home": False,
        "quantity": 1,
    },
    {
        "order_id": 3,
        "meat": "Beef",
        "noodle": "Egg Noodle",
        "is_extra": True,
        "is_take_home": False,
        "quantity": 1,
    },
    {
        "order_id": 4,
        "meat": "Chicken",
        "noodle": "Small",
        "is_extra": True,
        "is_take_home": False,
        "quantity": 1,
    },
]


def print_noodle_order(order):
    # print(order)
    print(order["order_id"])
    print(order["meat"])
    print(order["noodle"])
    print(order["is_extra"])
    print(order["is_take_home"])
    print(order["quantity"])
    print("-" * 40)


print_noodle_order(noodle_order1)

print_noodle_order(noodle_orders[0])
print_noodle_order(noodle_orders[1])
print_noodle_order(noodle_orders[2])
