import random

secret = random.randrange(1, 100)
guess = -1
guess_limit = 10
guess_count = 0

while guess != secret and guess_count < guess_limit:
    guess = int(input("Please guess number 1-100: "))
    guess_count += 1

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

    if guess_count > guess_limit - 3:
        print(f"You have {guess_limit-guess_count} times left.")

if guess_count == guess_limit:
    print("You lost")
else:
    print("You win")
