# guess game with try except, break, continue, exit
import random

secret = random.randrange(1, 100)
guess = -1
guess_limit = 10
guess_count = 0

while guess != secret and guess_count < guess_limit:

    try:
        guess_text = input("Please guess number 1-100: ")
        guess = int(guess_text)
        guess_count += 1
    except ValueError as err:
        if guess_text == "q" or guess_text == "Q":
            # break
            print("Bye bye")
            exit(0)
        else:
            # print(f"Please enter interger only: {err}")
            print("Not a number. Please enter interger only")
            continue

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

    if guess_count > guess_limit - 3:
        print(f"You have {guess_limit-guess_count} times left.")

if secret == guess:
    print("You win")
else:
    print("You lost")
