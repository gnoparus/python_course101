stocks = [
    50,
    60,
    40,
    35,
    70,
    65,
    45,
    55,
]

fruits = [
    "banana",
    "apple",
    "payaya",
    "durian",
    "mango",
    "longan",
    "lychee",
    "lemon",
]

print(len(fruits))
print(len(stocks))
print(fruits)
print(stocks)

# index, find
index_apple = fruits.index("apple")

print("index-----------------------------")
print(f"index_apple: {index_apple}")

# count
count_apple = fruits.count("apple")
print("count-----------------------------")
print(f"count_apple: {count_apple}")

# append
fruits.append("cherry")
stocks.append(99)

print("append-----------------------------")
print(len(fruits))
print(len(stocks))
print(fruits)
print(stocks)

# pop
last_fruit = fruits.pop()
last_stock = stocks.pop()

print("pop-----------------------------")
print(f"last_fruit: {last_fruit}")
print(f"last_stock: {last_stock}")
print(len(fruits))
print(len(stocks))
print(fruits)
print(stocks)


# sort, reverse
fruits.sort(reverse=True)
stocks.sort(reverse=True)

print("sort-----------------------------")
print(len(fruits))
print(len(stocks))
print(fruits)
print(stocks)

# insert
fruits.insert(1, "watermelon")
stocks.insert(1, 88)

print("insert-----------------------------")
print(len(fruits))
print(len(stocks))
print(fruits)
print(stocks)

# extend
fruits.extend(stocks)

print("extend-----------------------------")
print(len(fruits))
print(len(stocks))
print(fruits)
print(stocks)

# remove

fruits.remove("apple")
stocks.remove(60)
print("remove-----------------------------")
print(len(fruits))
print(len(stocks))
print(fruits)
print(stocks)


# clear
fruits.clear()
stocks.clear()
print("clear-----------------------------")
print(len(fruits))
print(len(stocks))
print(fruits)
print(stocks)
