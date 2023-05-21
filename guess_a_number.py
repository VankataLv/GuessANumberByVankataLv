import random


def name_validity(name):
    validity = name.isalpha()
    if not validity:
        print(f"> Your name probably contains ONLY letters.")
    if len(name) < 2:
        print(f"> Your name is probably longer than 1 letter.")
        validity = False
    if not validity:
        print("> You can try again.")
    return validity


def valid_user_guess(guess: int):
    validity = True
    if guess not in range(1, 101):
        print(f"> Out of range! You should guess a number between 1-100.")
        validity = False
    return validity


print("> -----------------------------------------------")
print("> Dear player, welcome to my Guess a number game!")
print("> -----------------------------------------------")
while True:
    user_name = input("> What is your name? \n> ")
    valid_name = name_validity(user_name)             # to check if the name is real
    if valid_name:
        break
user_name = user_name.capitalize()
print(f"> Hello {user_name}!\n> Let's play!\n-----------------------------------------------")
computer_random = random.randint(1, 100)
user_guess = int(input("> I have picked a number, between 1 and 100.\n> Try to guess it!\n> "))
while user_guess != computer_random:
    valid_guess = valid_user_guess(user_guess)             # to check if the user input is within limit: 1- 100
    if valid_guess:
        user_guess = int(user_guess)
        if user_guess > computer_random:
            print("My number is lower! ")
        elif user_guess < computer_random:
            print("My number is higher! ")
    else:
        user_guess = int(input("> "))
    user_guess = int(input("> Try to guess again!\n> "))
print(">-----------------------------------------------\n> You guessed right!!!\n> You WON!")