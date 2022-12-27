import random

# a = 5

# while a == 5:
#     print("infinite loop")

secret = random.randrange(1, 100)
guess = -1

while guess != secret:
    guess = int(input("Please guess number 1-100: "))
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

print("You win")
