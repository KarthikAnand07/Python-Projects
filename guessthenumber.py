import random

def generate_number(lower=1, upper=10):
    return random.randint(lower, upper)

def get_user_guess():
    try:
        guess = int(input("Enter your guess: "))
        return guess
    except ValueError:
        print("Please enter a valid number.")
        return None

def check_guess(guess, target):
    if guess < target:
        print("Your guess is too low.")
        return False
    elif guess > target:
        print("Your guess is too high")
        return False
    else:
        print("Congratulations! You've guessed the number!")
        return True

def main():
    lower_bound = 1
    upper_bound = 10
    target_number = generate_number(lower_bound, upper_bound)
    guessed_correctly = False

    print(f"Guess the number between {lower_bound} and {upper_bound}.")

    while not guessed_correctly:
        guess = get_user_guess()
        if guess is not None:
            guessed_correctly = check_guess(guess, target_number)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        main()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    main()
