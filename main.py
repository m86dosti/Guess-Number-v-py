import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guess Number Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

guess_number()
