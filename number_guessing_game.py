import random


def mode(name="player"):
    print(f"hi {name}! let's try guessing a number between 1 to 50!")
    print("first let's choose the difficulty level.")
    print("easy = 10 guesses\nmedium = 5 guesses\nhard = 3 guesses")
    while True:
        chosen_mode = input(f"Which mode will it be {name}? ").strip().lower()
        if chosen_mode == 'easy':
            return 10
        elif chosen_mode == 'medium':
            return 5
        elif chosen_mode == 'hard':
            return 3
        else:
            print(f"{name}, you have to choose from the given options!")


def guessing_game(name="player", max_guess=5):
    while True:
        computers_choice = random.randint(1, 50)
        guess_count = 0
        guess_remain = max_guess
        while True:
            try:
                player_choice = int(
                    input(f"guess a number between 1 to 50 {name}: "))
                if player_choice not in range(1, 51):
                    print(f"{name}, you must pick a number between 1 to 50!")
                    continue
                guess_remain -= 1
                guess_count += 1
                if player_choice == computers_choice:
                    print("you win!")
                    print(
                        f"congratz {name}, you got it on guess number {guess_count} ")
                    break
                elif player_choice < computers_choice:
                    print("Too low!")
                else:
                    print("Too high!")
                if guess_remain <= 0:
                    print(f"You're out of guesses...sorry {name}")
                    print(f"The chosen number was {computers_choice}.")
                    break
            except ValueError:
                print(f"You must enter a number {name}!")
        while True:
            do_continue = input(
                f"would you like to play again {name}? yes or no?\n").lower().strip()
            if do_continue == 'yes':
                max_guess = mode(name)
                break
            elif do_continue == "no":
                print(f"come back soon {name}!")
                return
            else:
                print("it's a yes or no question!")
                continue


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="personalizing the game experience!"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", default="player",
        help="enter player name."
    )

    args = parser.parse_args()
    max_guess = mode(args.name)
    guessing_game(args.name, max_guess)
