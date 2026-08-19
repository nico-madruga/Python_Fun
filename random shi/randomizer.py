import random

print("thinking of a number between 1 and 50")

MAX_VALUE = 50
MIN_VALUE = 1

secret = random.randint(MIN_VALUE, MAX_VALUE)
guess = 0
tries = 0

while guess != secret:
    text = input("guess it:")
    guess = int(text)

    if guess < MIN_VALUE or guess > MAX_VALUE:
        print("you out of bounds twin")
    elif guess > secret:
        print("you too high twin")
    elif guess < secret:
        print("you too low twin")
    else:
        print("congrats twin")