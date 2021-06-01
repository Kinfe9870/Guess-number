import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Enter your guess between 1 and {x}: "))
        if guess < random_number:
            print("Too low try again")
        elif guess > random_number:
            print("Too high try again")
    print(f"Correct {random_number} was the correct answer ")


guess(10)
