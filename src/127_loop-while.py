import random

# a = 5

# while a == 5:
#     print("infinite loop")

secret = random.randrange(1, 100)
guess = int(input("Please guess number 1-100: "))

while guess != secret:
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

    guess = int(input("Please guess number again: "))

print("You win")
