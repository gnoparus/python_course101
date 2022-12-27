for i in range(100):
    print("I love you")


text1 = "Last Christmas I gave you my heart"

for char in text1:
    print(char)

for word in text1.split(" "):
    print(word)


# list2 = "But the very next day you gave it away".split(" ")
list2 = ["But", "the", "very", "next", "day", "you", "gave", "it", "away"]

for word in list2:
    print(word)

# list2_length = len(list2)
list2_length = 9
print(f"list2_length = {list2_length}")

for i in range(list2_length):
    print(f"i = {i}, list2[i] = {list2[i]}")
