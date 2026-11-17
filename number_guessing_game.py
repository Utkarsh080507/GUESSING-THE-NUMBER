import random


MIN_NUMBER = 1
MAX_NUMBER = 500


def play_game():
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guesses = 0

    print(f"\nI'm thinking of a number from {MIN_NUMBER} to {MAX_NUMBER}.")

    while True:
        answer = input("Your guess: ").strip()

        try:
            guess = int(answer)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(f"Choose a number from {MIN_NUMBER} to {MAX_NUMBER}.")
            continue

        guesses += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"You got it in {guesses} guesses!")
            return


def main():
    print("Number Guessing Game")

    while True:
        play_game()
        if input("Play again? (y/n): ").strip().lower() not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
